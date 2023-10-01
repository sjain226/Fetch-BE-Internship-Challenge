from flask import Flask, jsonify, request
app = Flask(__name__)
transactions = []
balances = {}

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    payer = data['payer']
    points = data['points']
    timestamp = data['timestamp']

    transactions.append({
        'payer': payer,
        'points': points,
        'timestamp': timestamp
    })
    balances[payer] = balances.get(payer, 0) + points
    return '', 200

@app.route('/spend', methods=['POST'])
def spend():
    data = request.json
    points_spent = data['points']
    result = []
    sort = sorted(transactions, key=lambda x: x['timestamp'])

    for transaction in sort:
        payer = transaction['payer']
        points = transaction['points']

        if points_spent <= 0:
            break

        if balances.get(payer, 0) >= 0:
            spent = min(points_spent, points)
            balances[payer] -= spent
            points_spent -= spent
            result.append({'payer': payer, 'points': -spent})

    if points_spent > 0:
        return 'User does not have enough points', 400

    return jsonify(result), 200

@app.route('/balance', methods=['GET'])
def balance():
    return jsonify(balances), 200


if __name__ == '__main__':
    app.run(port=8000)
