#!/bin/bash

# Check if portaudio19-dev is installed
if ! dpkg -s portaudio19-dev >/dev/null 2>&1; then
  echo "portaudio19-dev is not installed. Installing..."
  sudo apt-get update
  sudo apt-get install -y portaudio19-dev
else
  echo "portaudio19-dev is already installed."
fi
