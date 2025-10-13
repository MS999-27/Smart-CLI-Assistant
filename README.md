This is the Smart CLI Assistant project
# Smart CLI Assistant (To-Do Manager)

**Author:** Mudita Songara

## 📜 Project Overview

This project is a simple, command-line interface (CLI) **To-Do Manager** developed in Python. It allows users to manage daily tasks directly from the terminal.

### Key Features
* **Task Management:** Provides basic CRUD (Create, Read, Update, Delete) functionality for tasks (Add, View, Delete, Clear All).
* **Persistence:** Tasks are automatically saved to `todo.txt` and reloaded upon restarting the application.
* **Action Logging (Unique Feature):** Every significant user action (Adding, Deleting, Viewing, Exiting) is recorded with a **timestamp** in the `activity.log` file for auditing.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your system.
* Git installed on your system.

### Installation and Setup

1. **Clone the Repository:**
```bash
git clone [https://github.com/MS999-27/Smart-CLI-Assistant.git](https://github.com/MS999-27/Smart-CLI-Assistant.git)
cd Smart-CLI-Assistant
```
2. **Make the script executable (Optional):**
```bash
chmod +x smart_cli_assistant.py
```

### How to Run

Execute the main Python script from the project directory:

```bash
python3 smart_cli_assistant.py
You will be presented with a menu (1-5) to interact with the To-Do Manager
```

### Project Files

File Name	& Description
smart_cli_assistant.py:	The core Python code containing the To-Do Manager logic and logging functions.
todo.txt:	Automatically created file where tasks are saved for persistence.
activity.log:	Automatically created file that records every user action with a timestamp.
README.md	: This documentation file.
CONTRIBUTION.md	: Documents individual student contributions to the project.
backups/:	Empty directory reserved for future backup functionality.

### 🔧 Workflow & Tools
Platform: macOS/Linux Terminal

Shell: zsh

Editor: nano

Version Control: Git & GitHub

### Screenshot of execution (To-Do Manager & logging)
<img width="1470" height="956" alt="Screenshot 2025-10-11 at 8 53 31 PM" src="https://github.com/user-attachments/assets/d2cd6b1c-76c2-49b3-95f1-482fad62a4d5" />
<img width="1470" height="956" alt="Screenshot 2025-10-11 at 8 53 39 PM" src="https://github.com/user-attachments/assets/c6f3a128-e678-47a0-8f1c-379871ad65ef" />
<img width="1470" height="956" alt="Screenshot 2025-10-11 at 8 53 46 PM" src="https://github.com/user-attachments/assets/baae27d0-c040-4b38-866f-a5f3f52ac712" />
<img width="1470" height="956" alt="Screenshot 2025-10-11 at 8 53 52 PM" src="https://github.com/user-attachments/assets/442d5455-3cf7-4964-8f2d-7e4810b42aa9" />
<img width="1470" height="956" alt="Screenshot 2025-10-11 at 8 53 55 PM" src="https://github.com/user-attachments/assets/f17c88f1-f1cf-4c67-88fe-a36516bf383c" />

## System Info + File Organizer Module

**Member 2:** Swarna Prakash
Branch: feature/sys-file

## Project Overview

This module is part of the Smart CLI Assistant project.
It helps users:
View important System Information (like OS, processor, username, etc.) 

Automatically Organize Files in a given folder based on their file type.

The purpose of this module is to make system management faster and reduce manual effort for organizing files.

## ⚙️ Features

Displays details such as:

Operating System

OS Version

Machine Architecture

Processor Info

Logged-in User

Organizes files into folders:
Images → .png, .jpg, .jpeg, .gif

Documents → .pdf, .docx, .txt

Videos → .mp4, .mov, .avi

Others → Remaining file types

Automatically creates folders if they don’t exist.

Works smoothly from the Linux terminal or VS Code terminal.

## Technologies Used

Language: Python

Platform: Linux / Windows

Tools: Git, GitHub, VS Code








