import subprocess
import csv

# Function to run the shell command
def get_open_ports(ip):
    command = f"curl -s https://www.shodan.io/host/{ip} | grep -oP 'Ports open: \K[0-9, ]+'"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            return None
    except Exception as e:
        return None

# Read IPs from the file
with open("Results/resolved_ips.txt", "r") as file:
    ips = [line.strip() for line in file if line.strip()]

# Create/open CSV file and write headers
with open("Results/openPort.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP_Address", "Open_Ports"])  # Header row

    # Loop through each IP and write to CSV
    for ip in ips:
        open_ports = get_open_ports(ip)
        if open_ports:
            writer.writerow([ip, open_ports])
            print(f"[{ip}] Open Ports: {open_ports}")
        else:
            writer.writerow([ip, "N/A"])
            print(f"[{ip}] Open Ports: N/A")


