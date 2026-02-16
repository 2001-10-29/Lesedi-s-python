def secret_cipher(message, cipher):
    result = ""
    for char in message:
        if char in cipher:
            result += cipher[char]
        else:
            result += "?"
    return result

print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))
# 'p?m?ojm'
