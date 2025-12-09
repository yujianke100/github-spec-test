from flask import Blueprint, request, jsonify
import sqlite3
from pathlib import Path
from datetime import datetime

bp = Blueprint('api', __name__)
DB_PATH = Path(__file__).parent / 'stocksite.db'

def get_conn():
    return sqlite3.connect(DB_PATH)

@bp.route('/api/stocks', methods=['GET'])
def get_stocks():
    conn = get_conn()
    c = conn.cursor()
    c.execute('SELECT stock_id, name FROM stocks')
    stocks = [{'stock_id': row[0], 'name': row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(stocks)

@bp.route('/api/query', methods=['POST'])
def query_stats():
    data = request.get_json()
    stock_id = data.get('stock_id')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    if not (stock_id and start_time and end_time):
        return jsonify({'error': '参数缺失'}), 400
    conn = get_conn()
    c = conn.cursor()
    # 价格曲线
    c.execute('SELECT time, price FROM prices WHERE stock_id=? AND time BETWEEN ? AND ? ORDER BY time',
              (stock_id, start_time, end_time))
    prices = [{'time': row[0], 'price': row[1]} for row in c.fetchall()]
    # 买卖量
    c.execute('''SELECT time, \
        SUM(CASE WHEN type='buy' THEN volume ELSE 0 END) as buy_volume, \
        SUM(CASE WHEN type='sell' THEN volume ELSE 0 END) as sell_volume \
        FROM trades WHERE stock_id=? AND time BETWEEN ? AND ? GROUP BY time ORDER BY time''',
        (stock_id, start_time, end_time))
    volumes = [{'time': row[0], 'buy_volume': row[1] or 0, 'sell_volume': row[2] or 0} for row in c.fetchall()]
    # 盈亏
    c.execute('''SELECT SUM(CASE WHEN type='buy' THEN volume*price ELSE 0 END), \
                       SUM(CASE WHEN type='sell' THEN volume*price ELSE 0 END) \
                FROM trades WHERE stock_id=? AND time BETWEEN ? AND ?''',
              (stock_id, start_time, end_time))
    row = c.fetchone()
    total_buy = row[0] or 0
    total_sell = row[1] or 0
    pnl = {'total_buy': total_buy, 'total_sell': total_sell, 'net_profit': total_sell - total_buy}
    conn.close()
    return jsonify({'prices': prices, 'volumes': volumes, 'pnl': pnl})
