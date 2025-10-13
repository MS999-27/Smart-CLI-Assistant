import os
import platform
import shutil

def system_info():
    print("\n🔹 SYSTEM INFORMATION 🔹")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"User: {os.getlogin()}")

def organize_files(target_folder):
    print(f"\n📁 Organizing files in: {target_folder}")
    if not os.path.exists(target_folder):
        print("Folder not found!")
        return
    file_types = {
        'Images': ['.png', '.jpg', '.jpeg', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Others': []
    }
    for file in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(file.endswith(ext) for ext in extensions):
                    dest = os.path.join(target_folder, folder)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest, file))
                    moved = True
                    break
            if not moved:
                dest = os.path.join(target_folder, 'Others')
                os.makedirs(dest, exist_ok=True)
                shutil.move(file_path, os.path.join(dest, file))
    print("✅ Files organized successfully!")
