from flask import Flask, jsonify, request
app = Flask(__name__)
transactions = []
balances = {}

@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.json
        payer = data['payer']
        points = data['points']
        timestamp = data['timestamp']

        if not points or not payer or not timestamp:
            return jsonify({"error" : "Invalid request data, check request body"}), 400

        if points<0:
            return jsonify({"error" : "Points must be greater than 0"}), 400

        transactions.append({
            'payer': payer,
            'points': points,
            'timestamp': timestamp
        })
        balances[payer] = balances.get(payer, 0) + points
        return '', 200
    
    except Exception as e:
        return jsonify({"error": stre(e)}), 500

@app.route('/spend', methods=['POST'])
def spend():
    try:
        data = request.json
        points_to_spend = data['points']
        result = []
        total_balance = 0
        sort = sorted(transactions, key=lambda x: x['timestamp'])

        for transaction in sort:
            total_balance += transaction['points']

        if total_balance < points_to_spend:
            return jsonify({"error" : "User does not have enough points"}), 400

        for transaction in sort:
            payer = transaction['payer']
            points = transaction['points']

            if points_to_spend == 0:
                break

            if balances.get(payer, 0) > 0:
                spent = min(points_to_spend, points)
                balances[payer] -= spent
                points_to_spend -= spent
                result.append({'payer': payer, 'points': -spent})

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error" : stre(e)}), 500

@app.route('/balance', methods=['GET'])
def balance():
    try:
        return jsonify(balances), 200

    except Exception as e:
        return jsonify({"error" : stre(e)}), 500



if __name__ == '__main__':
    app.run(port=8000)
