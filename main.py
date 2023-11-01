#!/usr/bin/python3

import yaml
import logging

from DockerExiter import ExitGracefully
from TimeHasher import TimeHasher


if __name__ == "__main__":

    f_settings = "settings.yaml"
    with open(f_settings, 'r') as f:
        settings = yaml.safe_load(f)

    prog = ExitGracefully()
    h = TimeHasher(settings)

    while prog.running:
        res = h.HashNow()
        print(res)
        logging.info(res)
        h.Sleep()
