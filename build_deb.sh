#!/bin/bash

set -e

APP="youjust"
VERSION="1.0"
ARCH="all"

rm -rf build
mkdir -p build/$APP/DEBIAN
mkdir -p build/$APP/usr/bin
mkdir -p build/$APP/etc/profile.d

# Control file
cat > build/$APP/DEBIAN/control <<EOF
Package: $APP
Version: $VERSION
Section: utils
Priority: optional
Architecture: $ARCH
Maintainer: AramCZ
Homepage: https://aramczdev.github.io
Description: Beginner-friendly Linux command wrapper
EOF

# Main program
install -m755 youjust.py build/$APP/usr/bin/youjust

# Shell integration
install -m644 youjust.sh build/$APP/etc/profile.d/youjust.sh

# Build package
dpkg-deb --build build/$APP "${APP}_${VERSION}_${ARCH}.deb"

echo "Built ${APP}_${VERSION}_${ARCH}.deb"