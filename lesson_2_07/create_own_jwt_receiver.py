import jwt

headers = {
    'alg': 'HS256',
    'type': 'JWT'
}

payload = {
    'username': 'tester_user',
    'email': 'tester@gmail.com',
    'is_active': False
}

secret = 'secret_123'

encoded_token = jwt.encode(headers=headers, payload=payload, key=secret)
print(f"encoded_token: {encoded_token}")

try:
    decoded_token = jwt.decode(encoded_token, secret, algorithms=['HS256'])
    print(f"decoded_token: {decoded_token}")
except jwt.InvalidTokenError:
    print('Invalid Token')
except jwt.DecodeError:
    print('Decode error')

