from enum import Enum


class OutputFormat(str, Enum):
    csv = "csv"
    json = "json"
    jsonl = "jsonl"
    table = "table"
