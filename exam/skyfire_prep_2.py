#!/usr/bin/env python3

from datetime import datetime, timedelta
from pathlib import Path
import logging
import os, sys
import argparse

def parse_args():
    # Example: python3 skyfire_prep_2.py --dir /tmp/logs --days 7 --recursive --dry-run
    # Example: python3 skyfire_prep_2.py --dir /tmp/log --days 7 --recursive --dry-run
    # Example: python3 skyfire_prep_2.py --dir /tmp/logs --days 7 --recursive 
    # Example: python3 skyfire_prep_2.py --dir /tmp/logs --days 7 --verbose
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

def validate_directory(directory: str) -> Path:
    path = Path(directory)
    if not path.exists():
        logging.error(f"Directory does not exist: {directory}")
        sys.exit(1)
    if not path.is_dir():
        logging.error(f"Path is not a directory: {directory}")
        sys.exit(1)
    return path

def get_files(directory: Path, recursive: bool):
    if recursive:
        return directory.rglob("*")
    else:
        return directory.glob("*")
    
def is_older_than(file_path: Path, cutoff_time: datetime) -> bool:
    try:
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        return mtime < cutoff_time
    except Exception as e:
        logging.warning(f"Could not read file metadata: {file_path} ({e})")
        return False

def collect_old_files(directory: Path, days: int, recursive: bool):
    cutoff_time = datetime.now() - timedelta(days=days)
    logging.debug(f"Cutoff time: {cutoff_time}")
    old_files = []
    for path in get_files(directory, recursive):
        if path.is_file():
            if is_older_than(path, cutoff_time):
                old_files.append(path)

    return old_files

def should_delete(file_path, cutoff_time):
    if dry_run:
        print(f"[DRY RUN] Would delete {file}")
    else:
        os.remove(file)

def delete_files(files, dry_run: bool):
    deleted_count = 0

    for file_path in files:
        try:
            if dry_run:
                logging.info(f"[DRY RUN] Would delete: {file_path}")
            else:
                file_path.unlink()
                logging.info(f"Deleted: {file_path}")
                deleted_count += 1
        except PermissionError:
            logging.error(f"Permission denied: {file_path}")
        except Exception as e:
            logging.error(f"Failed to delete {file_path}: {e}")

    return deleted_count

def get_time():
    # cutoff = datetime.now() - timedelta(days=days)
    # return cutoff
    pass

def main():
    args = parse_args()
    setup_logging(args.verbose)

    logging.info("Starting script")

    directory = validate_directory(args.dir)

    files = get_files(Path(args.dir), False)
    logging.info(f"files: {files}")

    files_recursive = get_files(Path(args.dir), True)
    logging.info(f"files: {files_recursive}")

    old_files = collect_old_files(
        directory=directory,
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