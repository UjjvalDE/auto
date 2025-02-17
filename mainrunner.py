import subprocess

# Get the number of times to run the task
num_runs = int(input("Enter the number of times to run the task file: "))

# Loop to execute the task file the specified number of times
for i in range(num_runs):
    print(f"Running task.py (iteration {i + 1}/{num_runs})...")
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    print(result.stdout)  # Display the output of task.py
    print(result.stderr)  # Display any errors from task.py
