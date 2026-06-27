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

cmd = args[0].lower()


# ---------------------------
# Package management (APT)
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
# File operations
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
# Navigation (limited)
# ---------------------------

elif cmd == "gointo":
    if len(args) < 2:
        print("Usage: youjust gointo <dir>")
    else:
        print(f"cd {args[1]}")

# ---------------------------
# Fastfetch or Neofetch
# ---------------------------

elif cmd == "showsystem":
    run(["bash", "-c", "fastfetch || neofetch || uname -a"])

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
# Networking
# ---------------------------

elif cmd == "ip":
    run(["ip", "addr"])

elif cmd == "ping":
    if len(args) < 2:
        print("Usage: youjust ping <host>")
    else:
        run(["ping", "-c", "4", args[1]])

# ---------------------------
# Process management
# ---------------------------

elif cmd == "processes":
    run(["ps", "aux"])

elif cmd == "kill":
    if len(args) < 2:
        print("Usage: youjust kill <PID>")
    else:
        run(["kill", args[1]])

# ---------------------------
# Disk usage
# ---------------------------

elif cmd == "space":
    run(["df", "-h"])

elif cmd == "folderusage":
    if len(args) < 2:
        run(["du", "-sh", "."])
    else:
        run(["du", "-sh", args[1]])

# ---------------------------
# Searching
# ---------------------------

elif cmd == "find":
    if len(args) < 2:
        print("Usage: youjust find <filename>")
    else:
        run(["find", ".", "-name", args[1]])

# ---------------------------
# Current directory
# ---------------------------

elif cmd == "whereami":
    run(["pwd"])

# ---------------------------
# Clear terminal
# ---------------------------

elif cmd == "clear":
    run(["clear"])

# ---------------------------
# Reboot / Shutdown
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

elif cmd == "help":
    print("""
YouJust - Beginner CLI wrapper for Debian

Package management:
  install <pkg>         Install package via apt
  remove <pkg>          Remove package via apt
  update                Update package list
  upgrade               Upgrade installed packages

System:
  showsystem            Show system information
  processes             List running processes
  kill <PID>            Kill a process
  reboot                Reboot the computer
  shutdown              Shut down the computer

Files & folders:
  createfile <name>     Create an empty file
  createfolder <name>   Create a folder
  showfile <file>       Display a file
  copy <src> <dst>      Copy a file or folder
  move <src> <dst>      Move a file or folder
  rename <old> <new>    Rename a file or folder
  delete <path>         Delete a file or folder
  makeexec <file>       Make a file executable
  list                  List files in the current directory
  find <name>           Find a file

Navigation:
  gointo <dir>          Print the cd command
  whereami              Show current directory

Networking:
  ip                    Show IP/network information
  ping <host>           Ping a host

Disk:
  space                 Show disk usage
  folderusage [dir]     Show folder size

Terminal:
  clear                 Clear the terminal

Other:
  help                  Show this help
""")

else:
    print(f"Unknown command: {cmd}")
    print("Try: youjust help")