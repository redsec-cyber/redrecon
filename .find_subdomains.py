import requests
import json
import sys
import os

# -------------------------------
# Read domain
# -------------------------------
try:
    with open("Results/domain.txt", "r") as f:
        domain = f.read().strip()

    print(f"Domain received from GUI: {domain}")

except FileNotFoundError:
    print("Error: domain.txt not found. Please run the GUI first.")
    sys.exit(1)

# -------------------------------
# Read API keys from file
# -------------------------------
Virustotal_api_key = None
Securitytails_api_key = None

if os.path.exists("api_key.txt"):
    with open("api_key.txt", "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                if key == "VIRUSTOTAL_API_KEY":
                    Virustotal_api_key = value
                elif key == "SECURITYTRAILS_API_KEY":
                    Securitytails_api_key = value
else:
    print("[!] api_key.txt file not found.")
    sys.exit(1)

# Validate keys
if not Virustotal_api_key or not Securitytails_api_key:
    print("[!] One or more API keys are missing in api_key.txt")
    sys.exit(1)

print("[*] API keys loaded successfully.")


# List to collect domains
domains = []

# --- Fetch from crt.sh ---
def fetch_crtsh(domain):
    print("[*] Fetching from crt.sh...")
    url = f"https://crt.sh/?q={domain}&output=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            crt_subdomains = sorted(set(entry['name_value'].replace('*.','') for entry in data))
            domains.extend(crt_subdomains)
            print(f"  [+] Found {len(crt_subdomains)} subdomains from crt.sh")
        except json.JSONDecodeError:
            print("[!] Error decoding JSON from crt.sh")
    else:
        print(f"[!] Failed to fetch from crt.sh (Status Code: {response.status_code})")

# --- Fetch from VirusTotal ---
def fetch_virustotal(domain, api_key):
    print("[*] Fetching from VirusTotal...")
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey': api_key, 'domain': domain}
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            jdata = response.json()
            virus_subdomains = sorted(jdata.get('subdomains', []))
            domains.extend(virus_subdomains)
            print(f"  [+] Found {len(virus_subdomains)} subdomains from VirusTotal")
        else:
            print(f"[!] VirusTotal API Error (Status Code: {response.status_code})")
    except requests.ConnectionError:
        print("[!] Could not connect to VirusTotal API")
        sys.exit(1)

# --- Optional: Fetch from SecurityTrails (currently commented) ---
def fetch_securitytrails(domain, api_key):
    print("[*] Fetching from SecurityTrails...")
    url = f'https://api.securitytrails.com/v1/domain/{domain}/subdomains?children_only=false&include_inactive=true'
    headers = {'APIKEY': api_key, 'Accept': 'application/json'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            tails_subdomains = response.json().get('subdomains', [])
            for sub in tails_subdomains:
                domains.append(f"{sub}.{domain}")
            print(f"  [+] Found {len(tails_subdomains)} subdomains from SecurityTrails")
        else:
            print(f"[!] SecurityTrails API Error (Status Code: {response.status_code})")
    except requests.ConnectionError:
        print("[!] Could not connect to SecurityTrails API")

# --- Main execution ---
if __name__ == "__main__":
    fetch_crtsh(domain)
    fetch_virustotal(domain, Virustotal_api_key)
    fetch_securitytrails(domain, Securitytails_api_key)

    # --- Clean and Save ---
    cleaned = set()
    for entry in domains:
        for sub in entry.split('\n'):
            cleaned.add(sub.strip())

    with open("Results/subdomains.txt", "w") as f:
        for subdomain in sorted(cleaned):
            f.write(subdomain + "\n")

    print(f"[*] Total unique subdomains saved: {len(cleaned)}")
    print("[*] Done! Subdomains saved to Results/subdomains.txt.")
