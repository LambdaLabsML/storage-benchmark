import os
import subprocess
import time

def test_unzip(storage_path):
    zip_url = "http://images.cocodataset.org/zips/train2017.zip"
    zip_file_name = "train2017.zip"
    zip_file_path = os.path.join(storage_path, zip_file_name)

    # Check if the zip file already exists
    if not os.path.isfile(zip_file_path):
        # Change to the storage directory
        os.chdir(storage_path)

        # Download the zip file
        subprocess.run(["curl", "-O", zip_url])
    else:
        print(f"{zip_file_name} already exists. Skipping download.")

    # Measure the time taken to unzip the file
    start_time = time.time()
    subprocess.run(["unzip", "-o", zip_file_path])  # '-o' to overwrite files without prompting
    elapsed_time = time.time() - start_time

    return f"Unzip operation completed.\nElapsed Time: {elapsed_time:.2f} seconds"
