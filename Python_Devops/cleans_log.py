import os
import shutil

log_dir = "demo_logs"
if os.path.exists(log_dir):
    shutil.rmtree(log_dir)
    print("logs cleaned before deployment")
else:
    print("No logs to clear")