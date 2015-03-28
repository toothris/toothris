#!/bin/sh

set -e

. /toothris-www/setup/share.sh

# libxmp
fetch-aur /li libxmp
makepkg -sc --noconfirm
sudo pacman -U --noconfirm libxmp-4.3.0-1-x86_64.pkg.tar.xz
rm libxmp-4.3.0-1-x86_64.pkg.tar.xz

# xmp
fetch-aur /xm xmp
makepkg -sc --noconfirm
sudo pacman -U --noconfirm xmp-4.0.9-1-x86_64.pkg.tar.xz
rm xmp-4.0.9-1-x86_64.pkg.tar.xz

# ffmpeg-libfdk_aac
fetch-aur /ff ffmpeg-libfdk_aac
makepkg -sc --noconfirm
sudo pacman -U --noconfirm ffmpeg-libfdk_aac-2.5.2-1-x86_64.pkg.tar.xz
rm ffmpeg-libfdk_aac-2.5.2-1-x86_64.pkg.tar.xz

# stackless-python2
fetch-aur /st stackless-python2
makepkg -sc --noconfirm
sudo pacman -U --noconfirm stackless-python2-2.7.6r3-1-x86_64.pkg.tar.xz
rm stackless-python2-2.7.6r3-1-x86_64.pkg.tar.xz

# python-rabbyt
# TODO: remove patch when upstream package is updated.
fetch-aur /py python-rabbyt
patch PKGBUILD /toothris-www/setup/python-rabbyt/PKGBUILD.patch
makepkg -sc --noconfirm
sudo pacman -U --noconfirm python-rabbyt-0.8.3-4-x86_64.pkg.tar.xz
rm python-rabbyt-0.8.3-4-x86_64.pkg.tar.xz

# toothris
# TODO: use aur package
cd /toothris-www/setup/toothris
makepkg -sc --noconfirm
sudo pacman -U --noconfirm toothris-0.0.0dev-1-any.pkg.tar.xz
rm toothris-0.0.0dev-1-any.pkg.tar.xz
