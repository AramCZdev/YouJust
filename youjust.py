#!/usr/bin/env python3
import sys
import subprocess

def run(cmd):
    print(f"> {' '.join(cmd)}")
    subprocess.run(cmd)

args = sys.argv[1:]

if not args:
    print("Usage: youjust <command>")
    sys.exit(0)

cmd = " ".join(args)

def norm(text):
    return text.lower()

def starts(prefix):
    return cmd.lower().startswith(prefix)

def after(prefix):
    if starts(prefix):
        return cmd[len(prefix):].strip()
    return None

# ---------------------------
# Sentence parsing system
# ---------------------------

cmd = " ".join(args).lower()

def after(prefix):
    if cmd.startswith(prefix):
        return cmd[len(prefix):].strip()
    return None


# ---------------------------
# Package management
# ---------------------------

if cmd.startswith("install"):
    pkg = after("install")
    if not pkg:
        print("Usage: youjust install <package>")
    else:
        run(["sudo", "apt", "install", "-y", pkg])

elif cmd.startswith("remove"):
    pkg = after("remove")
    if not pkg:
        print("Usage: youjust remove <package>")
    else:
        confirm = input(f"Remove {pkg}? [y/N]: ")
        if confirm.lower() == "y":
            run(["sudo", "apt", "remove", "-y", pkg])

elif cmd == "update":
    run(["sudo", "apt", "update"])

elif cmd == "upgrade":
    run(["sudo", "apt", "upgrade", "-y"])


# ---------------------------
# System info
# ---------------------------

elif cmd == "showsystem":
    run(["bash", "-c", "fastfetch || neofetch || uname -a"])

elif cmd.startswith("see ip"):
    run(["ip", "addr"])

elif cmd.startswith("see processes"):
    run(["ps", "aux"])

elif cmd.startswith("see space"):
    run(["df", "-h"])

elif cmd.startswith("see whereami"):
    run(["pwd"])


# ---------------------------
# Files & folders
# ---------------------------

elif cmd.startswith("create file"):
    name = after("create file")
    if not name:
        print("Usage: youjust create file <name>")
    else:
        run(["touch", name])

elif cmd.startswith("create folder"):
    name = after("create folder")
    if not name:
        print("Usage: youjust create folder <name>")
    else:
        run(["mkdir", "-p", name])

elif cmd.startswith("delete"):
    target = after("delete")
    if not target:
        print("Usage: youjust delete <file|folder>")
    else:
        confirm = input(f"Delete {target}? [y/N]: ")
        if confirm.lower() == "y":
            run(["rm", "-rf", target])

elif cmd.startswith("show file"):
    file = after("show file")
    if not file:
        print("Usage: youjust show file <file>")
    else:
        run(["cat", file])

elif cmd == "list":
    run(["ls", "-lah"])


# ---------------------------
# Copy / Move / Rename
# ---------------------------

elif cmd.startswith("copy"):
    parts = cmd.split()
    if len(parts) < 3:
        print("Usage: youjust copy <source> <destination>")
    else:
        run(["cp", "-r", parts[1], parts[2]])

elif cmd.startswith("move"):
    parts = cmd.split()
    if len(parts) < 3:
        print("Usage: youjust move <source> <destination>")
    else:
        run(["mv", parts[1], parts[2]])

elif cmd.startswith("rename"):
    parts = cmd.split()
    if len(parts) < 3:
        print("Usage: youjust rename <old> <new>")
    else:
        run(["mv", parts[1], parts[2]])


# ---------------------------
# Navigation
# ---------------------------

elif starts("go into"):
    path = after("go into")

    if not path:
        print("Usage: youjust go into <dir>")
    else:
        print(f"cd {path}")


# ---------------------------
# Networking
# ---------------------------

elif cmd.startswith("ping"):
    host = after("ping")
    if not host:
        print("Usage: youjust ping <host>")
    else:
        run(["ping", "-c", "4", host])


# ---------------------------
# Processes
# ---------------------------

elif cmd.startswith("kill"):
    pid = after("kill")
    if not pid:
        print("Usage: youjust kill <PID>")
    else:
        run(["kill", pid])


# ---------------------------
# Terminal
# ---------------------------

elif cmd == "clear":
    run(["clear"])


# ---------------------------
# Power
# ---------------------------

elif cmd == "reboot":
    confirm = input("Reboot computer? [y/N]: ")
    if confirm.lower() == "y":
        run(["sudo", "reboot"])

elif cmd == "shutdown":
    confirm = input("Shutdown computer? [y/N]: ")
    if confirm.lower() == "y":
        run(["sudo", "shutdown", "now"])


# ---------------------------
# Help
# ---------------------------

elif cmd in ("help", "gethelp"):
    print("""
YouJust - Sentence-style Linux command tool

You can write commands like natural language:

  youjust install git
  youjust remove nano
  youjust see ip
  youjust go into Documents
  youjust create file test.txt

----------------------------
PACKAGE MANAGEMENT
----------------------------
install <package>        Install a program
remove <package>         Remove a program
update                   Refresh package list
upgrade                  Upgrade all packages

----------------------------
SYSTEM
----------------------------
showsystem               Show system info
see ip                   Show network info
see processes            List running processes
see space                Show disk usage
see whereami             Show current directory

----------------------------
FILES
----------------------------
create file <name>      Create a file
create folder <name>    Create a folder
show file <file>       Display file contents
list                    List directory contents
delete <target>        Delete file or folder

----------------------------
NAVIGATION
----------------------------
go into <dir>          Show cd command

----------------------------
NETWORK
----------------------------
ping <host>            Ping a server

----------------------------
POWER
----------------------------
reboot                 Restart system
shutdown               Turn off system

----------------------------
TERMINAL
----------------------------
clear                  Clear screen
""")

else:
    print(f"Unknown command: {cmd}")
    print("Try: youjust help")