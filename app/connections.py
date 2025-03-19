import psutil
import socket
from tabulate import tabulate

def get_active_connections():
    connections = []
    
    for conn in psutil.net_connections(kind='inet'):
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        status = conn.status
        protocol = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"

        connections.append([laddr, raddr, protocol, status])

    return connections

if __name__ == "__main__":
    conn_list = get_active_connections()
    
    headers = ["Local Address", "Remote Address", "Protocol", "Status"]
    print(tabulate(conn_list, headers=headers, tablefmt="grid"))

