from ping3 import ping

def check_network_latency(host="8.8.8.8"):
    """
    Ping a given host and return latency in milliseconds.
    
    Args:
        host (str): Target host IP or domain to ping.
    Returns:
        float: Latency in milliseconds if reachable.
    Raises:
        Exception: If host is unreachable.
    """
    latency = ping(host, timeout=2)
    if latency:
        print(f"Latency to {host}: {latency*1000:.2f} ms")
        return latency * 1000
    else:
        raise Exception(f"Host {host} unreachable")

def verify_connection(host="8.8.8.8"):
    """
    Check if a host is reachable.
    
    Args:
        host (str): Target host IP or domain to ping.
    Returns:
        bool: True if reachable, False otherwise.
    """
    return ping(host, timeout=2) is not None
