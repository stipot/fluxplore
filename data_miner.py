import json
import pprint
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
        return openai.ChatCompletion.create(
            model=self.__model,
            messages=data
        ).choices[0].message.content


if __name__ == '__main__':
    chat = GPT(Config(api_key='', model="gpt-3.5-turbo-0125"))

    area = 'Societal'

    data = GeneratedCompetingParadigms(
        area=area,
        prompt=' '.join([f"Given the {area} bias context, identify potential competing paradigms which could provide "
                         f"contrasting viewpoints using the following format:",
                         '[{"first": "Labor Unions", "second": "Tech Companies", "desc": "Labor unions may express concerns '
                         'about job displacement and socioeconomic inequality resulting from technological '
                         'advancements, while techcompanies may emphasize the benefits of innovation, productivity, '
                         'and economic growth."}]']),
        paradigms=[]
    )

    for paradigm in json.loads(chat.request(data=chat.message_gen(data.prompt))):
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
                       f'{area}. Use the following template: '
                       '{"Labor Unions": "Embracing automation is necessary for efficiency", "Tech Companies": '
                       '"Automation leads to job loss and threatens workers rights"}',
                statements=None
            )
        )

    for paradigm in data.paradigms:
        tewst = chat.request(data=chat.message_gen(paradigm.prompt))
        print(tewst)
        tewst = json.loads(tewst)
        paradigm.statements = GeneratedStatementsArguments(
            first_statement=tewst[paradigm.first_paradigm],
            second_statement=tewst[paradigm.second_paradigm],
            prompt='',
            arguments=None
        )

    pprint.pprint(asdict(data))



