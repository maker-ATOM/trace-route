import subprocess


def traceroute(hostname):
    '''
    input: hostname/ip
    return: list ip hop
    '''
    print(f"Finding route to destination ({hostname})...")
    traceroute = subprocess.Popen(["traceroute", "-w 1", "-m 32", "-q 2",hostname],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ipList = []
    for line in iter(traceroute.stdout.readline, b""):
        line = line.decode("UTF-8")

        if not line.startswith(" "):
            continue

        ip_address = line.split()[1]
        ipList.append(ip_address)
    print("Routing Complete...")
    return ipList
