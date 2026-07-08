from pawpal_system import Task, Pet

def test_task_completion():
    task = Task(title="Brush teeth", duration_minutes=10, priority="low")
    assert task.is_completed is False
    task.mark_complete()
    assert task.is_completed is True

def test_task_addition():
    pet = Pet(name="Mochi", species="cat")
    assert len(pet.tasks) == 0
    pet.add_task(Task(title="Feeding", duration_minutes=15, priority="high"))
    assert len(pet.tasks) == 1