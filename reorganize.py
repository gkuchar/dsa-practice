# GitHub Actions script to reroute NeetCode.io auto commits into the directory structure:
# src/{topic}/{problem}/{problem}_{submission number}.py

import subprocess
import sys
import os
import shutil
from problem_topic_map import PROBLEM_TO_TOPIC


def get_changed_file():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().split('\n')

def assemble_path(diff):
    dirs = diff.split('/')

    raw_problem = dirs[1]
    topic = PROBLEM_TO_TOPIC.get(raw_problem, 'uncategorized')
    problem = raw_problem.replace('-', '_')

    submission_number = dirs[2].split('-')[1].split('.')[0]

    os.makedirs(f'src/{topic}/{problem}', exist_ok=True) # create problem directory if non-existent

    new_path = f'src/{topic}/{problem}/{problem}_{submission_number}.py'

    return new_path

def main():
    original_paths = get_changed_file()

    for path in original_paths:
        dirs = path.split('/')
        if dirs[0] != "Data Structures & Algorithms":
            continue
        if not os.path.exists(path):
            continue
        new_path = assemble_path(path)

        shutil.copy(path, new_path)
        os.remove(path)

if __name__ == "__main__":
    main()