#!/usr/bin/python3

import time
import logging

from datetime import datetime
from hashlib import sha1, md5


class TimeHasher():
    """Get hash of current time."""

    hash_algorithms = {'sha1': sha1,
                       'md5': md5}

    def __init__(self, settings: dict) -> None:
        self.settings = settings

    def __init_settings__(self, settings: dict) -> None:
        pass

    def HashDatetime(self, d: datetime) -> str:
        date_str = "{:%Y-%m-%dT%H:%M:%S}".format(d)
        input = date_str.encode(self.settings['string_encoding'])

        logging.debug("Creating {}-hash of input {}".format(
                self.settings['hash_algorithm'],
                date_str))

        # Since repeated update()-calls sums the input data together,
        # we need to create new hasher every time we run the function.
        self.hasher = self.hash_algorithms[self.settings['hash_algorithm']]()
        self.hasher.update(input)

        return self.hasher.hexdigest()

    def Sleep(self) -> None:
        time.sleep(self.settings['sleep_time'])

    def Run(self) -> None:
        self.HashNow(datetime.now())
        self.Sleep()


if __name__ == "__main__":
    pass
