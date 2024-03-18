import binascii

def decode_base_727(encoded_str):
    base_727 = 727
    decoded_str = ''
    
    for i in range(0, len(encoded_str), 3):
        chunk = (encoded_str[i:i+3], 16)
        decoded_str += chr(chunk)
    
    return decoded_str


encoded_hex_string = '06c3abc49dc4b443ca9d65c8b0c386c4b0c99fc798c2bdc5bccb94c68c37c296ca9ac29ac790c4af7bc585c59d'

# Декодирование из шестнадцатеричной строки
decoded_str = binascii.unhexlify(encoded_hex_string).decode()

# Декодирование из новой системы счисления с основанием 727
decoded_flag = decode_base_727(decoded_str)

print(decoded_flag)
