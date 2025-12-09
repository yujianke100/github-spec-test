from flask import Flask
from api import bp as api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(debug=True)
