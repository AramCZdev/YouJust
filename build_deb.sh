#!/bin/bash

set -e

APP="youjust"
VERSION="1.0.0"
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
Maintainer: AramCZ <aramcz@protonmail.com>
Description: Sentence-style Linux command tool
EOF

# ---------------------------
# Install main program
# ---------------------------
install -Dm755 youjust.py build/$APP/usr/bin/youjust

# ---------------------------
# Bash completion
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
# Wrapper script for changing directories and editing
# ---------------------------
cat > build/$APP/usr/share/youjust/wrapper.sh <<'EOF'
youjust() {
    if [[ "$1" == "edit" ]]; then
        command youjust "$@"
        return
    fi

    local output
    output=$(command youjust "$@")

    if [[ "$output" == YOUJUST_CD:* ]]; then
        cd "${output#YOUJUST_CD:}"
    else
        echo "$output"
    fi
}
EOF

# Create a postinst script to source the wrapper automatically
mkdir -p build/$APP/DEBIAN
cat > build/$APP/DEBIAN/postinst <<'EOF'
#!/bin/bash
set -e
SOURCE_LINE="source /usr/share/youjust/wrapper.sh"
for profile in /etc/bash.bashrc /etc/zsh/zshrc; do
    if [ -f "$profile" ] && ! grep -q "youjust/wrapper.sh" "$profile"; then
        echo "$SOURCE_LINE" >> "$profile"
    fi
done
EOF
chmod 755 build/$APP/DEBIAN/postinst

# ---------------------------
# Build package
# ---------------------------
dpkg-deb --build build/$APP "${APP}_${VERSION}_${ARCH}.deb"

echo "Built ${APP}_${VERSION}_${ARCH}.deb"