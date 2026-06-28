#!/bin/bash

set -e

APP="youjust"
VERSION="1.0"
ARCH="all"

rm -rf build

# ---------------------------
# Directory structure
# ---------------------------
mkdir -p build/$APP/DEBIAN
mkdir -p build/$APP/usr/bin
mkdir -p build/$APP/usr/share/bash-completion/completions

# ---------------------------
# Control file
# ---------------------------
cat > build/$APP/DEBIAN/control <<EOF
Package: $APP
Version: $VERSION
Section: utils
Priority: optional
Architecture: $ARCH
Maintainer: AramCZ
Homepage: https://aramczdev.github.io
Description: Sentence-style Linux command tool
 A CLI tool that translates sentence-style commands into Linux terminal actions.
EOF

# ---------------------------
# Main program
# ---------------------------
install -Dm755 youjust.py build/$APP/usr/bin/youjust

# ---------------------------
# Bash completion (updated to match Python commands)
# ---------------------------
cat > build/$APP/usr/share/bash-completion/completions/youjust <<'EOF'
_youjust_completion() {
    local cur="${COMP_WORDS[1]}"

    COMPREPLY=($(compgen -W "
        install remove update upgrade
        show system info
        show ip
        show processes
        show space
        show current directory
        create file
        create folder
        show file
        list files
        copy move rename
        go into
        ping
        kill
        clear screen
        reboot shutdown
        help get help
    " -- "$cur"))
}

complete -F _youjust_completion youjust
EOF

# ---------------------------
# Build package
# ---------------------------
dpkg-deb --build build/$APP "${APP}_${VERSION}_${ARCH}.deb"

echo "Built ${APP}_${VERSION}_${ARCH}.deb"