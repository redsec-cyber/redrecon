This tool is intended for **authorized security testing and educational purposes only**.

Users are responsible for:
- Ensuring they have permission to scan targets
- Protecting API keys and sensitive output
- Securing deployment environments

The maintainer is **not responsible** for misuse or illegal activity.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Features
- Subdomain discovery
- IP resolution
- Open port detection
- Technology and location identification
- Web screenshots
- Directory enumeration (🔴active scanning - select carefully)
- CSV result merger

## Requirements
- Linux (Kali / Ubuntu recommended)
- Python 3.x
----------------------------------------------------------------------------------------------------------------------
If you see:
Error: No supported terminal emulator found

Install:
sudo apt install xfce4-terminal

Add your keys to api_key.txt:

VIRUSTOTAL_API_KEY=your_key_here
SECURITYTRAILS_API_KEY=your_key_here

Usage
python main.py
Enter a domain, select modules, and run the tool.

----------------------------------------------------------------------------------------------------------------------

## 📁 Output
- `screenshots/` – portal screenshots (`.png`)
- `Results/`
  - `subdomains.csv`
  - `ip_addresses.csv`
  - `open_ports.csv`
  - `technology.csv`
  - `location.csv`
  - `directories/` – directory enumeration results(`.csv`)
