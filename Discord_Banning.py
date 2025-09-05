import time
import random
import sys

# ---------------- CONFIG ----------------
bot_name = "BY JIN VAEL'THARION MOURNDUSK"
note = "Note: This bot is made by Jin Vael'Tharion Mourndusk"

# ---------------- COLORS ----------------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ---------------- ASCII HEADER ----------------
header = r"""
██████╗ ██╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗
██╔══██╗██║██╔═══██╗██╔══██╗██╔═══██╗████╗  ██║
██████╔╝██║██║   ██║██████╔╝██║   ██║██╔██╗ ██║
██╔═══╝ ██║██║   ██║██╔═══╝ ██║   ██║██║╚██╗██║
██║     ██║╚██████╔╝██║     ╚██████╔╝██║ ╚████║
╚═╝     ╚═╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═══╝
"""

# ---------------- INPUT ----------------
target_username = input(f"{CYAN}Enter the target username: {RESET}")
repeat_count = int(input(f"{CYAN}How many times to 'report'? {RESET}"))
delay_between_reports = float(input(f"{CYAN}Delay between reports (seconds, e.g., 1.5): {RESET}"))

# ---------------- UTILITY ----------------
def animate_progress(task_name, duration=1.5):
    bar_length = 30
    for i in range(bar_length + 1):
        percent = int(100 * i / bar_length)
        bar = "#" * i + "-" * (bar_length - i)
        sys.stdout.write(f"\r{task_name}: [{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print(" ✅")

def fake_report_id():
    return f"#{random.randint(1000,9999)}-{random.randint(100000,999999)}"

# ---------------- SIMULATION ----------------
print(RED + header + RESET)
print(GREEN + bot_name.center(60) + RESET)
print(f"\n{YELLOW}Starting reports on: {target_username}\n{RESET}")

for i in range(1, repeat_count + 1):
    report_id = fake_report_id()
    print(f"{CYAN}[{i}/{repeat_count}] Preparing report ID {report_id}...")
    animate_progress(f"{RED}Sending report", duration=2)
    print(f"{YELLOW}{note}\n{RESET}")
    time.sleep(delay_between_reports)

print(GREEN + "Simulation complete! All reports sent. The account will be banned after sometime.\n" + RESET)
