from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Action(Enum):
    UNIDO = "Unido"
    ANTES = "Se unió antes"
    ABANDONO = "Abandonó"


@dataclass
class Record:
    line: int
    name: str
    action: Action
    update_at: datetime
