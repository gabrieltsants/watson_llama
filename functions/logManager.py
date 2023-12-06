llama_completion_dir = getenv("LLAMA_COMPLETION_DIR")
from os import getenv

# Print the command history
def print_history(option):
    print(llama_completion_dir + getenv(option + "_HISTORY"))
    with open(llama_completion_dir + getenv(option + "_HISTORY"), "r") as f:
        for line in f:
            print(line)

# Clear the command history file
def clear_history(option):
    with open(llama_completion_dir + getenv(option + "_HISTORY"), "w") as f:
        f.write("")
