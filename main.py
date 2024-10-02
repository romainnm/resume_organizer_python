from config import DOWNLOAD_DIR, COVER_LETTER_DIR, RESUME_DIR
from utils import create_folder, move_file

CATEGORY_DIRS = {
    'resume': RESUME_DIR,
    'cover-letter': COVER_LETTER_DIR
}

for file in DOWNLOAD_DIR.iterdir():
    if file.is_file():
        file_stem = file.stem
        file_split = file_stem.split("_")
        
        if len(file_split) == 3:
            year, folder_category, company = file_split

            if folder_category in CATEGORY_DIRS:
                destination_dir = CATEGORY_DIRS[folder_category] / year / company
                new_name = f"Romain_Nim_{folder_category}{file.suffix}"
                create_folder(destination_dir)
                move_file(file, destination_dir, new_name)
        else:
            print(f"Skipping file with unexpected format: {file.name}")
