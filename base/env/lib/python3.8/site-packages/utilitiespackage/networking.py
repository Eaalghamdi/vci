import subprocess


def get_primary_address():
    data = subprocess.check_output(["ip", "addr"])
    lines = data.split("\n")

    ip_address_candidates = []
    for line in lines:
        line = line.lstrip()
        line = line.rstrip()
        if "inet " in line:
            ip = line.split(" ")[1].split("/")[0]
            if not ip.startswith("127") and not ip.startswith("10") and not ip.startswith("192.168"):
                ip_address_candidates.append(ip)

    if "172.28.128.1" in ip_address_candidates:
        return "172.28.128.1"

    if "172.28.128.128" in ip_address_candidates:
        return "172.28.128.128"

    if len(ip_address_candidates):
        return ip_address_candidates[0]
