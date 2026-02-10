import requests
import csv

# Input and output file paths
input_file = "Results/resolved_ips.txt"
output_file = "Results/ip_location.csv"

# Fields to extract
fields = ["ip", "city", "country", "postal", "timezone", "loc", "org"]

# Open CSV file for writing
with open(output_file, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)  # Write header

    # Read IPs from txt file
    with open(input_file, "r") as f:
        for line in f:
            ip = line.strip()
            if not ip:
                continue
            try:
                url = f"https://ipinfo.io/{ip}/json"
                response = requests.get(url)
                data = response.json()
                row = [data.get(field, "") for field in fields]
                writer.writerow(row)
                #print(f"[+] Saved data for {ip}")
            except Exception as e:
                print(f"[!] Error processing {ip}: {e}")
