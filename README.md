# YouJust

A simple command-line tool that translates beginner-friendly commands into Linux terminal commands.

YouJust is a lightweight wrapper around common Linux commands designed to make the terminal more approachable for beginners. Instead of memorizing complex syntax, users can run simple commands like `youjust install`, `youjust delete`, and more.

## Features

- Beginner-friendly command syntax
- Package management shortcuts (APT)
- File and folder operations
- System information viewer
- Safe confirmations for destructive actions
- Simple CLI design with no dependencies beyond Python

## Installation

### Prerequesities

Debian, Ubuntu, Mint etc.

### From .deb package

Download the latest `.deb` release and install it:

```bash
sudo apt install (path to your .deb)
```
Dependencies should be installed automaticly. If not then install Python 3 via this command
```bash
sudo apt install python3
```

### Other Distros

YouJust is not available for other ditributions since I would have to remake it for every one of them

## Get Started

To get started just type
```bash
youjust help
```
And that will list all the available commands
