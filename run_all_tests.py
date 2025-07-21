import subprocess

subprocess.run(["python", "tests/run_baseline.py"])
subprocess.run(["python", "tests/run_load.py"])
subprocess.run(["python", "tests/run_spike.py"])
subprocess.run(["python", "tests/run_soak.py"])