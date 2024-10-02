import shutil
from pathlib import Path

def create_folder(destination: Path) -> None:
    """
    Create a directory and all parent directories if they do not exist.

    Args:
        destination (Path): The directory path to create.
    """
    destination.mkdir(parents=True, exist_ok=True)

def move_file(source_file: Path, destination_dir: Path, new_name: str = None) -> None:
    """
    Move a file to the specified directory.

    Args:
        source_file (Path): The file to move.
        destination_dir (Path): The directory to move the file into.
        new_name (str, optional): The new name for the file. Defaults to None.
    """
    try:
        destination_file = destination_dir / (new_name if new_name else source_file.name)
        shutil.move(str(source_file), str(destination_file))
    except Exception as e:
        print(f"Error moving file {source_file.name}: {e}")
