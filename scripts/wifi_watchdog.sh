#!/bin/bash
LOGFILE="/home/pi/paver-monitor/wifi_watchdog.log"

check_wifi() {
    if ! ping -c 1 -W 2 8.8.8.8 >/dev/null 2>&1; then
        echo "$(date): Wifi down, attempting reconnect..." >> "$LOGFILE"
        sudo nmcli networking off
        sleep 5
        sudo nmcli networking on
        sleep 10

        if ping -c 1 -W 2 8.8.8.8 >/dev/null 2>&1; then
            echo "$(date): Reconnected successfully." >> "$LOGFILE"
        else
            echo "$(date): Still no connection after retry." >> "$LOGFILE"
        fi
    fi
}

check_wifi