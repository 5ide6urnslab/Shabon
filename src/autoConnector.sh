#!/bin/bash

function is_connected() {
  {
    printf "info $device\n\n"
  } | bluetoothctl | grep "Connected: " | sed -e 's/Connected: //' | sed -e 's/^[[:blank:]]*//'
}


device=98:B6:E9:FC:DE:B0

if [[ $(is_connected) = "yes" ]]; then
  printf "Connected\n\n"
else
  /usr/bin/python3 /usr/local/bin/blinkLed.py

  {
    printf "scan off\n\n"
    sleep 5
    printf "scan on\n\n"
    sleep 10
    printf "remove $device\n\n"
    sleep 10
    printf "pair $device\n\n"
    sleep 5
    printf "connect $device\n\n"
    sleep 5
  } | bluetoothctl

  if [[ $(is_connected) = "yes" ]]; then
    /usr/bin/python3 /usr/local/bin/putonLed.py
    /usr/bin/python3 /usr/local/bin/switchJoycon.py
  else
    printf "nothing\n\n"
  fi
fi
