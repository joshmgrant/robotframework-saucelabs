# -*- coding: utf-8 -*-
from .plugin import SauceLabs
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

__all__ = ["SauceLabs"]