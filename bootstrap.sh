#!/bin/bash

# Ensure that the CLI is functioning correctly
set -e

echo "Setting up raspberry pi for remote temperature exporting..."

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install -y python3 python3-pip python3-venv git mariadb-client fail2ban ufw

if [ ! -d "/home/pi/RPI_Script" ]; then
    git clone https://github.com/cthacker-udel/RPI_Script.git /home/pi/paver-monitor
fi


############################
## WATCHDOG IMPLEMENTATION
############################
WATCHDOG_PATH="/home/pi/paver-monitor/scripts/wifi_watchdog.sh"
CRON_ENTRY="*/5 * * * * $WATCHDOG_PATH"

if [ ! -f "$WATCHDOG_PATH" ]; then
    echo "[ERROR] Wifi watchdog script not found at $WATCHDOG_PATH"
    exit 1
fi
chmod +x "$WATCHDOG_PATH"

###############################
## ADDING WATCHDOG TO CRONTAB
###############################
(crontab -1 2>/dev/null | grep -F "$WATCHDOG_PATH") || ((crontab -1 2>/dev/null; echo "$CRON_ENTRY") | crontab - echo "[INFO] Wifi watchdog added to crontab.")

##########################
## CREATING PYTHON VENV
##########################
cd /home/pi/paver-monitor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#########################
## CREATING SERVICE
#########################
sudo tee /etc/systemd/system/paver-monitor.service > /dev/null <<EOF
[Unit]
Description=Paver Temperature Monitor
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/paver-monitor
ExecStart=/home/pi/paver-monitor/venv/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

##########################
## SETTING SERVICE
##########################
sudo systemctl daemon-reload
sudo systemctl enable paver-monitor.service
sudo systemctl start paver-monitor.service

echo "Ensure that the .env file is placed in the root folder of the repository."
echo "Bootstrapping complete."