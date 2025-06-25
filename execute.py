import requests

from funny_dga.bundestag_dga import dga

for domain in dga():
    try:
        requests.get("https://" + domain + ".at")
    except:
        pass