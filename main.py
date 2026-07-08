from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    owner = Owner(name="Jordan", available_time_minutes=90)
    mochi = Pet(name="Mochi", species="cat")
    biscuit = Pet(name="Biscuit", species="dog")
    owner.add_pet(mochi)
    owner.add_pet(biscuit)
    
    biscuit.add_task(Task(title="Evening Run", duration_minutes=40, priority="medium", start_time_str="19:00"))
    mochi.add_task(Task(title="Breakfast", duration_minutes=15, priority="high", start_time_str="08:00"))
    
    biscuit.add_task(Task(title="Morning Walk", duration_minutes=30, priority="high", start_time_str="08:00"))

    all_pairs = Scheduler.get_all_task_pairs(owner)
    sorted_pairs = Scheduler.sort_by_time(all_pairs)
    conflicts = Scheduler.detect_conflicts(all_pairs)

    print("\nSmarter Scheduler Diagnostics ")
    print("=" * 65)
    print("CHRONOLOGICALLY SORTED LIST:")
    for pet, task in sorted_pairs:
        print(f"   {task.start_time_str} | [{pet}] {task.title}")
        
    if conflicts:
        print("\nCONFLICT WARNING ALERTS:")
        for warning in conflicts:
            print(f"  {warning}")
    print("=" * 65)

if __name__ == "__main__":
    main()