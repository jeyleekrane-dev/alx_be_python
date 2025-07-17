# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt for the task's priority level
# Convert to lowercase for easier matching
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
# Convert to lowercase for easier matching
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the base reminder message
Reminder = ""

# Use a match-case statement to handle different priority levels
match priority:
    case "high":
        Reminder = f"'{task}' is a high priority task"
    case "medium":
        Reminder = f"'{task}' is a medium priority task"
    case "low":
        Reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        # Handle cases where the priority input is not recognized
        Reminder = f"'{task}' has an unrecognized priority level."
        # print("Warning: Please enter 'high', 'medium', or 'low' for priority.")

# Check if the task is time-bound and modify the reminder accordingly
# This condition applies the "immediate attention" message only if time_bound is 'yes'
# and the priority is not 'low' (as low priority has its own specific message).
if time_bound == "yes" and priority in ["high", "medium"]:
    Reminder += " that requires immediate attention today!"
elif time_bound == "yes" and priority == "low":
    # If it's low priority and time-bound, the "immediate attention" might contradict
    # the "consider completing when you have free time" message.
    # We'll adjust it to still emphasize time-bound for low priority, but keep the
    # "consider completing" part if it was already set.
    # For this specific problem, the example output suggests low priority time-bound
    # tasks still get the "consider completing" message, so we'll stick to that.
    # No change needed if the 'low' case already set its message.
    pass  # The low priority message already handles its specific phrasing.


# Print the customized reminder
print(f"Reminder: {Reminder}")
