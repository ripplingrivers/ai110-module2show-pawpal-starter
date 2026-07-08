from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    is_completed: bool = False

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

@dataclass
class Owner:
    name: str
    available_time_minutes: int = 120
    pets: List[Pet] = field(default_factory=list)

class Scheduler:
    @staticmethod
    def generate_plan(owner: Owner):
        pass