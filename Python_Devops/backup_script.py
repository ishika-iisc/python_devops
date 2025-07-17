import sys
import shutil

if len(sys.argv) != 3:
    print(" usage:: python backup_script.py <source> <destination>")
    sys.exit(1)

src = sys.argv[1]
dest = sys.argv[2]

try : 
    shutil.copy(src,dest)
    print(f" backup completed from {src} to {dest}")
except FileNotFoundError:
    print("file not found, backup failed")
    sys.exit(2)