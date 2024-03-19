import os
import subprocess
from typing import List
import config

from my_types import Directory

config = config.Config()


def main():
    directories = config.get_directories()
    for directory in directories:
        add_watchman_trigger(directory)


def get_directory_excludes(directory: Directory) -> str:
    exclude_list = directory.get("excludeList")
    exclude_list.append(".git")
    exclude_list = list(set(exclude_list))
    return " ".join(f"--exclude={i}" for i in directory["excludeList"])


def create_watchman_trigger_command(directory: Directory) -> str:
    if not os.path.exists("scripts"):
        os.makedirs("scripts")
    name = f"scripts/{directory['name']}.sh"
    command = f"rsync -rlptzv --rsh='ssh -p 20384' {get_directory_excludes(directory)} {directory['localPath']} {directory['remotePath']}"
    with open(name, "w") as f:
        f.write(command)
    return os.path.abspath(name)


def get_pattern(directory: Directory) -> List[str]:
    if not "pattern" in directory or len(directory["pattern"]) == 0:
        return ["**/*"]
    return directory["pattern"]


def add_watchman_trigger(directory: Directory):
    command_file = create_watchman_trigger_command(directory)
    subprocess.run(["watchman", "watch-del", directory["localPath"]])
    subprocess.run(["watchman", "watch", directory["localPath"]])
    subprocess.run(
        ["watchman", "trigger-del", directory["localPath"], directory["name"]]
    )
    subprocess.run(
        [
            "watchman",
            "--",
            "trigger",
            directory["localPath"],
            directory["name"],
            *get_pattern(directory),
            "--",
            "bash",
            command_file,
        ]
    )


if __name__ == "__main__":
    main()
