from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a single care activity for a pet."""
    title: str
    duration_minutes: int
    priority: str # "high", "medium", "low"
    is_completed: bool = False

    def mark_complete(self) -> None:
        """Changes the task's completion status to True."""
        self.is_completed = True

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
    """The logic engine that organizes and prioritizes tasks across all pets."""
    @staticmethod
    def generate_plan(owner: Owner):
        """Sorts all pet tasks by priority and fits them within the owner's available time."""
        schedule = []
        remaining_time = owner.available_time_minutes
        
        # Gather all tasks across all pets
        all_tasks = []
        for pet in owner.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))
                
        # Simple sorting mechanism by priority string values
        priority_map = {"high": 1, "medium": 2, "low": 3}
        sorted_tasks = sorted(all_tasks, key=lambda x: priority_map.get(x[1].priority, 3))
        
        for pet, task in sorted_tasks:
            if remaining_time >= task.duration_minutes:
                remaining_time -= task.duration_minutes
                schedule.append({"pet": pet.name, "task": task.title, "duration": task.duration_minutes, "priority": task.priority, "status": "Scheduled"})
            else:
                schedule.append({"pet": pet.name, "task": task.title, "duration": task.duration_minutes, "priority": task.priority, "status": "Skipped"})
        return schedule