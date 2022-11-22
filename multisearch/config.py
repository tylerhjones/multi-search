
from __future__ import annotations
import dataclasses
from dataclasses import dataclass
import os
import toml
import logging as log
from pathlib import Path

class ConfigException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

CONFIG_TYPE_TOML = 'toml'

def toml_loader(config: Config):
    with open(config.config_path, "r") as f:
        return toml.load(f)

def toml_saver(config: Config):
    with open(config.config_path, "w") as f:
        toml.dump(dataclasses.asdict(config), f)

DEFAULT_CONFIG_FILENAME = "config.toml"

DEFAULT_CONFIG_PATH = "~/.config/multi-search"



@dataclass
class Config:
    config_path: str = os.path.expanduser(f"{DEFAULT_CONFIG_PATH}/{DEFAULT_CONFIG_FILENAME}")


class ConfigFactory:
    def __init__(self) -> None:
        self.default_config = Config()

    def build_path(self)-> None:
      try:
        config_dir = os.path.expanduser(DEFAULT_CONFIG_PATH)
        log.debug(f"Creating config directory at {config_dir}")
        Path(config_dir).mkdir(parents=True, exist_ok=True)
      except Exception as e:
        raise ConfigException(
          f"Error creating config path {self.default_config.config_path}") from e

    def build(self) -> Config:
        if not os.path.exists(self.default_config.config_path):
            log.debug(f"Creating config file at {self.default_config.config_path}")
            self.build_path()
            toml_saver(self.default_config)
            return self.default_config
        else:
            log.debug(f"Loading config from {self.default_config.config_path}")
            return toml_loader(self.default_config)