import hashlib
import io

import humanhash
from pypdf import PdfReader
from requests import get

def dga():
    vorgang = get("https://search.dip.bundestag.de/api/v1/vorgangsposition/1?format=json&apikey=OSOegLs.PR2lwJ1dwCeje9vTj7FPOt3hvpYKtwKkhw")
    dokument = vorgang.json()["fundstelle"]["pdf_url"]
    on_fly_mem_obj = io.BytesIO(get(dokument).content)
    reader = PdfReader(on_fly_mem_obj)

    for page in reader.pages:
        text = page.extract_text()
        for line in text.split("\n"):
            h = hashlib.md5(line.encode()).hexdigest()
            domain = humanhash.humanize(h)
            yield domain
