# storage-benchmark

## Installation

```
sudo usermod -aG docker ${USER} && \
newgrp docker

sudo apt-get -y install fio

git clone https://github.com/LambdaLabsML/storage-benchmark.git && \
cd storage-benchmark
```


## Usage

Setup storage path for the test

```
export STORAGE_PATH=/home/ubuntu/scratch
```

Benchmark

```

python benchmark.py ${STORAGE_PATH}
```


Collect results

```
python compile_results.py ${STORAGE_PATH}/log/ results_home.csv
```


## Results
[Here](./results/results_home.csv) is a reference result for a local storage.

