from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# DİKKAT: İçeride "keycloak:8080" şeklinde kullanıyoruz.
# Çünkü docker-compose içindeki Keycloak servisine
# "keycloak" adıyla erişebiliyoruz.
KEYCLOAK_TOKEN_URL = "http://192.168.1.105:8080/realms/myrealm/protocol/openid-connect/token"
CLIENT_ID = "test"        # Keycloak Client Name
CLIENT_SECRET = "jbLcQbTveQUqNWqoAKjBP0kLzzq2P30I"    # Keycloak'ta oluşturduğunuz client'ın secret değeri

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    data = {
        "grant_type": "password",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "username": username,
        "password": password
    }

    response = requests.post(KEYCLOAK_TOKEN_URL, data=data)
    if response.status_code == 200:
        token_data = response.json()
        return jsonify({
            "access_token": token_data.get("access_token"),
            "refresh_token": token_data.get("refresh_token"),
            "expires_in": token_data.get("expires_in")
        }), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    # 0.0.0.0'a bağlanıp 5000 portunu dinliyoruz
    app.run(host="0.0.0.0", port=5000)
