import socket

import requests

from funny_dga.bundestag_dga import dga

for domain in dga():
    try:
        socket.getaddrinfo(domain + ".at", 80)
        requests.get("https://" + domain + ".at")
    except Exception as e:
        pass

    try:
        requests.get("https://europa.eu")
    except Exception as e:
        print(e)
        pass