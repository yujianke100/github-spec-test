import sqlite3
from pathlib import Path


import random
import datetime
import numpy as np

DB_PATH = Path(__file__).parent / 'stocksite.db'
USER_NUM = 100
STOCK_NUM = 50
DAYS = 7
TRADES_PER_USER_PER_DAY = (1, 5)
PRICE_RANGE = (20, 200)
TIME_STEP_MIN = 5
STOCK_NAMES = [f'Stock{i+1}' for i in range(STOCK_NUM)]

def get_db_path():
    return DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)''')
    c.execute('''CREATE TABLE IF NOT EXISTS stocks (stock_id INTEGER PRIMARY KEY, name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS prices (id INTEGER PRIMARY KEY, stock_id INTEGER, time DATETIME, price REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS trades (id INTEGER PRIMARY KEY, user_id INTEGER, stock_id INTEGER, time DATETIME, type TEXT, volume INTEGER, price REAL)''')
    conn.commit()
    conn.close()

def generate_data():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # 清空表
    c.execute('DELETE FROM users')
    c.execute('DELETE FROM stocks')
    c.execute('DELETE FROM prices')
    c.execute('DELETE FROM trades')
    # 用户
    c.executemany('INSERT INTO users(user_id) VALUES (?)', [(i+1,) for i in range(USER_NUM)])
    # 股票
    c.executemany('INSERT INTO stocks(stock_id, name) VALUES (?, ?)', [(i+1, STOCK_NAMES[i]) for i in range(STOCK_NUM)])
    # 价格与买卖记录
    start_date = datetime.datetime.now() - datetime.timedelta(days=DAYS)
    for stock_id in range(1, STOCK_NUM+1):
        price = random.uniform(*PRICE_RANGE)
        times = [start_date + datetime.timedelta(minutes=TIME_STEP_MIN*i) for i in range((DAYS*24*60)//TIME_STEP_MIN)]
        for t in times:
            # 正态波动
            price *= np.exp(random.gauss(0, 0.01))
            price = max(price, 1)
            c.execute('INSERT INTO prices(stock_id, time, price) VALUES (?, ?, ?)', (stock_id, t, price))
    # 买卖记录
    for user_id in range(1, USER_NUM+1):
        for d in range(DAYS):
            day = start_date + datetime.timedelta(days=d)
            trade_count = random.randint(*TRADES_PER_USER_PER_DAY)
            for _ in range(trade_count):
                stock_id = random.randint(1, STOCK_NUM)
                t = day + datetime.timedelta(minutes=random.randint(0, 24*60-1))
                trade_type = random.choice(['buy', 'sell'])
                volume = random.randint(1, 100)
                # 取该时刻价格
                c.execute('SELECT price FROM prices WHERE stock_id=? AND time<=? ORDER BY time DESC LIMIT 1', (stock_id, t))
                row = c.fetchone()
                price = row[0] if row else random.uniform(*PRICE_RANGE)
                c.execute('INSERT INTO trades(user_id, stock_id, time, type, volume, price) VALUES (?, ?, ?, ?, ?, ?)',
                          (user_id, stock_id, t, trade_type, volume, price))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    generate_data()
    print('Database generated.')
