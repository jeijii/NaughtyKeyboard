import socket, threading, sys, cmd

bind_ip = '0.0.0.0'
bind_port = 4444

print("Welcome to Naughty Server")
print("Waiting for client to et phone home")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(1)

conn, address = server.accept()
print("Connected: "+repr(address))

def writeall(sock):
    while True:
        data = sock.recv(256)
        if not data:
            sys.stdout.write("\r\n*** EOF ***\r\n\r\n")
            sys.stdout.flush()
        sys.stdout.write(data)
        sys.stdout.flush()


def launchshell():
    writer = threading.Thread(target=writeall, args=(conn,))
    writer.start()
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            conn.send(d)
    except EOFError:
        pass


class shell(cmd.Cmd):
    prompt = "Naughty> "
    file = None

    def do_list_scripts(self, arg):
        'View all the scripts available in the pi'
        conn.send("ls -l /home/pi/NaughtyKeyboard/dakencoder \r\n")
        print(conn.recv(1028))
        print(conn.recv(1028))
        print(conn.recv(1028))
        print(conn.recv(1028))

    def do_launch_scripts(self, arg):
        'Execute a ducky script to connected computer. \nExample: launch_script rickroll.txt'
        print("Sending Command...")
        data = "python /home/pi/NaughtyKeyboard/dakencoder/dakencoder.py /home/pi/NaughtyKeyboard/dakencoder/"+arg+" \r\n"
        conn.send(data)

    def do_shell(self, arg):
        'open an interactive shell to the pi'
        launchshell()

    def do_exit(self, arg):
        'Exits Application'
        sys.exit(0)

if __name__ == '__main__':
    shell().cmdloop()

