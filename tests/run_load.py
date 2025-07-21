import subprocess
import os
import shutil

# Absolute path to jmeter.bat
JMETER_PATH = r"C:\\apache-jmeter-5.6.3\\apache-jmeter-5.6.3\\bin\\jmeter.bat"

# Define paths relative to current script
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
jmx_file = os.path.join(base_dir, "jmeter", "load_test.jmx")
results_file = os.path.join(base_dir, "results", "load_test.jtl")
log_file = os.path.join(base_dir, "results", "load_test.log")
report_dir = os.path.join(base_dir, "reports", "load")

# Cleanup previous run
if os.path.exists(results_file):
    os.remove(results_file)

if os.path.exists(report_dir):
    shutil.rmtree(report_dir)

# Run JMeter
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
    print(f"[ERROR] JMX file not found: {jmx_file}")
