import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_stocks(client):
    resp = client.get('/api/stocks')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert all('stock_id' in s and 'name' in s for s in data)

def test_query_stats(client):
    # 取一只股票和时间范围
    stocks = client.get('/api/stocks').get_json()
    if not stocks:
        pytest.skip('No stocks in db')
    stock_id = stocks[0]['stock_id']
    # 查询所有价格时间范围
    import sqlite3
    from backend import db
    conn = sqlite3.connect(db.get_db_path())
    c = conn.cursor()
    c.execute('SELECT MIN(time), MAX(time) FROM prices WHERE stock_id=?', (stock_id,))
    row = c.fetchone()
    conn.close()
    if not row or not row[0] or not row[1]:
        pytest.skip('No price data')
    start_time, end_time = row
    resp = client.post('/api/query', json={
        'stock_id': stock_id,
        'start_time': start_time,
        'end_time': end_time
    })
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'prices' in data and 'volumes' in data and 'pnl' in data
