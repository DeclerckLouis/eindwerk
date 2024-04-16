from flask import Flask, request, abort
import hmac
import hashlib

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Your secret key (this should be kept private)
    secret_key = b'your-secret-key'

    # Extract the signature from the 'X-Signature' header
    signature = request.headers.get('X-Signature')

    if signature is None:
        # No signature provided in the request
        abort(403)

    # Calculate the HMAC of the raw body using the secret key
    calculated_signature = hmac.new(secret_key, request.data, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(signature, calculated_signature):
        # The calculated HMAC does not match the one sent in the request
        abort(403)

    # If we reach this point, the request is valid
    print('Received valid webhook')
    return '', 200

if __name__ == '__main__':
    # Run the app with SSL encryption using your own certificates and on port 5000
    app.run(host='0.0.0.0', port=5000, ssl_context=('../certs/test.crt', '../certs/test.key'))