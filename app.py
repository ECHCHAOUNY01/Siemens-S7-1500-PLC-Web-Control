# app.py
from flask import Flask, jsonify, request
from plc import SiemensPlc
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
plc = SiemensPlc()

@app.route('/connect')
def connect():
    return jsonify({"status": plc.connect()})

@app.route('/read', methods=['GET'])
def read():
    try:
        db = int(request.args.get('db'))
        start = int(request.args.get('start'))
        byte = int(request.args.get('byte'))
        bit = int(request.args.get('bit'))
        value = plc.read_bool(db, start, byte, bit)
        return jsonify({'value': value})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/write', methods=['POST'])
def write():
    try:
        data = request.json
        db = data['db']
        start = data['start']
        byte = data['byte']
        bit = data['bit']
        value = data['value']
        plc.write_bool(db, start, byte, bit, value)
        return jsonify({'status': 'written', 'value': value})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
