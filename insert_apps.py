""" This script inserts the data from the apps.tsv file into the app table in the database.

The script provides functionality to import app data from a file and insert it 
into a SQLite database. It takes an optional file path and separator as arguments, 
which allow customization of the input file and field separator.

If no arguments are provided, the default values from the config.py file will be used.

Usage: python insert_apps.py <file> <separator>
file: The path to the file containing the app data.
separator: The separator used to separate the fields in the file.

Example usage:
- python insert_apps.py
- python insert_apps.py apps.tsv ","
- python insert_apps.py /path/to/apps.tsv ";"

Note: The script requires the config.py file to be present in the same directory, 
      which contains the necessary configuration values.

"""

import sys
import sqlite3
import config
from app import database


def import_apps(file_path: str = config.APPS_PATH,
                 separator: str = config.CSV_GAMES_SEPARATOR
                 ) -> None:
    """
    Imports app data from a file and inserts it into a SQLite database.

    Args:
        file_path (str): The path to the file containing the app data.
        separator (str): The separator used to separate the fields in the file.

    Returns:
        None
    """
    db = database.Database()

    with open(file_path, "r", encoding="utf-8") as f:
        print(f.readline())
        for line in f:
            line = line.replace("\n", "")
            data = line.strip().split(separator)
            print(data)
            if len(data) != config.NUMBER_GAME_COLUMNS:
                for _ in range(len(data), config.NUMBER_GAME_COLUMNS):
                    data.append(None)
            try:
                db.insert_app(data)
            except sqlite3.Error as e:
                print(f"Error {e}: for {line}")
        db.close()

def display_help() -> None:
    """
    Displays the help message for the script.

    Returns:
        None
    """
    print("""This script inserts the data from the apps.tsv file into the apps table
          in the database.""")
    print()
    print("Usage: python insert_apps.py <file> <separator>")
    print("file: The path to the file containing the app data.")
    print("separator: The separator used to separate the fields in the file.")
    print()
    print("If no arguments are provided, the default values from the config.py file will be used.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        display_help()
    elif len(sys.argv) == 1:
        import_apps()
    elif len(sys.argv) == 3:
        import_apps(sys.argv[1], sys.argv[2])
    elif len(sys.argv) != 3:
        print("Usage: python insert_apps.py <file> <separator>")
        sys.exit(1)
    sys.exit(0)
