#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
config.py
"""

__author__ = 'Yoshikawa Masaya'
__version__ = '1.0.0'
__date__ = '2024/06/03 (Created: 2024/06/03)'

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
