from pathlib import Path


def path(file_name):
    return str(
        Path(__file__).parent.parent / 'tests' / 'resources' / file_name
    )
