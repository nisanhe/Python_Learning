import os
import time
import shutil

def rotate_logs(log_dir, max_files):
    log_files = os.listdir(log_dir)
    log_files.sort(key=lambda x: os.path.getmtime(os.path.join(log_dir, x)))

    if len(log_files) > max_files:
        for file in log_files[:-max_files]:
            old_file = os.path.join(log_dir, file)
            new_file = os.path.join(log_dir, f"{file}.{int(time.time())}")
            shutil.move(old_file, new_file)