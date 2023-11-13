import os
import subprocess
import time
import re

def test_fio_write_throughput(storage_path):
    fio_dir = os.path.join(storage_path, "fiotest")
    os.makedirs(fio_dir, exist_ok=True)

    fio_command = [
        "sudo", "fio", "--name=write_throughput",
        f"--directory={fio_dir}",
        "--numjobs=8", "--size=10G", "--time_based", "--runtime=60s",
        "--ramp_time=2s", "--ioengine=libaio", "--direct=1", "--verify=0",
        "--bs=1M", "--iodepth=64", "--rw=write", "--group_reporting=1"
    ]

    start_time = time.time()
    result = subprocess.run(fio_command, capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    log_output = f"FIO Write Throughput Test Completed.\nElapsed Time: {elapsed_time:.2f} seconds\n{result.stdout}"

    return log_output


def parse_fio_write_throughput(log_file_path):
    print("parse_fio_write_throughput ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'fio_write_throughput' in log_file_path:
        match = re.search(r"WRITE: bw=(\d+(\.\d+)?(MiB|GiB)/s)", log_content)
        if match:
            print(match.group(1))
            return match.group(1)

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test


def test_fio_write_iops(storage_path):
    fio_dir = os.path.join(storage_path, "fiotest")
    os.makedirs(fio_dir, exist_ok=True)

    fio_command = [
        "sudo", "fio", "--name=write_iops",
        f"--directory={fio_dir}",
        "--size=10G", "--time_based", "--runtime=60s", "--ramp_time=2s",
        "--ioengine=libaio", "--direct=1", "--verify=0",
        "--bs=4K", "--iodepth=64", "--rw=randwrite", "--group_reporting=1"
    ]

    start_time = time.time()
    result = subprocess.run(fio_command, capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    log_output = f"FIO Write IOPS Test Completed.\nElapsed Time: {elapsed_time:.2f} seconds\n{result.stdout}"

    return log_output

def parse_fio_write_iops(log_file_path):
    print("parse_fio_write_iops ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'fio_write_iops' in log_file_path:
        match = re.search(r"WRITE: bw=(\d+(\.\d+)?(MiB|GiB)/s)", log_content)
        if match:
            print(match.group(1))
            return match.group(1)

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test

def test_fio_read_throughput(storage_path):
    fio_dir = os.path.join(storage_path, "fiotest")
    os.makedirs(fio_dir, exist_ok=True)

    fio_command = [
        "sudo", "fio", "--name=read_throughput",
        f"--directory={fio_dir}",
        "--numjobs=8", "--size=10G", "--time_based", "--runtime=60s",
        "--ramp_time=2s", "--ioengine=libaio", "--direct=1", "--verify=0",
        "--bs=1M", "--iodepth=64", "--rw=read", "--group_reporting=1"
    ]

    start_time = time.time()
    result = subprocess.run(fio_command, capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    log_output = f"FIO Read Throughput Test Completed.\nElapsed Time: {elapsed_time:.2f} seconds\n{result.stdout}"

    return log_output

def parse_fio_read_throughput(log_file_path):
    print("parse_fio_read_throughput ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'fio_read_throughput' in log_file_path:
        match = re.search(r"READ: bw=(\d+(\.\d+)?(MiB|GiB)/s)", log_content)
        if match:
            print(match.group(1))
            return match.group(1)

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test

def test_fio_read_iops(storage_path):
    fio_dir = os.path.join(storage_path, "fiotest")
    os.makedirs(fio_dir, exist_ok=True)

    fio_command = [
        "sudo", "fio", "--name=read_iops",
        f"--directory={fio_dir}",
        "--size=10G", "--time_based", "--runtime=60s", "--ramp_time=2s",
        "--ioengine=libaio", "--direct=1", "--verify=0",
        "--bs=4K", "--iodepth=64", "--rw=randread", "--group_reporting=1"
    ]

    start_time = time.time()
    result = subprocess.run(fio_command, capture_output=True, text=True)
    elapsed_time = time.time() - start_time

    log_output = f"FIO Read IOPS Test Completed.\nElapsed Time: {elapsed_time:.2f} seconds\n{result.stdout}"

    return log_output

def parse_fio_read_iops(log_file_path):
    print("parse_fio_read_iops ...")
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    if 'fio_read_iops' in log_file_path:
        match = re.search(r"READ: bw=(\d+(\.\d+)?(MiB|GiB)/s)", log_content)
        if match:
            print(match.group(1))
            return match.group(1)

    return "N/A"  # Return "N/A" if the metric can't be found or if it's an unhandled test