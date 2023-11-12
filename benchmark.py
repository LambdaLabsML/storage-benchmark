import sys
import os
from datetime import datetime

# Import test functions
from tests.git_clone_test import git_clone_test
from tests.git_status_test import git_status_test
from tests.remove_repo_test import remove_repo_test

# List of available test modules
available_tests = {
    'git-clone': git_clone_test,
    'git-status': git_status_test,
    'remove-repo': remove_repo_test,
    # Add other tests as needed
}

def run_test(test_name, storage_path):
    result = available_tests[test_name](storage_path)
    log_file_name = f"{test_name}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
    log_path = os.path.join(storage_path, 'log', log_file_name)

    # Ensure log directory exists
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    with open(log_path, 'w') as file:
        file.write(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python benchmark.py <storage_path> [test_name]")
        sys.exit(1)

    storage_path = sys.argv[1]
    test_name = sys.argv[2] if len(sys.argv) > 2 else None

    os.makedirs(os.path.dirname(storage_path + "/log"), exist_ok=True)

    if test_name:
        if test_name in available_tests:
            run_test(test_name, storage_path)
        else:
            print(f"Test '{test_name}' is not available.")
    else:
        for test in available_tests:
            run_test(test, storage_path)

if __name__ == "__main__":
    main()
