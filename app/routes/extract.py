#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
extract.py
"""

__author__ = "Yoshikawa Masaya"
__version__ = "1.0.0"
__date__ = "2024/06/03 (Created: 2024/06/03)"

from fastapi import APIRouter, HTTPException, Query
from services.gemini_service import GeminiService

router = APIRouter()
gemini = GeminiService()


@router.get("/extract")
async def extract_proper_nouns_route(
    text: str = Query(..., description="Text to extract proper nouns from")
):
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    proper_nouns = gemini.extract_proper_nouns(text)
    return proper_nouns


@router.get("/categorize")
async def categorize_route(
    text: str = Query(..., description="Text to categorize sentence meaning from")
):
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    proper_nouns = gemini.categorize_sentence_meaning(text)
    return proper_nouns


@router.get("/extract-and-categorize")
async def extract_and_categorize_route(
    text: str = Query(
        ...,
        description="Text to extract proper nouns and categorize sentence meaning from",
    )
):
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    proper_nouns = gemini.extract_and_categorize(text)
    return proper_nouns


# # テスト用に画面にOKと表示されるだけのルートを追加
# @router.get("/health")
# async def health_check():
#     return {"status": "OK"}
