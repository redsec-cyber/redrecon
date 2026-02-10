import subprocess
import platform
import shutil
import tkinter as tk
from tkinter import messagebox

def get_terminal():
    for term in ['gnome-terminal', 'xterm', 'konsole', 'mate-terminal']:
        if shutil.which(term):
            return term
    return None

def run_initial_scripts():
    try:
        subprocess.run(['python3', '.find_subdomains.py'], check=True)
        subprocess.run(['python3', '.Domain_to_IP.py'], check=True)
        messagebox.showinfo("Success", "Subdomains and IP addresses found. Task completed!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running initial scripts:\n{e}")

def run_selected_scripts():
    # Save the domain input to domain.txt
    domain = domain_entry.get().strip()
    if domain:
        with open("Results/domain.txt", "w") as f:
            f.write(domain)
    else:
        messagebox.showwarning("Warning", "Please enter a domain before running scripts.")
        return

    # Always run the initial scripts first
    run_initial_scripts()

    # Prepare selected commands
    selected_commands = []
    if add_port_var.get():
        selected_commands.append(['python3', '.add_port.py'])
    if autodirbuster_var.get():
        selected_commands.append(['python3', './.prebuild/AutoDirbuster.py', 'Results/ip_port_pairs.txt', '-w', '/usr/share/dirb/wordlists/common.txt'])
    if gowitness_var.get():
        selected_commands.append(['./.prebuild/gowitness-3.0.5-linux-amd64', 'scan', 'file', '-f', 'Results/ip_port_pairs.txt', '--no-http', '--save-content', '--write-db'])
    if technology_var.get():
        selected_commands.append(['python3', '.technology.py'])
    if openport_var.get():
        selected_commands.append(['python3', '.openPort.py'])
    if location_var.get():
        selected_commands.append(['python3', '.location.py'])

    if not selected_commands:
        messagebox.showinfo("Info", "No optional scripts selected. Only mandatory scripts were run.")
        return

    # Run selected commands
    if platform.system() == 'Windows':
        for cmd in selected_commands:
            subprocess.Popen(f'start cmd /k {" ".join(cmd)}', shell=True)
    else:
        terminal = get_terminal()
        if terminal is None:
            messagebox.showerror("Error", "No supported terminal emulator found.")
            return
        else:
            for cmd in selected_commands:
                subprocess.Popen([terminal, '--'] + cmd)
    
    messagebox.showinfo("Success", "Selected scripts started in new terminals.")

# GUI setup
root = tk.Tk()
root.title("RedRecon")
root.geometry("1000x600")
root.configure(bg="black")

title = tk.Label(root, text="Welcome to RedRecon", font=("Helvetica", 28, "bold"), fg="Red", bg="black")
title1 = tk.Label(root, 
                  text="This tool is more effective at discovering subdomains compared to other tools and also performs IP reconnaissance on resolved IPs. It serves multiple purposes, including IP reconnaissance, taking screenshots of web portals, directory listing enumeration, finding open ports from the Shodan database, and identifying server locations and technologies used...", 
                  font=("Arial", 16), 
                  fg="white", 
                  bg="black", 
                  wraplength=750,
                  justify="center",
                  anchor="center",
                  width=70,
                  height=6)
title.pack(pady=10)
title1.pack(pady=10)

# Frame for domain input
domain_frame = tk.Frame(root, bg="black")
domain_frame.pack(pady=10)

domain_label = tk.Label(domain_frame, text="Enter Domain:", font=("Arial", 16), fg="white", bg="black")
domain_label.pack(side="left", padx=5)

domain_entry = tk.Entry(domain_frame, font=("Arial", 16), width=20)
domain_entry.pack(side="left", padx=5)

# Frame for checkboxes
checkbox_frame = tk.Frame(root, bg="black")
checkbox_frame.pack(pady=10)

# Variables to track checkbox state
add_port_var = tk.BooleanVar()
autodirbuster_var = tk.BooleanVar()
gowitness_var = tk.BooleanVar()
technology_var = tk.BooleanVar()
openport_var = tk.BooleanVar()
location_var = tk.BooleanVar()

# Checkboxes
cb1 = tk.Checkbutton(checkbox_frame, text="HTTP port add", font=("Arial", 14), variable=add_port_var, bg="black", fg="white", selectcolor="black")
cb1.pack(anchor="w")

cb2 = tk.Checkbutton(checkbox_frame, text="Directory finder", font=("Arial", 14), variable=autodirbuster_var, bg="black", fg="white", selectcolor="black")
cb2.pack(anchor="w")

cb3 = tk.Checkbutton(checkbox_frame, text="Taking screenshots", font=("Arial", 14), variable=gowitness_var, bg="black", fg="white", selectcolor="black")
cb3.pack(anchor="w")

cb4 = tk.Checkbutton(checkbox_frame, text="Technology Detection", font=("Arial", 14), variable=technology_var, bg="black", fg="white", selectcolor="black")
cb4.pack(anchor="w")

cb5 = tk.Checkbutton(checkbox_frame, text="Open Port Finder", font=("Arial", 14), variable=openport_var, bg="black", fg="white", selectcolor="black")
cb5.pack(anchor="w")

cb6 = tk.Checkbutton(checkbox_frame, text="Location Finder", font=("Arial", 14), variable=location_var, bg="black", fg="white", selectcolor="black")
cb6.pack(anchor="w")

# Run button
btn_run_selected = tk.Button(root, text="Run tool", font=("Arial", 16), command=run_selected_scripts, width=20)
btn_run_selected.pack(pady=20)

root.mainloop()
