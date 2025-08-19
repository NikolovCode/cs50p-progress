import os
import subprocess
from datetime import datetime
import shutil

# Път до CS50 папката
CS50_FOLDER = r"D:\Niki\Programming CS50\CS50P"

# Локален clone на публичното GitHub repo
PUBLIC_REPO_FOLDER = r"D:\Niki\GitHub\cs50p-progress"

# GitHub URL на repo-то
PUBLIC_REPO_URL = "https://github.com/NikolovCode/cs50p-progress.git"


def run(cmd, cwd=None):
    """Изпълнява shell команда."""
    subprocess.run(cmd, cwd=cwd, shell=True, check=True)


def sync_files():
    if not os.path.exists(PUBLIC_REPO_FOLDER):
        run(f"git clone {PUBLIC_REPO_URL} {PUBLIC_REPO_FOLDER}")

    for item in os.listdir(CS50_FOLDER):
        if item in [".git", "__pycache__"]:  # ⬅️ игнорирай тези
            continue

        s = os.path.join(CS50_FOLDER, item)
        d = os.path.join(PUBLIC_REPO_FOLDER, item)

        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)


def commit_and_push():
    run("git add .", cwd=PUBLIC_REPO_FOLDER)
    msg = f"CS50 update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run(f'git commit -m "{msg}"', cwd=PUBLIC_REPO_FOLDER)
    run("git push origin main", cwd=PUBLIC_REPO_FOLDER)


if __name__ == "__main__":
    sync_files()
    try:
        commit_and_push()
        print("✅ Синхронизирано успешно!")
    except subprocess.CalledProcessError:
        print("⚠️ Няма нови промени за commit.")