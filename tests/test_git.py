import os
import subprocess
import shutil
import time

# Git clone test implementation
def test_git_clone(storage_path):
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

# Git status test implementation
def test_git_status(storage_path):
    repo_dir_name = "DeepLearningExamples"
    repo_path = os.path.join(storage_path, repo_dir_name)

    # Check if the repository directory exists
    if not os.path.isdir(repo_path):
        return "Error: Repository not found. Please run git-clone test first."

    start_time = time.time()
    result = subprocess.run(["git", "-C", repo_path, "status"], capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    return f"Git Status Result: {result.stdout}\nTime taken: {elapsed_time:.2f} seconds"


# Delete a git repository test
def test_remove_repo(storage_path):
    repo_dir_name = "DeepLearningExamples"
    repo_path = os.path.join(storage_path, repo_dir_name)

    # Check if the repository directory exists
    if not os.path.isdir(repo_path):
        return "Error: Repository not found. Nothing to remove."

    start_time = time.time()
    shutil.rmtree(repo_path)
    elapsed_time = time.time() - start_time

    return f"Repository removal completed.\nTime taken: {elapsed_time:.2f} seconds"