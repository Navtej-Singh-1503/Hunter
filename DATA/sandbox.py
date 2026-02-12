'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

13/02/2026

version - 1.2.1

mail - navtejsingh15032011@gmail.com

'''

import subprocess
import tempfile
import shutil
import os
import time

TIMEOUT = 5  # seconds


def run_in_sandbox(file_path):
    temp_dir = tempfile.mkdtemp(prefix="av_sandbox_")

    report = {
        "stdout": "",
        "stderr": "",
        "timeout": False,
        "created_files": [],
    }

    try:
        sandbox_file = os.path.join(temp_dir, os.path.basename(file_path))
        shutil.copy(file_path, sandbox_file)

        before = set(os.listdir(temp_dir))

        proc = subprocess.Popen(
            ["python3", sandbox_file],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        try:
            out, err = proc.communicate(timeout=TIMEOUT)
            report["stdout"] = out
            report["stderr"] = err
        except subprocess.TimeoutExpired:
            proc.kill()
            report["timeout"] = True

        after = set(os.listdir(temp_dir))
        report["created_files"] = list(after - before)

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    return report

