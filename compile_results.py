import os
import csv
import sys

from tests.test_git import parse_git_clone, parse_git_status, parse_remove_repo
from tests.test_unzip import parse_unzip
from tests.test_dd import parse_dd
from tests.test_fio import parse_fio_write_throughput, parse_fio_write_iops, parse_fio_read_throughput, parse_fio_read_iops
from tests.test_ml import parse_ssd

# List of available test modules
available_tests = {
    'fio_write_throughput': parse_fio_write_throughput,
    'fio_write_iops': parse_fio_write_iops,
    'fio_read_throughput': parse_fio_read_throughput,
    'fio_read_iops': parse_fio_read_iops,
    'git_clone': parse_git_clone,
    'git_status': parse_git_status,
    'remove_repo': parse_remove_repo,
    'unzip': parse_unzip,
    'dd': parse_dd,
    'ssd': parse_ssd,
    # Add other tests as needed
}

def process_logs(log_folder_path):
    metrics = {}

    for file in os.listdir(log_folder_path):
        if file.endswith(".txt"):
            log_file_path = os.path.join(log_folder_path, file)
            test_name = file.split('-')[0]  # Extract test name from filename

            if test_name in available_tests:
                metric = available_tests[test_name](log_file_path)

                if test_name not in metrics:
                    metrics[test_name] = []
                metrics[test_name].append(metric)
            else:
                print(f"No parser available for test: {test_name}")

    return metrics

def write_to_csv(metrics, output_file_path):
    with open(output_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(metrics.keys())  # Write the header
        # Assuming each test has the same number of entries
        for i in range(len(next(iter(metrics.values())))):
            row = [metrics[test][i] for test in metrics]
            csvwriter.writerow(row)

def main():
    if len(sys.argv) < 2:
        print("Usage: python compile_results.py <log_folder_path> [output_file_path]")
        sys.exit(1)

    log_folder_path = sys.argv[1]
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else "results.csv"


    metrics = process_logs(log_folder_path)
    write_to_csv(metrics, output_file_path)
    print(f"Metrics extracted to {output_file_path}")

if __name__ == "__main__":
    main()
