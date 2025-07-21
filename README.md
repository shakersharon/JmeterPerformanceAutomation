# JMeter Python Performance Test

## Overview
Performance testing project using JMeter and Python to simulate user actions like login, browsing, and checkout.

## Folder Structure
```
jmeter/        -> Contains .jmx test plans
results/       -> Raw .jtl result files
reports/       -> Generated HTML reports
tests/         -> Python scripts to run JMeter tests
```

## Setup
1. Install [Apache JMeter](https://jmeter.apache.org/)
2. Clone this repo
3. Update JMeter path in `tests/*.py`

## Run All Tests
```bash
python run_all_tests.py
```

## Individual Tests
```bash
python tests/run_baseline.py
python tests/run_load.py
python tests/run_spike.py
python tests/run_soak.py
```

Reports will be generated in `reports/`.
