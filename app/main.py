#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
main.py
"""

__author__ = 'Yoshikawa Masaya'
__version__ = '1.0.0'
__date__ = '2024/06/03 (Created: 2024/06/03)'

from fastapi import FastAPI
from routes.extract import router as extract_router

app = FastAPI()

app.include_router(extract_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
