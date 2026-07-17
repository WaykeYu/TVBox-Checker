"""
validators.py

TVBox Checker
"""

from __future__ import annotations

import json
from xml.etree import ElementTree

###########################################################################

HTML_ERRORS = (

    "<html",

    "<!doctype",

    "404",

    "403",

    "forbidden",

    "access denied",

    "502",

    "503",

    "bad gateway",

    "cloudflare",

)

###########################################################################

def has_html_error(text: str) -> bool:

    if not text:
        return True

    t = text.lower()

    return any(err in t for err in HTML_ERRORS)

###########################################################################

def validate_json(text: str) -> bool:

    if has_html_error(text):
        return False

    try:

        obj = json.loads(text)

    except Exception:

        return False

    if isinstance(obj, dict):

        # TVBox 常見格式
        if "sites" in obj:
            return True

        if "spider" in obj:
            return True

        if "lives" in obj:
            return True

        if "parses" in obj:
            return True

    if isinstance(obj, list):

        return True

    return False

###########################################################################

def validate_xml(text: str) -> bool:

    if has_html_error(text):
        return False

    try:

        ElementTree.fromstring(text)

        return True

    except Exception:

        return False

###########################################################################

def validate_m3u(text: str) -> bool:

    if has_html_error(text):
        return False

    if "#EXTM3U" not in text.upper():

        return False

    return "#EXTINF" in text.upper()

###########################################################################

def validate_txt(text: str) -> bool:

    if has_html_error(text):
        return False

    lines = [

        x.strip()

        for x in text.splitlines()

        if x.strip()

    ]

    if len(lines) == 0:

        return False

    return True

###########################################################################

def validate(url: str, text: str) -> bool:

    u = url.lower()

    if u.endswith(".json"):

        return validate_json(text)

    if u.endswith(".xml"):

        return validate_xml(text)

    if u.endswith(".m3u"):

        return validate_m3u(text)

    if u.endswith(".txt"):

        return validate_txt(text)

    return not has_html_error(text)
