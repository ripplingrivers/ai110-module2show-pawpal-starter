from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Task:
    """Represents a single care activity for a pet."""
    title: str
    duration_minutes: int
    priority: str # "high", "medium", "low"
    start_time_str: str  # Format: "HH:MM" (e.g., "08:30")
    frequency: str = "Once"  # "Once", "Daily", "Weekly"
    is_completed: bool = False

    def mark_complete(self) -> None:
        """Changes the task's completion status to True."""
        self.is_completed = True
        if self.frequency == "Daily":
            return Task(title=self.title, duration_minutes=self.duration_minutes, priority=self.priority, start_time_str=self.start_time_str, frequency=self.frequency)
        return None
    
@dataclass
class Pet:
    """Stores individual pet details and their assigned care tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Appends a new care task to the pet's task list."""
        self.tasks.append(task)

@dataclass
class Owner:
    """Manages the owner's profile and multiple pets."""
    name: str
    available_time_minutes: int = 120
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Adds a new pet profile to the owner's account."""
        self.pets.append(pet)

class Scheduler:
    """Calculates chronological sort weights and logs scheduling overlaps."""
    
    @staticmethod
    def get_all_task_pairs(owner: Owner) -> List[tuple[str, Task]]:
        """Gathers a combined collection of all tasks linked to pet identifier text."""
        pairs = []
        for pet in owner.pets:
            for task in pet.tasks:
                pairs.append((pet.name, task))
        return pairs

    @staticmethod
    def sort_by_time(task_pairs: List[tuple[str, Task]]) -> List[tuple[str, Task]]:
        """Sorts tasks chronologically based on their HH:MM clock string values."""
        return sorted(task_pairs, key=lambda pair: datetime.strptime(pair[1].start_time_str, "%H:%M"))
    
    @staticmethod
    def filter_by_pet(task_pairs: List[tuple[str, Task]], pet_name: str) -> List[tuple[str, Task]]:
        """Filters a task collection by matching a designated pet's name."""
        return [p for p in task_pairs if p.lower() == pet_name.lower()]

    @staticmethod
    def detect_conflicts(task_pairs: List[tuple[str, Task]]) -> List[str]:
        """Scans timestamps and logs warning alerts if identical clocks collide."""
        warnings = []
        time_registry: Dict[str, List[str]] = {}
        
        for pet_name, task in task_pairs:
            if task.start_time_str not in time_registry:
                time_registry[task.start_time_str] = []
            time_registry[task.start_time_str].append(f"{pet_name}'s {task.title}")
            
        for clock_time, entries in time_registry.items():
            if len(entries) > 1:
                warnings.append(f"Conflict at {clock_time}: Overlap detected between {', '.join(entries)}.")
        return warnings