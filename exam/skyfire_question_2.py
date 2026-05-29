'''
Write a script to remove client files that are more than 90 days old, based on the naming conventions above. Feel free to use any programming language you would like.
This script is going to be running in production on mission-critical files that aren't easy to restore, so make sure to build in some debugging capabilities for your teammates, including Future You™!
'''


#!/usr/bin/env python3

# Reference
# https://stackoverflow.com/questions/7728694/python-regex-how-to-extract-date-from-filename-using-regular-expression
# https://stackoverflow.com/questions/3743222/how-do-i-convert-a-datetime-to-date

from datetime import datetime, timedelta, date
from pathlib import Path
import logging
import os, sys, re
import argparse

def parse_args():
    # Example: python3 test.py --dir ./uploads --days 90 --recursive --dry-run --verbose
    # Example: python3 test.py --dir ./uploads --days 90 --recursive
    parser = argparse.ArgumentParser(description="Parse argument")
    parser.add_argument("--dir", required=True, help="Target directory")
    parser.add_argument("--days", type=int, required=True, help="Delete files older than N days")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be deleted without deleting")
    parser.add_argument("--recursive", action="store_true", help="Traverse directories recursively")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()

def setup_logging(verbose: bool):
    if verbose: 
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("script.log"),
            logging.StreamHandler(sys.stdout),
        ],
    )

def get_files(directory: Path, recursive: bool):
    if recursive:
        return directory.rglob("*")
    else:
        return directory.glob("*")

def is_older_than(file_path: Path, cutoff_time: datetime) -> bool:
    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
    return mtime.date() < cutoff_time

def collect_old_files(directory: Path, days: int, recursive: bool):
    logging.debug(f"Directory: {directory}")
    cutoff_time = date.fromisoformat('2024-05-15') - timedelta(days=days)
    logging.debug(f"Cutoff time: {cutoff_time}")
    old_files = []
    for path in get_files(directory, recursive):
        print(path)
        if path.is_file():
            if is_older_than(path, cutoff_time):
                logging.debug(f"File to be deleted: {path}")
                old_files.append(path)

    return old_files

def delete_files(files, dry_run: bool):
    for file_path in files:
        try:
            if dry_run:
                logging.info(f"[DRY RUN] Would delete: {file_path}")
            else:
                file_path.unlink()
                logging.info(f"Deleted: {file_path}")
        except Exception as e:
            logging.error(f"Failed to delete {file_path}: {e}")

def main():
    args = parse_args()
    setup_logging(args.verbose)

    logging.info("Starting script")

    old_files = collect_old_files(
        directory=Path(args.dir),
        days=args.days,
        recursive=args.recursive,
    )
    logging.info(f"Found {len(old_files)} files older than {args.days} days")

    deleted_count = delete_files(old_files, args.dry_run)
    if not args.dry_run:
        logging.info(f"Deleted {deleted_count} files")
        
    logging.info("End script")

if __name__ == "__main__":
    main()

0 2 * * * /usr/bin/python3 python3 test.py --dir /home/data/uploads --days 90 --recursive --verbose


'''
What we liked
- We liked that the shape of your scripts looked good overall. It looked like you were going to find the right files and then remove them.
- We also liked that you set up the crontab correctly to execute the script nightly at 2:00 AM.
- We appreciated that you used multiple functions and added a usage statement.

Potential areas for improvement
- We liked solutions that redirected one or more of the output streams in the crontab (stdout or stderr) to a log file to be able to inspect the results of the script after it ran.
- We don't have additional feedback for you on potential improvements because your work accomplished many of the things we check for.
'''