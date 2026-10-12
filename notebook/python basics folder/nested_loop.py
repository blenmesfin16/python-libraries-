days = ["Day 1", "Day 2"]
sessions = ["Morning Session", "Afternoon Session", "Evening Session"]

print("--- Event Schedule ---")
# Outer loop: Runs 2 times
for day in days:
    print(f"\n📅 {day}:")
    
    # Inner loop: Runs 3 times for EVERY single day
    for session in sessions:
        print(f"  • {session}")
