import json
import pprint
import time
from dataclasses import dataclass, asdict
from typing import Dict, List

import openai

from prompts import GeneratedCompetingParadigms, GeneratedOppositeStatements, GeneratedStatementsArguments


@dataclass(frozen=True)
class Config:
    api_key: str
    model: str


class GPT:
    def __init__(self, config: Config):
        self.__api_key = config.api_key
        self.__model = config.model

    @staticmethod
    def message_gen(message: str):
        return [{"role": "user", "content": message}]

    def request(self, data: List):
        openai.api_key = self.__api_key
        while True:
            try:
                time.sleep(20)
                res = openai.ChatCompletion.create(
                    model=self.__model,
                    messages=data
                ).choices[0].message.content
                print(res)
                res = json.loads(res)
                return res
            except Exception as ex:
                print(ex)


if __name__ == '__main__':
    chat = GPT(Config(api_key='', model="gpt-3.5-turbo-0125"))

    area = 'Societal'

    data = GeneratedCompetingParadigms(
        area=area,
        prompt=' '.join([f"Given the {area} bias context, identify potential competing paradigms which could provide "
                         f"contrasting viewpoints. Use the format:",
                         '[{"first": "Labor Unions", "second": "Tech Companies", "desc": "Labor unions may express concerns '
                         'about job displacement and socioeconomic inequality resulting from technological '
                         'advancements, while techcompanies may emphasize the benefits of innovation, productivity, '
                         'and economic growth."}, {"first": "Labor Unions", "second": "Tech Companies", "desc": "Labor unions may express concerns '
                         'about job displacement and socioeconomic inequality resulting from technological '
                         'advancements, while techcompanies may emphasize the benefits of innovation, productivity, '
                         'and economic growth."}]']),
        paradigms=[]
    )

    for paradigm in chat.request(data=chat.message_gen(data.prompt)):
        data.paradigms.append(
            GeneratedOppositeStatements(
                first_paradigm=paradigm['first'],
                second_paradigm=paradigm['second'],
                prompt=f'generate two opposing generalized statements aligning with the chosen paradigms on a '
                       f'selected subject, using a pre-defined template. For instance, given the paradig'
                       f'ms of "{paradigm["first"]}" and "{paradigm["second"]}" in the {area} field, the instruction '
                       f'could be: "Given the'
                       f'paradigms of "{paradigm["first"]}" and "{paradigm["second"]}", generate two opposing '
                       f'statements on the topic of'
                       f'{area}. Use the format: '
                       '{"Labor Unions": "Embracing automation is necessary for efficiency", "Tech Companies": '
                       '"Automation leads to job loss and threatens workers rights"}',
                statements=None
            )
        )

    for paradigm in data.paradigms:
        tewst = chat.request(data=chat.message_gen(paradigm.prompt))
        paradigm.statements = GeneratedStatementsArguments(
            first_statement=tewst[paradigm.first_paradigm],
            second_statement=tewst[paradigm.second_paradigm],
            first_prompt=f'Your task is to advocate for the stance "{tewst[paradigm.first_paradigm]}", and focus on the specific semantic and '
                   'functional implications of this stance. In a dialogue with me (where I will be defending the '
                   'opposing stance), you are required to present 10 unique arguments affirming your position. '
                   'Use the format:'
                   '[{"Argument 1": "Fisrt argument"}, {"Argument 2": "Fisrt argument"}, {"Argument 3": "Fisrt argument"}]',
            second_prompt=f'Your task is to advocate for the stance "{tewst[paradigm.first_paradigm]}", and focus on the specific semantic and '
                   'functional implications of this stance. In a dialogue with me (where I will be defending the '
                   'opposing stance), you are required to present 10 unique arguments affirming your position. '
                   'Use the format:'
                   '[{"Argument 1": "Fisrt argument"}, {"Argument 2": "Fisrt argument"}, {"Argument 3": "Fisrt argument"}]',
            first_arguments=None,
            second_arguments=None
        )

        first_arguments = chat.request(data=chat.message_gen(paradigm.statements.first_prompt))
        print(first_arguments)
        second_arguments = chat.request(data=chat.message_gen(paradigm.statements.first_prompt))
        print(second_arguments)

        paradigm.statements.first_arguments = first_arguments
        paradigm.statements.second_arguments = second_arguments

    print(asdict(data))
    pprint.pprint(asdict(data))
