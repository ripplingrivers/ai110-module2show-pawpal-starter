from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    owner = Owner(name="Jordan", available_time_minutes=90)
    mochi = Pet(name="Mochi", species="cat")
    biscuit = Pet(name="Biscuit", species="dog")
    owner.add_pet(mochi)
    owner.add_pet(biscuit)
    
    mochi.add_task(Task(title="Feeding", duration_minutes=15, priority="high"))
    biscuit.add_task(Task(title="Morning Walk", duration_minutes=60, priority="high"))
    biscuit.add_task(Task(title="Agility Training", duration_minutes=30, priority="low"))
    
    plan = Scheduler.generate_plan(owner)
    print("\n  Schedule Plan")
    for item in plan:
        print(f"  {item['status']}: [{item['pet']}] {item['task']} ({item['duration']} mins)")

if __name__ == "__main__":
    main()