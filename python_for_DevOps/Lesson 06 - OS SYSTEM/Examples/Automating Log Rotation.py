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


# Explaintion:
# This code is used to rotate logs in a directory. It sorts the logs by their last modified
# time and then moves the oldest logs to a new file with a timestamp in the filename. This
# is useful for keeping a certain number of recent logs in the directory and removing older
# logs to prevent the directory from becoming too large.
# The function takes two parameters: log_dir (the directory where the logs are located) and
# max_files (the maximum number of log files to keep in the directory).
