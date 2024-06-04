#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
gemini_service.py
"""

__author__ = "Yoshikawa Masaya"
__version__ = "1.0.0"
__date__ = "2024/06/03 (Created: 2024/06/03)"

"""
test_extract.py
"""

import sys
import os
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from app.main import app

client = TestClient(app)


def test_extract_proper_nouns():
    """
    正常な文章を送信して固有名詞を抽出するテスト
    """
    response = client.get("/extract?text=ジョンは東京に行きました")
    assert response.status_code == 200
    json_response = response.json()
    assert "proper_nouns" in json_response
    assert json_response["proper_nouns"] == ["ジョン", "東京"]


def test_extract_proper_nouns_no_text():
    """
    空の文章を送信してエラーレスポンスを受け取るテスト
    """
    response = client.get("/extract?text=")
    assert response.status_code == 400
    json_response = response.json()
    assert json_response == {"detail": "Text is required"}


def test_extract_proper_nouns_missing_param():
    """
    `text` クエリパラメータを欠如させたリクエストを送信してエラーレスポンスを受け取るテスト
    """
    response = client.get("/extract")
    assert response.status_code == 422
    json_response = response.json()
    assert "detail" in json_response
