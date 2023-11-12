import os
from datetime import datetime
import subprocess
import time

# Git status test implementation
def git_status_test(storage_path):
    repo_dir_name = "DeepLearningExamples"
    repo_path = os.path.join(storage_path, repo_dir_name)

    # Check if the repository directory exists
    if not os.path.isdir(repo_path):
        return "Error: Repository not found. Please run git-clone test first."

    start_time = time.time()
    result = subprocess.run(["git", "-C", repo_path, "status"], capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    return f"Git Status Result: {result.stdout}\nTime taken: {elapsed_time:.2f} seconds"