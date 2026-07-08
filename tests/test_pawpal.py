import pytest
from pawpal_system import Task, Pet, Owner, Scheduler

def test_recurrence_logic():
    task = Task(title="Daily Feeding", duration_minutes=15, priority="high", start_time_str="08:00", frequency="Daily")
    assert task.is_completed is False
    
    next_task = task.mark_complete()
    assert task.is_completed is True
    assert next_task is not None
    assert next_task.title == "Daily Feeding"
    assert next_task.start_time_str == "08:00"

def test_chronological_sorting_correctness():
    owner = Owner(name="Test Owner")
    pet = Pet(name="Rover", species="dog")
    owner.add_pet(pet)
    
    pet.add_task(Task(title="Late Activity", duration_minutes=10, priority="low", start_time_str="21:00"))
    pet.add_task(Task(title="Early Activity", duration_minutes=10, priority="high", start_time_str="06:00"))
    
    all_pairs = Scheduler.get_all_task_pairs(owner)
    sorted_pairs = Scheduler.sort_by_time(all_pairs)
    
    # The first item in the list must be the 06:00 task
    assert sorted_pairs[0][1].title == "Early Activity"
    assert sorted_pairs[1][1].title == "Late Activity"

def test_conflict_detection_accuracy():
    owner = Owner(name="Test Owner")
    pet1 = Pet(name="Mochi", species="cat")
    pet2 = Pet(name="Biscuit", species="dog")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    
    pet1.add_task(Task(title="Breakfast", duration_minutes=15, priority="high", start_time_str="08:00"))
    pet2.add_task(Task(title="Morning Walk", duration_minutes=30, priority="high", start_time_str="08:00"))
    
    all_pairs = Scheduler.get_all_task_pairs(owner)
    warnings = Scheduler.detect_conflicts(all_pairs)
    
    assert len(warnings) == 1
    assert "Conflict at 08:00" in warnings[0]