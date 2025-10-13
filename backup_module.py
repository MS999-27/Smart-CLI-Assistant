import os
import shutil
from datetime import datetime

def backup_folder(source_folder, backup_root="backups"):
    if not os.path.exists(source_folder):
        print("[ERROR] Source folder not found!")
        return
    os.makedirs(backup_root, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = f"{backup_root}/backup_{timestamp}"
    shutil.copytree(source_folder, backup_folder_name)
    print(f"[SUCCESS] Backup created at: {backup_folder_name}")
if __name__ == "__main__":
    backup_folder("data_to_backup")
