from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class Plataform(Enum):
    GLASSDOOR = 1
    LINKEDIN = 2


@dataclass
class Vaga:
    name: str
    url: str
    plataform: Plataform


class Site:
    url: str
    plataform: Plataform
    vagas: Optional[list[Vaga]] = []
