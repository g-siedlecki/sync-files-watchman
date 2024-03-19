import argparse
import json
from typing import List

from my_types import Directory, IConfig


class Config:
    def __init__(self):
        self._config_name = "config.json"
        self.config: IConfig = self.get_config()
        self._parser = self._create_parser()

    def get_config(self):
        with open(self._config_name, "r") as f:
            return json.load(f)

    def get_directories(self) -> List[Directory]:
        return self.config.get("directories")

    def get_arguments(self):
        args = self._parser.parse_args()
        return {
            "deleteAll": args.deleteall,
            "delete": args.delete,
        }

    def _create_parser(self):
        parser = argparse.ArgumentParser(description="Sync files using watchman")
        parser.add_argument(
            "-da",
            "--deleteall",
            action="store_true",
            help="Delete all watchman triggers",
        )
        parser.add_argument(
            "-d",
            "--delete",
            action="store",
            help="Delete watchman trigger by name",
        )

        return parser
