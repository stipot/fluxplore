from dataclasses import dataclass
from typing import List, Dict


@dataclass
class GeneratedStatementsArguments:
    first_statement: str
    second_statement: str
    first_prompt: str
    second_prompt: str

    first_arguments: List[Dict] | None
    second_arguments: List[Dict] | None


@dataclass
class GeneratedOppositeStatements:
    first_paradigm: str
    second_paradigm: str
    prompt: str

    statements: GeneratedStatementsArguments | None


@dataclass
class GeneratedCompetingParadigms:
    area: str
    prompt: str

    paradigms: List[GeneratedOppositeStatements]




