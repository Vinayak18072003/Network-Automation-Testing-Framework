from ping3 import ping

def check_network_latency(host="8.8.8.8"):
    """Ping a host and return latency in ms."""
    latency = ping(host, timeout=2)
    if latency:
        print(f"Latency to {host}: {latency*1000:.2f} ms")
        return latency * 1000
    else:
        raise Exception(f"Host {host} unreachable")

def verify_connection(host="8.8.8.8"):
    """Return True if host reachable, False otherwise."""
    return ping(host, timeout=2) is not None
