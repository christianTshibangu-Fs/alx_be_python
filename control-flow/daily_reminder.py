task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

urgency_message = ""
if time_bound.lower() == "yes":
    urgency_message = " that requires immediate attention today!"

# Traitement de la tâche avec la priorité via le "match case"
match priority.lower():
    case "high":
        print(f"Reminder: '{task}' is a high priority task{urgency_message}.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task{urgency_message}.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please choose 'high', 'medium', or 'low'.")
