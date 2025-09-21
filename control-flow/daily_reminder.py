task = input("What is your daily reminder task? ")
priority = input("What is the priority level (low, medium, high)? ").lower()
time_bound = input("Is this task time-bound? (yes/no) ").lower()
is_priority = False

match priority :
    case "high":
        is_priority = True
 
    case "medium":
        is_priority = True
    case "low":
        is_priority = True
    case _:
        print("Invalid priority level. Please enter low, medium, or high.")

if time_bound == "yes" and is_priority:
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today")
elif time_bound == "no" and is_priority:
    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
