"""
Enum for supported output formats in the CLI (csv, json, jsonl, table).
"""

from enum import Enum


class OutputFormat(str, Enum):
    csv = "csv"
    json = "json"
    jsonl = "jsonl"
    table = "table"
