import json

import jwt


def jwtUtils():
    payload = {'name': 'talker111'}
    token = jwt.encode(payload, 'tk123', algorithm='HS256')
    print(token)
    decoded_token = token.decode('utf-8')
    print(decoded_token)
    _payload = jwt.decode(token, key="tk123")
    print(_payload)


if __name__ == '__main__':
    jwtUtils()
