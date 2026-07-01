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
mkdir -p build/$APP/usr/share/youjust
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
Description: Sentence-style Linux command tool
EOF

# ---------------------------
# Install main program
# ---------------------------
install -Dm755 youjust.py build/$APP/usr/bin/youjust

# ---------------------------
# Install shell wrapper (REQUIRED for cd)
# ---------------------------
install -Dm644 youjust.sh build/$APP/usr/share/youjust/youjust.sh

# ---------------------------
# Enable wrapper automatically in bash
# ---------------------------
cat > build/$APP/DEBIAN/postinst <<'EOF'
#!/bin/bash
set -e

SOURCE_LINE="source /usr/share/youjust/youjust.sh"

if ! grep -q "youjust.sh" /etc/bash.bashrc; then
    echo "$SOURCE_LINE" >> /etc/bash.bashrc
fi
EOF

chmod 755 build/$APP/DEBIAN/postinst

# ---------------------------
# Bash completion (UNCHANGED LOGIC)
# ---------------------------
cat > build/$APP/usr/share/bash-completion/completions/youjust <<'EOF'
_youjust_completion() {
    local cur="${COMP_WORDS[COMP_CWORD]}"

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