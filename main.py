#!/bin/bash
cd
if [ -e "/data/data/com.termux/files/home/storage" ]; then
    rm -rf /data/data/com.termux/files/home/storage
fi
termux-setup-storage
yes | pkg update
. <(curl https://cdn.quanghuynopro.com/store/termux-change-repo.sh)
yes | pkg upgrade
yes | pkg i python
yes | pkg i python-pip 
pip install httpx colorama
curl -Ls "https://raw.githubusercontent.com/PHAAutoSetup/Script/refs/heads/main/Update.py" -o /sdcard/Download/update.py"

if ! command -v su >/dev/null 2>&1 || ! su -c 'exit' >/dev/null 2>&1; then
    exit
fi
su -c "settings put global development_settings_enabled 1" && su -c "am kill-all" && su -c "cd /sdcard/Download && export PATH=\$PATH:/data/data/com.termux/files/usr/bin && export TERM=xterm-256color && python ./update.py"
