import os
import subprocess
import shutil
import time

# Git clone test implementation
def git_clone_test(storage_path):
    repo_url = "https://github.com/NVIDIA/DeepLearningExamples.git"
    repo_dir_name = "DeepLearningExamples"
    repo_path = os.path.join(storage_path, repo_dir_name)

    # Check if the repository already exists and delete it
    if os.path.isdir(repo_path):
        shutil.rmtree(repo_path)

    start_time = time.time()
    result = subprocess.run(["git", "-C", storage_path, "clone", repo_url], capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    return f"Git Clone Result: {result.stdout}\nTime taken: {elapsed_time:.2f} seconds"
