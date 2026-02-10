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

## ⏳ Execution Flow
**Phase 1 (Automatic)**  
- Subdomain discovery  
- Domain-to-IP resolution  
⏱️ ~5–10 minutes, then click **OK** to continue.

**Phase 2 (Optional)**  
Once confirmed, the tool opens 4–5 terminal windows that close automatically after execution. The full scan may take 10–20 minutes on a high-speed connection.
- Open ports  
- Technology & location  
- Screenshots  
- Directory enumeration  
Once confirmed, the tool will automatically open 4–5 terminal windows, which will close after execution. The full scan may take 10–20 minutes on a high-speed connection. 
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
