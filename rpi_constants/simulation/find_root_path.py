"""
Helper function to find project root path given marker files.    
"""

from pathlib import Path

def find_root_path(marker_file: str) -> Path:
    """
    Attempts to find the path to the root of the project.

    Args:
        marker_files (str): The file attributed with belonging to the project root.

    Raises:
        ValueError: If the supplied `marker_files` are empty, it's impossible to discern when we arrive at the root.
        FileNotFoundError: If the root folder was unable to be found.

    Returns:
        Path: The `Path` instance detailing the path to the project root.
    """
    if len(marker_file) == 0:
        raise ValueError("Attempting to find root of project without any marker files; impossible.")
    
    current_path = Path(__file__).resolve()
    for parent in [current_path] + list(current_path.parents):
        if Path(parent, marker_file).exists():
            return parent
            
    raise FileNotFoundError("Unable to find root folder path. Check marker files supplied.")
