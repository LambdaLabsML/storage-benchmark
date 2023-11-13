import os
import subprocess
import time
import re

def test_ssd(storage_path):
    # Modify the user group to include docker (might require a password)
    subprocess.run(["sudo", "usermod", "-aG", "docker", os.getenv("USER")])

    # Change to the storage directory
    os.chdir(storage_path)

    # Download the Makefile
    subprocess.run(["wget", "https://raw.githubusercontent.com/lambdal/deeplearning-benchmark/master/pytorch/Makefile"])

    # Run make install
    subprocess.run(["make", "install", f"PATH_STORAGE={storage_path}"])

    # Run make create_data
    data_dir = os.path.join(storage_path, "data", "object_detection")
    # Check if the data/object_detection subfolder exists
    if not os.path.exists(data_dir):
        # If not, run make create_data
        subprocess.run(["make", "create_data", f"PATH_STORAGE={storage_path}"])

    # Run make benchmark and capture output
    start_time = time.time()
    result = subprocess.run(["make", "benchmark", f"PATH_STORAGE={storage_path}"], capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    log_output = f"SSD Benchmark Test Completed.\nElapsed Time: {elapsed_time:.2f} seconds\n{result.stdout}"

    return log_output


def parse_ssd(log_file_path):
    print("parse_ssd ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'ssd' in log_file_path:
        match = re.search(r"Training performance = (\d+\.\d+) FPS", log_content)
        if match:
            print(match.group(1) + " FPS")
            return match.group(1) + " FPS"

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test