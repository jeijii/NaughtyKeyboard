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

    def do_view_id(self, arg):
        'view the pid and vid of the duck'
        data = "cat /home/pi/NaughtyKeyboard/boot/config.cfg"
        conn.send(data)
        print(conn.recv(1028))
    def do_change_pid(self, arg):
        'Changes pid. Restart to see effect \nWARNING: Changing to an Invalid PID might cause the pi to hang.'
        data = "python /home/pi/NaughtyKeyboard/boot/changepid.py " + arg + " \r\n"
        conn.send(data)

    def do_change_vid(self, arg):
        'Changes vid. Restart to see effect. \nNot often needed, change PID for device to enumerate again\nWARNING: Changing to an Invalid VID might cause the pi to hang.'
        data = "python /home/pi/NaughtyKeyboard/boot/changevid.py " + arg + " \r\n"
        conn.send(data)
    def do_exit(self, arg):
        'Exits Application'
        sys.exit(0)

if __name__ == '__main__':
    shell().cmdloop()

