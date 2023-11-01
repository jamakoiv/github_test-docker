#!/usr/bin/python3

import logging
import signal
from signal import SIGINT, SIGTERM


class ExitGracefully():
    """Simple class for attaching OS SIGINT and SIGTERM to terminate
    the application. Mainly intented to stop program running on eternal loop
    inside docker container.

    Usage:

    prog = ExitGracefully()
    while prog.running:
        <do stuff>
    """

    def __init__(self):
        self.running: bool = True

        signal.signal(SIGINT, self.exit_program)
        signal.signal(SIGTERM, self.exit_program)

    def exit_program(self, signum, frame):
        self.running = False
        logging.info(f"Received signum {signum}. Exiting...")

    def __call__(self):
        return self.running
