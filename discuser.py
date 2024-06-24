import json
import pprint
import time
from dataclasses import dataclass
from typing import List, Dict, Any

import openai
from gigachat import GigaChat

ARBITRATOR_PROMPT = ''
PARTICIPANTS_PROMPT = ''


@dataclass(frozen=True)
class ConfigI:
    pass


@dataclass(frozen=True)
class ConfigGigaChat:
    api_key: str


@dataclass(frozen=True)
class Config:
    api_key: str
    model: str


class LLMI:
    def message_gen(self, message: str, clear_gen: bool = False) -> List[Dict[str, str]]:
        raise "Not set"

    @property
    def messages(self) -> List[Dict[str, str]]:
        raise "Not set"

    @property
    def system_prompt(self) -> str:
        raise "Not set"

    def request(self) -> Any:
        raise "Not set"


class DiscussesI:

    def debug(self) -> None:
        raise "Not set"

    def request(self, message: str) -> str:
        raise "Not set"


class GC(LLMI):
    def __init__(self, config: ConfigGigaChat, system_prompt: str = "") -> None:
        self.__api_key = config.api_key

        self.__system_prompt = system_prompt
        self.__messages = f"Промпт: {self.__system_prompt}\n"

    def message_gen(self, message: str, clear_gen: bool = False) -> str:
        if clear_gen:
            self.__messages = f"Промпт: {self.__system_prompt}\n" + f"Пользователь: {message}\n" if self.__system_prompt \
                else f"Пользователь: {message}\n"
        else:
            self.__messages += f"Пользователь: {message}\n"
        return self.__messages

    @property
    def messages(self) -> str:
        return self.__messages

    @property
    def system_prompt(self) -> str:
        return self.__system_prompt

    def request(self) -> Any:
        try:
            with GigaChat(credentials=self.__api_key, verify_ssl_certs=False) as giga:
                response = giga.chat(self.__messages)
            return response.choices[0].message.content
        except Exception as ex:
            print(ex)


class GPT:
    def __init__(self, config: Config, system_prompt: str = "") -> None:
        self.__api_key = config.api_key
        self.__model = config.model

        self.__system_prompt = system_prompt
        self.__messages = [{"role": "system", "content": self.__system_prompt}]

    def message_gen(self, message: str, clear_gen: bool = False) -> List[Dict[str, str]]:
        if clear_gen:
            self.__messages = [{"role": "system", "content": self.__system_prompt},
                               {"role": "user", "content": message}] if self.__system_prompt \
                else [{"role": "user", "content": message}]
        else:
            self.__messages.append({"role": "user", "content": message})
        return self.__messages

    @property
    def messages(self) -> List[Dict[str, str]]:
        return self.__messages

    @property
    def system_prompt(self) -> str:
        return self.__system_prompt

    def request(self) -> Any:
        openai.api_key = self.__api_key
        try:
            res = openai.ChatCompletion.create(
                model=self.__model,
                messages=self.__messages
            ).choices[0].message.content
            return res
        except Exception as ex:
            print(ex)


class Chat:
    def __init__(self, arbitrator: DiscussesI, first_llm: DiscussesI, second_llm: DiscussesI) -> None:
        self.__arbitrator = arbitrator
        self.__first_participant = first_llm
        self.__second_participant = second_llm

        # print(self.__arbitrator.request(self.__arbitrator.prompt))

        self.__history = []

    @property
    def history(self) -> List[Dict[str, str]]:
        return self.__history

    def debug(self):
        self.__first_participant.debug()
        self.__second_participant.debug()

    def fit(self, init_message: str = "") -> None:
        if init_message:
            first_participant_stance = self.__first_participant.request(message=init_message)
            self.__history.append({"first_participant": first_participant_stance})

            second_participant_stance = self.__second_participant.request(message=first_participant_stance)
            self.__history.append({"second_participant": second_participant_stance})
        else:
            first_participant_stance = self.__first_participant.request(message=self.__history[-1]["second_participant"])
            self.__history.append({"first_participant": first_participant_stance})

            second_participant_stance = self.__second_participant.request(message=first_participant_stance)
            self.__history.append({"second_participant": second_participant_stance})


class Arbitrator(DiscussesI):
    def __init__(self, llm: LLMI) -> None:
        self.__llm = llm

    def debug(self):
        pprint.pprint(self.__llm.messages)

    def request(self, message: str) -> str:
        self.__llm.message_gen(message=message, clear_gen=True)

        return self.__llm.request()

    def evaluate(self, first_state: str, second_state: str):
        pass


class Participant(DiscussesI):
    def __init__(self, llm: LLMI) -> None:
        self.__llm = llm

    def debug(self):
        pprint.pprint(self.__llm.messages)

    def request(self, message: str) -> str:
        self.__llm.message_gen(message=message)

        return self.__llm.request()


if __name__ == '__main__':
    base_config = ConfigGigaChat(
        api_key='',
    )

    GC1 = GC(base_config, system_prompt="Напиши противоположные мнения в Социальной сфере")
    GC2 = GC(base_config, system_prompt="Твоя задача отстаивать позицию: Все люди равны и заслуживают одинаковых возможностей. Обращай внимание на функциональные и семантические особенности")
    GC3 = GC(base_config, system_prompt="Твоя задача отстаивать позицию: Некоторые люди более талантливы и заслуживают большего успеха. Обращай внимание на функциональные и семантические особенности")

    chat = Chat(
        arbitrator=Arbitrator(GC1),
        first_llm=Participant(GC2),
        second_llm=Participant(GC3)
    )

    chat.fit(init_message="Докажи Все люди равны и заслуживают одинаковых возможностей")

    chat.fit()
    chat.fit()
    # chat.fit()

    chat.debug()

    pprint.pprint(chat.history)
