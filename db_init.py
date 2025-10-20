#!/usr/bin/env python3

import os
import sqlite3


def set_wal_mode(db_path):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.close()


def db_init_users():
    db_path = "db_users.sqlite"
    users = [("admin", "SuperSecret"), ("elliot", "123123123"), ("tim", "12345678")]
    set_wal_mode(db_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE users (username text, password text, failures int, mfa_enabled int, mfa_secret text)"
    )

    for u, p in users:
        c.execute(
            "INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES ('%s', '%s', '%d', '%d', '%s')"
            % (u, p, 0, 0, "")
        )

    conn.commit()
    conn.close()


def db_init_posts():
    db_path = "db_posts.sqlite"
    set_wal_mode(db_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE posts (date date, username text, text text)")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    try:
        os.remove("db_users.sqlite")
    except FileNotFoundError:
        pass

    try:
        os.remove("db_posts.sqlite")
    except FileNotFoundError:
        pass
    db_init_users()
    db_init_posts()
