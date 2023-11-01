#!/usr/bin/python3

import time
import logging

from datetime import datetime
from hashlib import sha1, md5


class TimeHasher():
    """Get hash of current time."""

    hash_algorithms = {'sha1': sha1,
                       'md5': md5}

    def __init__(self, settings) -> None:
        self.settings = settings

        self.hasher = self.hash_algorithms[self.settings['hash_algorithm']]()

    def HashNow(self) -> str:
        date_str = "{:%Y-%m-%dT%H:%M:%S}".format(datetime.now())
        input = date_str.encode(self.settings['string_encoding'])

        logging.debug("Creating {}-hash of input {}".format(
                self.settings['hash_algorithm'],
                date_str))

        self.hasher.update(input)
        return self.hasher.hexdigest()

    def Sleep(self) -> None:
        time.sleep(self.settings['sleep_time'])


if __name__ == "__main__":
    pass
