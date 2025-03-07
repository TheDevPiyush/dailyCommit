import os
from datetime import datetime

file_path = "log.txt"

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

with open(file_path, "a") as file:
    file.write(f"Commit on {timestamp}\n")

os.system("git add .")
os.system(f'git commit -m "Daily commit on {timestamp}"')
os.system("git push origin main")