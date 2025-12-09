import os
import sys
import sqlite3
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend import db

def test_db_schema():
    db.init_db()
    conn = sqlite3.connect(db.get_db_path())
    c = conn.cursor()
    # 检查表是否存在
    for table in ['users', 'stocks', 'prices', 'trades']:
        c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        assert c.fetchone(), f"Table {table} not found"
    conn.close()

def test_generate_data():
    db.generate_data()
    conn = sqlite3.connect(db.get_db_path())
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users')
    assert c.fetchone()[0] == db.USER_NUM
    c.execute('SELECT COUNT(*) FROM stocks')
    assert c.fetchone()[0] == db.STOCK_NUM
    c.execute('SELECT COUNT(*) FROM prices')
    assert c.fetchone()[0] > 0
    c.execute('SELECT COUNT(*) FROM trades')
    assert c.fetchone()[0] > 0
    conn.close()
