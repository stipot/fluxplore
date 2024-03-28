from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CompetingArguments:
    first: str
    second: str


@dataclass
class GeneratedStatementsArguments:
    first_statement: str
    second_statement: str
    prompt: str

    arguments: List[CompetingArguments] | None


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




