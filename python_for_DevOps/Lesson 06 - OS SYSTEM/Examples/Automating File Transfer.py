import os
import shutil

def transfer_files(src_dir, dst_dir):
    for file in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(dst_dir, file)
        shutil.copy2(src_file, dst_file)

# Example usage:
src_dir = "/path/to/source/dir"
dst_dir = "/path/to/destination/dir"
transfer_files(src_dir, dst_dir)