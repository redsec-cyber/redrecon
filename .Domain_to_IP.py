import socket
import csv
import subprocess

# Function to read subdomains from file.txt
def read_subdomains_from_file(filename):
    with open(filename, "r") as file:
        subdomains = [line.strip() for line in file if line.strip()]
    return subdomains

# Function to get IP address for a given subdomain
def get_ip_address(subdomain):
    try:
        return socket.gethostbyname(subdomain)
    except socket.gaierror:
        return "N/A"  # If the subdomain cannot be resolved

# Main function to write subdomains and IP addresses to CSV
def main():
    # Read subdomains from file.txt
    subdomains = read_subdomains_from_file("Results/subdomains.txt")
   
    # Separate resolved and unresolved subdomains
    resolved = []
    unresolved = []
    
    for subdomain in subdomains:
        ip_address = get_ip_address(subdomain)
        if ip_address != "N/A":
            resolved.append([subdomain, ip_address])
        else:
            unresolved.append([subdomain, ip_address])

    # Define the CSV output file name
    output_filename = "Results/subdomains_ip_addresses.csv"
   
    # Open the CSV file for writing
    with open(output_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
       
        # Write the header
        writer.writerow(["Subdomain", "IPAddress"])
        
        # Write resolved subdomains first
        for entry in resolved:
            writer.writerow(entry)
        
        # Write unresolved subdomains after
        for entry in unresolved:
            writer.writerow(entry)
   
    print(f"Subdomains and IP addresses have been saved to {output_filename}")

# Run the main function
if __name__ == "__main__":
    main()

