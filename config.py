from pathlib import Path
import yaml


class Config:

    def __init__(self, filename="config.yaml"):

        with open(filename, "r", encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)

    @property
    def download(self):
        return self.cfg["download"]

    @property
    def checker(self):
        return self.cfg["checker"]

    @property
    def report(self):
        return self.cfg["report"]

    @property
    def logging(self):
        return self.cfg["logging"]


config = Config()
