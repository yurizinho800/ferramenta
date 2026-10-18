import subprocess

def get_gateway_windows():
    result = subprocess.check_output("ipconfig", shell=True).decode("cp850")
    for line in result.splitlines():
        if "Gateway" in line:
            print("\033[92m" + line.strip() + "\033[0m")




