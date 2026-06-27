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

# ---------------------------
# Sentence parsing
# ---------------------------

# turn: ["see", "ip"] -> cmd = "see ip"
cmd = " ".join(args).lower()

# split helper for arguments after keyword
rest = args[1:] if len(args) > 1 else []


# ---------------------------
# Commands
# ---------------------------

if cmd == "install":
    if len(args) < 2:
        print("Usage: youjust install <package>")
    else:
        run(["sudo", "apt", "install", "-y", args[1]])

elif cmd == "remove":
    if len(args) < 2:
        print("Usage: youjust remove <package>")
    else:
        confirm = input(f"Remove {args[1]}? [y/N]: ")
        if confirm.lower() == "y":
            run(["sudo", "apt", "remove", "-y", args[1]])

elif cmd == "update":
    run(["sudo", "apt", "update"])

elif cmd == "upgrade":
    run(["sudo", "apt", "upgrade", "-y"])


# ---------------------------
# File ops
# ---------------------------

elif cmd == "createfile":
    if len(args) < 2:
        print("Usage: youjust createfile <name>")
    else:
        run(["touch", args[1]])

elif cmd == "createfolder":
    if len(args) < 2:
        print("Usage: youjust createfolder <name>")
    else:
        run(["mkdir", "-p", args[1]])

elif cmd == "makeexec":
    if len(args) < 2:
        print("Usage: youjust makeexec <file>")
    else:
        run(["chmod", "+x", args[1]])

elif cmd == "delete":
    if len(args) < 2:
        print("Usage: youjust delete <file|folder>")
    else:
        confirm = input(f"Delete {args[1]}? [y/N]: ")
        if confirm.lower() == "y":
            run(["rm", "-rf", args[1]])


# ---------------------------
# System (sentence style)
# ---------------------------

elif cmd == "showsystem":
    run(["bash", "-c", "fastfetch || neofetch || uname -a"])

elif cmd == "see ip":
    run(["ip", "addr"])

elif cmd == "see processes":
    run(["ps", "aux"])

elif cmd == "see space":
    run(["df", "-h"])

elif cmd == "see whereami":
    run(["pwd"])


# ---------------------------
# Navigation
# ---------------------------

elif cmd == "gointo":
    path = " ".join(args[1:])
    if not path:
        print("Usage: youjust gointo <dir>")
    else:
        print(f"cd {path}")


# ---------------------------
# Networking
# ---------------------------

elif cmd == "ping":
    if len(args) < 2:
        print("Usage: youjust ping <host>")
    else:
        run(["ping", "-c", "4", args[1]])


# ---------------------------
# Process kill
# ---------------------------

elif cmd == "kill":
    if len(args) < 2:
        print("Usage: youjust kill <PID>")
    else:
        run(["kill", args[1]])


# ---------------------------
# Disk usage
# ---------------------------

elif cmd == "folderusage":
    if len(args) < 2:
        run(["du", "-sh", "."])
    else:
        run(["du", "-sh", args[1]])


# ---------------------------
# File viewing
# ---------------------------

elif cmd == "showfile":
    if len(args) < 2:
        print("Usage: youjust showfile <file>")
    else:
        run(["cat", args[1]])

elif cmd == "list":
    run(["ls", "-lah"])


# ---------------------------
# Copy / Move
# ---------------------------

elif cmd == "copy":
    if len(args) < 3:
        print("Usage: youjust copy <source> <destination>")
    else:
        run(["cp", "-r", args[1], args[2]])

elif cmd == "move":
    if len(args) < 3:
        print("Usage: youjust move <source> <destination>")
    else:
        run(["mv", args[1], args[2]])

elif cmd == "rename":
    if len(args) < 3:
        print("Usage: youjust rename <old> <new>")
    else:
        run(["mv", args[1], args[2]])


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
YouJust - Beginner-friendly Linux command tool

This tool lets you use simple sentence-style commands instead of complex Linux syntax.

The idea is:
  youjust <action> <thing>

Example:
  youjust install htop
  (installs a program without needing apt commands)

----------------------------
PACKAGE MANAGEMENT
----------------------------

install <package>
  Installs a program using the system package manager (APT).
  Example: youjust install git

remove <package>
  Removes a program from your system.
  Example: youjust remove nano

update
  Refreshes the list of available packages.
  Example: youjust update

upgrade
  Updates all installed programs to their latest versions.
  Example: youjust upgrade


----------------------------
SYSTEM INFORMATION
----------------------------

showsystem
  Displays basic system info (uses fastfetch, neofetch, or uname).

see ip
  Shows your network IP addresses.

see processes
  Lists all running programs.

see space
  Shows how much disk space is used.

see whereami
  Shows your current folder location.


----------------------------
FILES & FOLDERS
----------------------------

createfile <name>
  Creates a new empty file.

createfolder <name>
  Creates a new folder (directory).

showfile <file>
  Displays the contents of a file.

list
  Shows all files in the current folder.

copy <source> <destination>
  Copies files or folders.

move <source> <destination>
  Moves files or folders.

rename <old> <new>
  Renames a file or folder.

delete <file/folder>
  Deletes a file or folder (asks for confirmation first).


----------------------------
NAVIGATION
----------------------------

gointo <dir>
  Shows the command needed to enter a folder (cd <dir>).


----------------------------
NETWORKING
----------------------------

ping <host>
  Checks if a website or server is reachable.


----------------------------
POWER COMMANDS
----------------------------

reboot
  Restarts your computer (asks for confirmation).

shutdown
  Turns off your computer (asks for confirmation).


----------------------------
TERMINAL
----------------------------

clear
  Clears the terminal screen.

----------------------------

Tip:
  This tool is designed to help beginners learn Linux commands by using simpler language first.
  Over time, you will naturally start recognizing the real Linux commands underneath.
""")

else:
    print(f"Unknown command: {cmd}")
    print("Try: youjust help")