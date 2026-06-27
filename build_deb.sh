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
Description: Beginner-friendly Linux command wrapper
 A simple CLI tool that translates beginner-friendly sentence-style commands
 into Linux terminal commands.
EOF

# ---------------------------
# Main program
# ---------------------------

install -Dm755 youjust.py build/$APP/usr/bin/youjust

# ---------------------------
# Shell integration
# ---------------------------

install -Dm644 youjust.sh build/$APP/etc/profile.d/youjust.sh

# ---------------------------
# Bash completion (shell integration)
# ---------------------------

cat > build/$APP/usr/share/bash-completion/completions/youjust <<'EOF'
_youjust_completion() {
    local cur="${COMP_WORDS[1]}"

    COMPREPLY=($(compgen -W "
        install remove update upgrade
        createfile createfolder delete
        showfile list
        copy move rename
        showsystem
        see ip
        see processes
        see space
        see whereami
        help gethelp
        clear reboot shutdown
    " -- "$cur"))
}

complete -F _youjust_completion youjust
EOF

# ---------------------------
# Build package
# ---------------------------

dpkg-deb --build build/$APP "${APP}_${VERSION}_${ARCH}.deb"

echo "Built ${APP}_${VERSION}_${ARCH}.deb"