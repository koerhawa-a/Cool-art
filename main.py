# Coolest art entry: a fire phoenix over the ruined city, Japanese style.
# Burning orange wings against a blackened city under a dark sky.
# The art ships as base64 text (entry.png.b64) and is decoded to the
# output directory, byte for byte.
import base64
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png.b64")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

with open(SRC, "r", encoding="ascii") as f:
    data = base64.b64decode(f.read())

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "wb") as f:
    f.write(data)
