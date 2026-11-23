"""
Encoding and obfuscation variants for generated payloads.
Each encoder takes a raw payload string and returns a transformed string.
"""

import base64
import urllib.parse


def encode_raw(payload: str) -> str:
    return payload


def encode_url(payload: str) -> str:
    return urllib.parse.quote(payload, safe="")


def encode_html_entities(payload: str) -> str:
    return "".join(f"&#{ord(c)};" for c in payload)


def encode_base64(payload: str) -> str:
    encoded = base64.b64encode(payload.encode()).decode()
    return f"eval(atob('{encoded}'))"


def encode_hex(payload: str) -> str:
    return "".join(f"\\x{ord(c):02x}" for c in payload)


ENCODERS = {
    "raw": encode_raw,
    "url": encode_url,
    "html": encode_html_entities,
    "base64": encode_base64,
    "hex": encode_hex,
}
