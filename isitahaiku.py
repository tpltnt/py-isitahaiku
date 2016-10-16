#!/usr/bin/env python3
"""
An abstraction of isitahaiku.com for Python.
"""
import requests

def isHaiku(text):
    """
    :param text: text to check
    :type text: str
    :returns: bool
    :raises: RuntimeError (if scraper fails)
    """
    payload = {'haiku': text}
    r = requests.post('http://isitahaiku.com/',
                      data=payload)
    if 200 != r.status_code:
        raise RuntimeError('POST request failed')
    if '(No)' in r.text:
        r.close()
        return False
    if '(Yes)' in r.text:
        r.close()
        return True
    r.close()
    raise RuntimeError('website changed, code needs to be adjusted')
