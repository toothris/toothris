#!/bin/bash

set -e

. /toothris-www/setup/share.sh

sed 's/^CheckSpace/#CheckSpace/g' -i /etc/pacman.conf

pacman-key --refresh-keys

# Pacman database has changed in version 4.2 on 2014-12-29.
# Need to upgrade it first before going any further.
echo "Server = $AA_ROOT/repos/2014/12/28/\$repo/os/\$arch" \
    > /etc/pacman.d/mirrorlist
pacman -Syyuu --noconfirm

echo "Server = $AA_ROOT/repos/2014/12/29/\$repo/os/\$arch" \
    > /etc/pacman.d/mirrorlist
pacman -Sy --noconfirm pacman
pacman-db-upgrade
pacman -Syyuu --noconfirm

# Finish the upgrade.
echo "Server = $AA_ROOT/repos/$AA_YEAR/$AA_MONTH/$AA_DAY/\$repo/os/\$arch" \
    > /etc/pacman.d/mirrorlist
pacman -Syyuu --noconfirm
pacman -S --noconfirm --needed base base-devel rsyslog sudo
paccache -rk0

# user
useradd -u 1000 -m user -G wheel
chmod +w /etc/sudoers
echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
chown -R user:user /toothris-www

pacman -S --noconfirm --needed git imagemagick nodejs ttf-dejavu \
                               xorg-server-xvfb xorg-xset

sudo -u user bash -l /toothris-www/setup/as-user.sh

paccache -rk0
