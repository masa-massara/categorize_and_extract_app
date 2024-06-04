#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
extract.py
"""

__author__ = "Yoshikawa Masaya"
__version__ = "1.0.0"
__date__ = "2024/06/03 (Created: 2024/06/03)"

from fastapi import APIRouter, HTTPException, Query
from services.gemini_service import extract_proper_nouns

router = APIRouter()


@router.get("/extract")
async def extract_proper_nouns_route(
    text: str = Query(..., description="Text to extract proper nouns from")
):
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    proper_nouns = extract_proper_nouns(text)
    return proper_nouns


# # テスト用に画面にOKと表示されるだけのルートを追加
# @router.get("/health")
# async def health_check():
#     return {"status": "OK"}
