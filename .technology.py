import subprocess
import csv
import re

# Run the httpx command
result = subprocess.run(['./.prebuild/httpx', '-td', '-nc','-l', 'Results/resolved_ips.txt'], capture_output=True, text=True)

# Check for errors
if result.returncode != 0:
    print("Error running httpx:", result.stderr)
else:
    lines = result.stdout.strip().split('\n')
    data = []

    for line in lines:
        match = re.match(r'(\S+)\s+\[(.+)\]', line)
        if match:
            url = match.group(1)
            techs = match.group(2)
            data.append([url, techs])
        else:
            print(f"Line did not match expected format: {line}")

    # Write to CSV
    with open('Results/technology.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['URL', 'Technologies'])
        writer.writerows(data)

    print("Saved output to Results/technology.csv")
