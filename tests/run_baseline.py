import subprocess
import os
import shutil

# Path to JMeter
JMETER_PATH = r"C:\apache-jmeter-5.6.3\apache-jmeter-5.6.3\bin\jmeter.bat"

# Base project directory
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define file paths
jmx_file = os.path.join(base_dir, "jmeter", "baseline_test.jmx")
results_file = os.path.join(base_dir, "results", "baseline.jtl")
log_file = os.path.join(base_dir, "results", "baseline.log")
report_dir = os.path.join(base_dir, "reports", "baseline")

# Clean up old files/directories if they exist
if os.path.exists(results_file):
    os.remove(results_file)

if os.path.exists(log_file):
    os.remove(log_file)

if os.path.exists(report_dir):
    shutil.rmtree(report_dir)

# Run JMeter if the test plan exists
if os.path.exists(jmx_file):
    subprocess.run([
        JMETER_PATH,
        "-n",
        "-t", jmx_file,
        "-l", results_file,
        "-j", log_file,
        "-e",
        "-o", report_dir
    ])
else:
    print(f"[ERROR] Baseline test plan not found: {jmx_file}")
