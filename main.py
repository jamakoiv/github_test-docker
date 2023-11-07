#!/usr/bin/python3

import yaml
import logging
import datetime

from DockerExiter import ExitGracefully
from TimeHasher import TimeHasher


def init_logging_file(d: datetime.date) -> dict:
    f_log = "{:%Y_%m_%d}".format(d)
    logging.basicConfig(filename=f"log_{f_log}.log",
                        encoding='utf-8',
                        level=logging.INFO,
                        format="%(asctime)s %(levelname)s:%(message)s")

    # Echo logging to stderr.
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
        res = h.HashNow()
        logging.info(res)
        h.Sleep()
