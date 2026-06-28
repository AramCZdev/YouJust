#!/usr/bin/env python3
import os
import sys
import subprocess
import shlex
import re

def run(cmd):
    print(f"> {' '.join(cmd)}")
    subprocess.run(cmd)

args = sys.argv[1:]

if not args:
    print("Usage: youjust <command>")
    sys.exit(0)

# ---------------------------
# Normalize input (fix spacing)
# ---------------------------
raw_cmd = " ".join(args)
raw_cmd = re.sub(r"\s+", " ", raw_cmd).strip()
cmd = raw_cmd.lower()

def starts(x):
    return cmd.startswith(x)

def after(x):
    if starts(x):
        return raw_cmd[len(x):].strip()
    return None


# ---------------------------
# PACKAGE MANAGEMENT
# ---------------------------
if starts("install"):
    pkg = after("install")
    if not pkg:
        print("Usage: youjust install <package>")
    else:
        run(["sudo", "apt", "install", "-y", pkg])

elif starts("remove"):
    pkg = after("remove")
    if not pkg:
        print("Usage: youjust remove <package>")
    else:
        if input(f"Remove {pkg}? [y/N]: ").lower() == "y":
            run(["sudo", "apt", "remove", "-y", pkg])

elif cmd == "update":
    run(["sudo", "apt", "update"])

elif cmd == "upgrade":
    run(["sudo", "apt", "upgrade", "-y"])


# ---------------------------
# SYSTEM INFO
# ---------------------------
elif cmd == "show system info":
    run(["bash", "-c", "fastfetch || neofetch || uname -a"])

elif cmd == "show ip":
    run(["ip", "addr"])

elif cmd == "show processes":
    run(["ps", "aux"])

elif cmd == "show space":
    run(["df", "-h"])

elif cmd == "show current directory":
    run(["pwd"])


# ---------------------------
# FILES & FOLDERS
# ---------------------------
elif starts("create file"):
    name = after("create file")
    if not name:
        print("Usage: youjust create file <name>")
    else:
        run(["touch", name])

elif starts("create folder"):
    name = after("create folder")
    if not name:
        print("Usage: youjust create folder <name>")
    else:
        run(["mkdir", "-p", name])

elif starts("delete"):
    target = after("delete")
    if not target:
        print("Usage: youjust delete <file|folder>")
    else:
        if input(f"Delete {target}? [y/N]: ").lower() == "y":
            run(["rm", "-rf", target])

elif starts("show file"):
    file = after("show file")
    if not file:
        print("Usage: youjust show file <file>")
    else:
        run(["cat", file])

elif cmd == "list files":
    run(["ls", "-lah"])


# ---------------------------
# COPY / MOVE / RENAME
# ---------------------------
elif starts("copy"):
    parts = shlex.split(raw_cmd)
    if len(parts) < 3:
        print("Usage: youjust copy <source> <destination>")
    else:
        run(["cp", "-r", parts[1], parts[2]])

elif starts("move"):
    parts = shlex.split(raw_cmd)
    if len(parts) < 3:
        print("Usage: youjust move <source> <destination>")
    else:
        run(["mv", parts[1], parts[2]])

elif starts("rename"):
    parts = shlex.split(raw_cmd)
    if len(parts) < 3:
        print("Usage: youjust rename <old> <new>")
    else:
        run(["mv", parts[1], parts[2]])


# ---------------------------
# NAVIGATION (shell wrapper handles actual cd)
# ---------------------------
elif starts("go into"):
    path = after("go into")
    if not path:
        print("Usage: youjust go into <directory>")
    else:
        try:
            os.chdir(path)
            print(f"now in {os.getcwd()}")
        except FileNotFoundError:
            print(f"No such directory: {path}")


# ---------------------------
# NETWORKING
# ---------------------------
elif starts("ping"):
    host = after("ping")
    if not host:
        print("Usage: youjust ping <host>")
    else:
        run(["ping", "-c", "4", host])


# ---------------------------
# PROCESSES
# ---------------------------
elif starts("kill"):
    pid = after("kill")
    if not pid:
        print("Usage: youjust kill <PID>")
    else:
        run(["kill", pid])


# ---------------------------
# TERMINAL
# ---------------------------
elif cmd == "clear screen":
    run(["clear"])


# ---------------------------
# POWER
# ---------------------------
elif cmd == "reboot":
    if input("Reboot computer? [y/N]: ").lower() == "y":
        run(["sudo", "reboot"])

elif cmd == "shutdown":
    if input("Shutdown computer? [y/N]: ").lower() == "y":
        run(["sudo", "shutdown", "now"])


# ---------------------------
# HELP
# ---------------------------
elif cmd in ("help", "get help"):
    print("""
YouJust - Sentence-style Linux command tool

COMMAND STYLE (IMPORTANT)
Everything is written as simple sentences:

  youjust install git
  youjust remove nano
  youjust show system info
  youjust show ip
  youjust show current directory
  youjust go into Documents
  youjust create file test.txt
  youjust create folder projects
  youjust show file notes.txt
  youjust list files
  youjust delete test.txt
  youjust copy a.txt b.txt
  youjust move a.txt folder/
  youjust rename old.txt new.txt
  youjust ping aramczdev.github.io
  youjust kill 1234
  youjust clear screen
  youjust reboot
  youjust shutdown

----------------------------
PACKAGE MANAGEMENT
----------------------------
install <package>        Install a package
remove <package>         Remove a package
update                   Update package lists
upgrade                  Upgrade system packages

----------------------------
SYSTEM INFO
----------------------------
show system info         System information
show ip                  Network info
show processes           Running processes
show space               Disk usage
show current directory   Current path

----------------------------
FILES
----------------------------
create file <name>      Create file
create folder <name>    Create folder
show file <file>        Display file contents
list files              List directory contents
delete <target>        Delete file or folder

----------------------------
NAVIGATION
----------------------------
go into <dir>          Change directory (handled via shell wrapper)

----------------------------
NETWORK
----------------------------
ping <host>            Ping a host

----------------------------
PROCESS
----------------------------
kill <pid>             Kill process

----------------------------
POWER
----------------------------
reboot                 Restart system
shutdown               Turn off system

----------------------------
TERMINAL
----------------------------
clear screen           Clear terminal
""")

else:
    print(f"Unknown command: {cmd}")
    print("Try: youjust help")