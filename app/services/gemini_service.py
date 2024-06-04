#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
gemini_service.py
"""

__author__ = "Yoshikawa Masaya"
__version__ = "1.0.0"
__date__ = "2024/06/03 (Created: 2024/06/03)"

from config import Config

import json
import re

import google.generativeai as genai
from google.api_core.exceptions import InternalServerError, ResourceExhausted


class GeminiService:
    """
    Gemini APIを利用して、入力テキストから固有名詞を抽出したり文章をカテゴライズするクラス
    """

    def __init__(self):
        self.gemini_api_key = Config.GEMINI_API_KEY

    def _config_model(self):
        genai.configure(api_key=self.gemini_api_key)
        model = genai.GenerativeModel(
            "gemini-1.5-pro",
            generation_config={"response_mime_type": "application/json"},
        )
        return model

    def _fetch_response(self, prompt: str):
        model = self._config_model()
        try:
            response = model.generate_content(prompt)
            response_text = response.candidates[0].content.parts[0].text
            response_json = json.loads(response_text)
            return response_json
        except ResourceExhausted as e:
            print(f"リソースが枯渇しました: {e}")
            return None
        except InternalServerError as e:
            print(f"サーバーエラー: {e}")
            return None

    def extract_proper_nouns(self, text: str) -> dict:
        prompt = f"""
        次の入力テキストから固有名詞を抜き出し、必ず結果フォーマットの形で返してください。
        固有名詞がない場合は "proper_nouns" フィールドに null を返してください。

        入力テキスト: "{text}"
        
        結果フォーマット:
        {{
            "proper_nouns": ["固有名詞1", "固有名詞2", ...] もしくは null
        }}
        """

        response = self._fetch_response(prompt)
        return response

    def categorize_sentence_meaning(self, text: str) -> dict:
        prompt = f"""
        次の入力テキストの意味をenumの中から最も当てはまるものを選びフォーマットの形で返してください。

        入力テキスト: "{text}"

        "enum": [
                "雰囲気の質問",
                "共感",
                "場所の質問",
                "否定",
                "感謝",
                "食事の質問",
                "方法・手段の質問",
                "要望",
                "意味なし",
                ]
        
        結果フォーマット:
        {{
            "category": "カテゴリ名"
        }}
        """

        response = self._fetch_response(prompt)
        print("responseを返すよう: ", response)
        return response

    def extract_and_categorize(self, text: str) -> dict:
        prompt = f"""
        次の入力テキストから固有名詞と文章の意味をenumの中から最も当てはまるものを選びフォーマットの形で返してください。
        固有名詞がない場合は "proper_nouns" フィールドに null を返してください。

        入力テキスト: "{text}"
        "enum": [
                "雰囲気の質問",
                "共感",
                "場所の質問",
                "否定",
                "感謝",
                "食事の質問",
                "方法・手段の質問",
                "要望",
                "意味なし",
                ]
        
        結果フォーマット:
        {{
            "proper_nouns": ["固有名詞1", "固有名詞2", ...] もしくは null
            "category": "カテゴリ名"
        }}
        """

        response = self._fetch_response(prompt)
        return response
