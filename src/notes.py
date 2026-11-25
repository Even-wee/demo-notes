"""demo-notes: 读书笔记管理器（MVP）"""

import argparse
import sqlite3
from pathlib import Path

DB = Path.home() / ".demo-notes.db"


def init():
    with sqlite3.connect(DB) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS notes ("
            "id INTEGER PRIMARY KEY, text TEXT NOT NULL, tag TEXT, book TEXT)"
        )


def add(text: str, tag: str = "", book: str = ""):
    init()
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO notes (text, tag, book) VALUES (?, ?, ?)", (text, tag, book))
    print("已记录:", text)


def list_notes(tag: str = ""):
    init()
    sql = "SELECT id, text, tag FROM notes"
    args = ()
    if tag:
        sql += " WHERE tag = ?"
        args = (tag,)
    with sqlite3.connect(DB) as conn:
        for row in conn.execute(sql, args):
            print(f"[{row[0]}] {row[1]}  #{row[2]}")


def main():
    p = argparse.ArgumentParser(description="读书笔记小工具")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add")
    a.add_argument("text")
    a.add_argument("--tag", default="")
    a.add_argument("--book", default="")

    l = sub.add_parser("list")
    l.add_argument("--tag", default="")

    args = p.parse_args()
    if args.cmd == "add":
        add(args.text, args.tag, args.book)
    elif args.cmd == "list":
        list_notes(args.tag)


if __name__ == "__main__":
    main()
