import secrets


def generate_key(nbytes):
    return secrets.token_hex(nbytes)


print(generate_key(16))
