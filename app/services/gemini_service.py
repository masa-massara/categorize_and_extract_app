#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
gemini_service.py
"""

__author__ = 'Yoshikawa Masaya'
__version__ = '1.0.0'
__date__ = '2024/06/03 (Created: 2024/06/03)'

from config import Config

import json
import re

import google.generativeai as genai
from google.api_core.exceptions import InternalServerError, ResourceExhausted

gemini_api_key = Config.GEMINI_API_KEY

def extract_proper_nouns(text: str) -> dict:
    prompt = f"""
    次の入力テキストから固有名詞を抜き出し、必ず結果フォーマットの形で返してください。
    固有名詞がない場合は "proper_nouns" フィールドに null を返してください。

    入力テキスト: "{text}"
    
    結果フォーマット:
    {{
        "proper_nouns": ["固有名詞1", "固有名詞2", ...] もしくは null
    }}
    """

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-pro', generation_config={"response_mime_type": "application/json"})
    try:
        response = model.generate_content(prompt)
        # JSONの解析
        try:
            response_text = response.candidates[0].content.parts[0].text
            response_json = json.loads(response_text)
            return response_json
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            print(f"エラー: {e}")
            return {"proper_nouns": None}
    except ResourceExhausted as e:
        print(f"リソースが枯渇しました: {e}")
        return {"proper_nouns": None}
    except InternalServerError as e:
        print(f"サーバーエラー: {e}")
        return {"proper_nouns": None}
