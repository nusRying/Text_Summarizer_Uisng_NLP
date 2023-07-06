import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "text_Summarizer"
list_Files = [
    ".github/workflow/.gitkeep",   # for commenting on GitHub
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for file_path in list_Files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w"):
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists.")
