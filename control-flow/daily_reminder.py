Task = input("What is your daily reminder task?")
Priority = input("What is the priority level (low, medium, high)?")
Time_Bound = input("Is this task time-bound? (yes/no)")
is_priority = False

match Priority :
    case "high":
        is_priority = True
 
    case "medium":
        is_priority = True
    case "low":
        is_priority = True
    case _:
        print("Invalid priority level. Please enter low, medium, or high.")

if Time_Bound == "yes" and is_priority:
    print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today")
elif Time_Bound == "no" and is_priority:
    print(f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")
