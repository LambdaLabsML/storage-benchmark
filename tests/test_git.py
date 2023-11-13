import os
import subprocess
import time
import re

# Git clone test implementation
def test_git_clone(storage_path):
    repo_url = "https://github.com/NVIDIA/DeepLearningExamples.git"
    repo_dir_name = "DeepLearningExamples"
    repo_path = os.path.join(storage_path, repo_dir_name)

    # Check if the repository already exists and delete it
    if os.path.isdir(repo_path):
        subprocess.run(["sudo", "rm", "-rf", repo_path], check=True)

    start_time = time.time()
    result = subprocess.run(["git", "-C", storage_path, "clone", repo_url], capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    return f"Git Clone Result: {result.stdout}\nTime taken: {elapsed_time:.2f} seconds"


def parse_git_clone(log_file_path):
    print("parse_git_clone ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'git_clone' in log_file_path:
        match = re.search(r"Time taken: (\d+\.\d+) seconds", log_content)
        if match:
            print(match.group(1) + " seconds")
            return match.group(1) + " seconds"

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test



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


def parse_git_status(log_file_path):
    print("parse_git_status ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'git_status' in log_file_path:
        match = re.search(r"Time taken: (\d+\.\d+) seconds", log_content)
        if match:
            print(match.group(1) + " seconds")
            return match.group(1) + " seconds"

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test


# Delete a git repository test
def test_remove_repo(storage_path):
    repo_dir_name = "DeepLearningExamples"
    repo_path = os.path.join(storage_path, repo_dir_name)

    # Check if the repository directory exists
    if not os.path.isdir(repo_path):
        return "Error: Repository not found. Nothing to remove."

    start_time = time.time()
    subprocess.run(["sudo", "rm", "-rf", repo_path], check=True)
    elapsed_time = time.time() - start_time

    return f"Repository removal completed.\nTime taken: {elapsed_time:.2f} seconds"

def parse_remove_repo(log_file_path):
    print("parse_remove_repo ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'remove_repo' in log_file_path:
        match = re.search(r"Time taken: (\d+\.\d+) seconds", log_content)
        if match:
            print(match.group(1) + " seconds")
            return match.group(1) + " seconds"

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test