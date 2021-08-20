#!/bin/bash

SCRIPT_DIR=`dirname "$(readlink -f "$BASH_SOURCE")"`
INDICATOR_APP_PATH="${SCRIPT_DIR}/headset-charge-indicator.py"

echo "Creating ~/.config/autostart/headset-charge-indicator.desktop"
mkdir -p ~/.config/autostart/
cat <<EOF >~/.config/autostart/headset-charge-indicator.desktop
[Desktop Entry]
Name=Wireless headset app-indicator
Type=Application
Exec=${INDICATOR_APP_PATH}
X-GNOME-Autostart-enabled=true
EOF
