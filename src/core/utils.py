from pathlib import Path



def get_root_path() -> Path:
    """Get the root path of the project.

    Returns:
        The root path as a Path object.
    """
    return Path(__file__).parent.parent.parent

