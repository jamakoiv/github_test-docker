import unittest
import subprocess
import time


# NOTE: This is not strictly an unit-test. Behaviour depends on the
#       child process to react in time for creation and termination,
#       therefore we need the clumsy time.sleep calls for waiting.
#       This is closer to functional or integration test.

class TestExitGracefully(unittest.TestCase):
    wait_for_process = 0.5

# BUG: send_signal(SIGINT) gives error "unsupported signal: 2".
#    def test_exit_sigint(self):
#        cmd = "python src/testing/DockerExiter_testhelper.py"
#        proc = subprocess.Popen(cmd)
#
#        # Check subprocess is running.
#        self.assertEqual(proc.poll(), None)
#        
#        # Send sigint and check the process is terminated.
#        proc.send_signal(signal.SIGINT.value)
#        self.assertNotEqual(proc.poll(), None)

    def test_exit_sigterm(self):
        cmd = "python src/testing/DockerExiter_testhelper.py"
        proc = subprocess.Popen(cmd)

        # Check subprocess is running.
        time.sleep(self.wait_for_process)
        self.assertIsNone(proc.poll())
        
        # Send SIGTERM and check the process is terminated.
        proc.terminate()
        time.sleep(self.wait_for_process)
        self.assertIsNotNone(proc.poll())