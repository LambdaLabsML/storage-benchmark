import os
import time
import shutil


# Delete a git repository test
def remove_repo_test(storage_path):
    repo_dir_name = "DeepLearningExamples"
    repo_path = os.path.join(storage_path, repo_dir_name)

    # Check if the repository directory exists
    if not os.path.isdir(repo_path):
        return "Error: Repository not found. Nothing to remove."

    start_time = time.time()
    shutil.rmtree(repo_path)
    elapsed_time = time.time() - start_time

    return f"Repository removal completed.\nTime taken: {elapsed_time:.2f} seconds"