import subprocess
from scapy.all import sniff, IP, TCP
import threading

# Configure the proxy server settings
def start_proxy_server():
    address = '0.0.0.0'  # Listen on all interfaces
    port = 8080          # Port for the proxy server (can be any open port)
    
    # Run proxy.py as a subprocess and pass the desired options
    proxy_cmd = [
        'proxy', 
        '--hostname', address, 
        '--port', str(port),
        '--num-workers', '4'  # Use 4 workers for handling multiple connections
    ]

    print(f"Starting proxy server with command: {' '.join(proxy_cmd)}")
    proxy_process = subprocess.Popen(proxy_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print output and error streams from the proxy server
    print("Proxy server started. Reading output...")
    while True:
        output = proxy_process.stdout.readline()
        if output == '' and proxy_process.poll() is not None:
            break
        if output:
            print(f"PROXY OUTPUT: {output.strip()}")
    error = proxy_process.stderr.read()
    if error:
        print(f"PROXY ERROR: {error.strip()}")

    return proxy_process

# Function to log and trace packets using Scapy
def packet_callback(packet):
    if IP in packet:
        print(f"Packet from {packet[IP].src} to {packet[IP].dst}")
        if TCP in packet:
            print(f"TCP Packet - Src Port: {packet[TCP].sport}, Dst Port: {packet[TCP].dport}")
        print(f"Raw data: {bytes(packet[IP].payload)}\n")

# Start sniffing packets with Scapy
def start_sniffing():
    print("Starting packet sniffing...")
    sniff(filter="ip", prn=packet_callback, store=0)

# Main function to start both the proxy and packet sniffing
if __name__ == '__main__':
    proxy_thread = threading.Thread(target=start_proxy_server)
    proxy_thread.start()
    print("Proxy server thread started")

    start_sniffing()
