import csv

def save_unique_ips_to_txt(csv_filename, txt_filename):
    unique_ips = set()

    with open(csv_filename, mode="r") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)  # Skip header

        for row in reader:
            if len(row) == 2:
                _, ip_address = row
                if ip_address != "N/A":
                    unique_ips.add(ip_address.strip())

    with open(txt_filename, mode="w") as txt_file:
        for ip in sorted(unique_ips):
            txt_file.write(f"{ip}\n")

    print(f"Unique resolved IPs have been saved to {txt_filename}")

# File paths
csv_filename = "Results/subdomains_ip_addresses.csv"
txt_filename = "Results/resolved_ips.txt"

# Save unique IPs to the txt file (optional if already exists)
save_unique_ips_to_txt(csv_filename, txt_filename)

# List of ports
ports = [80, 8080, 443]

# Read unique IPs from two input files
txt_file1 = "Results/subdomains.txt"
txt_file2 = "Results/resolved_ips.txt"

ips = set()
for filename in [txt_file1, txt_file2]:
    with open(filename, "r") as ip_file:
        for line in ip_file:
            ip = line.strip()
            if ip:
                ips.add(ip)

# Generate IP-port pairs and write to output file
with open("Results/ip_port_pairs.txt", "w") as output_file:
    for ip in sorted(ips):
        for port in ports:
            output_file.write(f"{ip}:{port}\n")

print("IP-port pairs have been saved to Results/ip_port_pairs.txt")
