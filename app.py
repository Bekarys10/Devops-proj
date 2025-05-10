from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    data = [
        {'location': 'New York', 'temperature': '22°C', 'condition': 'Sunny'},
        {'location': 'London', 'temperature': '18°C', 'condition': 'Cloudy'},
        {'location': 'Tokyo', 'temperature': '26°C', 'condition': 'Rainy'}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
