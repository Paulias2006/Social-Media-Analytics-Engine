from __future__ import annotations

import sqlite3
from pathlib import Path


def create_database(db_path: Path, posts: list[dict[str, object]]) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()

    with sqlite3.connect(db_path) as conn:
        columns = list(posts[0].keys())
        conn.execute(f"CREATE TABLE posts ({', '.join(column + ' TEXT' for column in columns)})")
        conn.executemany(
            f"INSERT INTO posts ({', '.join(columns)}) VALUES ({', '.join('?' for _ in columns)})",
            [[row[column] for column in columns] for row in posts],
        )
        conn.commit()


def query_dicts(db_path: Path, sql: str) -> list[dict[str, object]]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        return [dict(row) for row in conn.execute(sql)]
