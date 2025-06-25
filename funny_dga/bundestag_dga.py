import hashlib
import io
import time

import humanhash
from pypdf import PdfReader
from requests import get

def dga():
    retry = True
    while retry:
        try:
            on_fly_mem_obj = io.BytesIO(get("https://dserver.bundestag.de/btd/16/000/1600001.pdf").content)
            retry = False
        except:
            retry = True
            time.sleep(1)

    reader = PdfReader(on_fly_mem_obj)

    for page in reader.pages:
        text = page.extract_text()
        for line in text.split("\n"):
            h = hashlib.md5(line.encode()).hexdigest()
            domain = humanhash.humanize(h)
            yield domain
