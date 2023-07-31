#!/bin/bash

# Create symlink to dnsleuth.py in /usr/local/bin
ln -s "$(pwd)/dnsleuth.py" /usr/local/bin/dnsleuth

# Make dnsleuth.py executable
chmod +x dnsleuth.py

echo "DNSleuth has been installed successfully. To use it, simply run 'dnsleuth' in a terminal."