import ctypes

# Define the necessary constants
ES_CONTINUOUS = 0x80000000
ES_DISPLAY_REQUIRED = 0x00000002
ES_SYSTEM_REQUIRED = 0x00000001

# Import the SetThreadExecutionState function
SetThreadExecutionState = ctypes.windll.kernel32.SetThreadExecutionState

# Set the thread execution state
previous_state = SetThreadExecutionState(ES_CONTINUOUS | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED)

if previous_state == 0:
    print("Failed to set thread execution state.")
else:
    print("Screen will stay on.")
    print("Press 'y' followed by Enter to exit and restore previous behavior...")

    exit_flag = False
    while not exit_flag:
        user_input = input()
        if user_input == "y":
            exit_flag = True

# Restore the previous thread execution state
SetThreadExecutionState(previous_state)
