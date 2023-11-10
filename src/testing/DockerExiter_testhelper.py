
import sys
sys.path.append("src/")

from DockerExiter import ExitGracefully

if __name__ == "__main__":
    prog = ExitGracefully()
    while prog.running:
        pass