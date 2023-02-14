import argparse
from pathlib import Path

import preprocess  # import entire file preprocess.py
from settings import logger, settings  # this imports objects from the settings.py


def main(file: Path) -> None:
    if not file.exists():
        logger.error(f"File {filename} not found")
        raise FileNotFoundError
    preprocess.clean_file(filename, settings)


if __name__ == "__main__":
    
    # Get the file argument from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path, help="Source file (.parq)")
    args = parser.parse_args()

    filename = settings.datadir / args.file
    main(file=filename)
