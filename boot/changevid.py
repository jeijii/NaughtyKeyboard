import sys

if len(sys.argv) < 1:
    sys.exit()
with open('setup.cfg', 'r') as file:
    data = file.readlines()

new = []
for line in data:
    if "VID=" in line:
        line = "VID="+sys.argv[1]+"\n"
    new.append(line)

with open('setup.cfg', 'w') as file:
    file.writelines(new)