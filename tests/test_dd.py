import os
import subprocess
import time
import re

def test_dd(storage_path):
    input_file = os.path.join(storage_path, 'train2017.zip')
    output_dir = os.path.join(storage_path, 'ddtest')
    output_file = os.path.join(output_dir, 'testfile')

    # Ensure the input file exists
    if not os.path.isfile(input_file):
        return "Error: Input file train2017.zip not found in storage path."

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Execute the dd command
    dd_command = f"dd if={input_file} of={output_file} bs=100k count=100k && sync"
    start_time = time.time()
    result = subprocess.run(["sh", "-c", dd_command], capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    return f"dd operation completed.\nElapsed Time: {elapsed_time:.2f} seconds\n{result.stdout}"


def parse_dd(log_file_path):
    print("parse_dd ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'dd' in log_file_path:
        match = re.search(r"Elapsed Time: (\d+\.\d+) seconds", log_content)
        if match:
            print(match.group(1) + " seconds")
            return match.group(1) + " seconds"

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test