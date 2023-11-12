import os
import subprocess
import time

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
