# Proxy Server and Packet Sniffing

This project provides a simple Python script that starts a proxy server and simultaneously sniffs network packets. The proxy server is globally accessible, allowing machines from any network to connect. It also logs details of network traffic using Scapy.

## Requirements

### Python Libraries

- **Scapy**: Used for network packet sniffing.
  - Install with: `pip install scapy`
- **subprocess**: A built-in Python library used to run external commands.
- **threading**: A built-in Python library used to run multiple tasks concurrently in separate threads.

### External Dependencies

- **proxy.py**: A simple proxy server. Ensure this is installed or available in your system’s PATH.
  - You can install `proxy.py` via pip:
    ```bash
    pip install proxy.py
    ```

## Script Overview

The script performs two main tasks:

1. **Proxy Server**: 
   - Listens globally on all network interfaces for incoming connections and handles them via a proxy.
   - The proxy server listens on port `8080` by default (this can be changed).
   - You can configure how many worker threads the proxy uses to handle multiple clients at the same time.

2. **Packet Sniffing**:
   - Uses Scapy to monitor and log network traffic. Captures IP and TCP packet details, including source and destination IP addresses and ports.
   - Runs continuously, printing raw packet data to the console.

## How It Works

### Start the Proxy Server
The proxy server listens globally on all interfaces (`0.0.0.0`) at the specified port (`8080` by default). It can handle multiple connections at once, with four worker threads enabled for better performance with concurrent connections.

- **Command for proxy.py**:
  ```bash
  proxy --hostname 0.0.0.0 --port 8080 --num-workers 4
