#!/usr/bin/python3

import yaml
import logging
import datetime
import argparse

from DockerExiter import ExitGracefully
from TimeHasher import TimeHasher

parser = argparse.ArgumentParser(
    prog="Testing program.",
    description="Periodically gets the hash of current datetime.")
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()


def init_logging_file(d: datetime.date) -> dict:
    f_log = "{:%Y_%m_%d}".format(d)
    logging.basicConfig(filename=f"log_{f_log}.log",
                        encoding='utf-8',
                        level=logging.INFO,
                        format="%(asctime)s %(levelname)s:%(message)s")

    # Echo logging to stderr.
    if args.verbose:
        logger = logging.getLogger()
        logger.addHandler(logging.StreamHandler())


if __name__ == "__main__":
    init_logging_file(datetime.datetime.now())

    f_settings = "settings.yaml"
    with open(f_settings, 'r') as f:
        settings = yaml.safe_load(f)

    prog = ExitGracefully()
    h = TimeHasher(settings)

    while prog.running:
        res = h.HashDatetime(datetime.datetime.now())
        logging.info(res)
        h.Sleep()
