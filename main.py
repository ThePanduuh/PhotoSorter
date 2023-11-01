import glob
import os
import shutil
import sys

sort_file = sys.argv[1]
src_dir = os.path.dirname(sort_file)
dest_dir_jpg = os.path.join(src_dir, "JPG")
dest_dir_raw = os.path.join(src_dir, "RAW")
os.chdir(src_dir)

if not os.path.exists(dest_dir_jpg):
    os.mkdir(dest_dir_jpg)
if not os.path.exists(dest_dir_raw):
    os.mkdir(dest_dir_raw)

for file in glob.glob("*.jpg"):
    f_src_path = os.path.join(src_dir, file)
    f_dest_path_jpg = os.path.join(dest_dir_jpg, file)
    shutil.move(f_src_path, f_dest_path_jpg)
for file in glob.glob("*.raf"):
    f_src_path = os.path.join(src_dir, file)
    f_dest_path_raw = os.path.join(dest_dir_raw, file)
    shutil.move(f_src_path, f_dest_path_raw)
