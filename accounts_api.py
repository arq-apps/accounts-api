from flask import Flask, request, jsonify
from bank_auth_sdk import BankAuth

app = Flask(__name__)
auth = BankAuth("accounts")

@app.route('/balance', methods=['GET'])
def balance():
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return jsonify({
            "error": "Token faltante o malformado en el header Authorization. Se espera 'Bearer <token>'"
        }), 401

    token = auth_header.replace('Bearer ', '')
    issuer = request.headers.get('X-Token-Issuer')
    if not issuer:
        return jsonify({
            "error": "Falta el header X-Token-Issuer para determinar quién firmó el token"
        }), 400

    try:
        auth.verify_token(token, issuer_app_name=issuer)
        # Simulamos una respuesta de balance de cuenta
        return jsonify({
            "status": "success",
            "api": "accounts",
            "balance": {
                "currency": "ARS",
                "available": 132500.50,
                "last_updated": "2025-05-06T21:15:00Z"
            }
        })
    except ValueError as e:
        return jsonify({"error": f"Token inválido o expirado: {str(e)}"}), 403
    except Exception as e:
        return jsonify({"error": f"Error interno al verificar el token: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
