from dataclasses import dataclass
from typing import List, TypedDict


@dataclass
class Directory(TypedDict):
    name: str
    localPath: str
    remotePath: str
    excludeList: List[str]
    pattern: List[str]


@dataclass
class IConfig(TypedDict):
    directories: List[Directory]
