# Resume Organizer

Resume Organizer is a Python script that automates the organization of your resume and cover letter files. It moves files from your downloads directory to designated folders based on the file name, categorizing them by year, document type, and company.

## Features

- **Automated File Organization**: Moves resume and cover letter files to specified directories.
- **Dynamic Folder Creation**: Creates year and company subfolders as needed.
- **File Renaming**: Optionally renames files according to a standardized format.

## Configuration (config.py)

The `config.py` file is used to store directory paths and user-specific information. 

To use the project, you must create a `config.py` file in the root of the project with the following content:

```python
from pathlib import Path
DOWNLOAD_DIR = Path(absolute path)
COVER_LETTER_DIR = Path(absolute path)
RESUME_DIR = Path(absolute path)
OWNER_NAME = "YourName_"

