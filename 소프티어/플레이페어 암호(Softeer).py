def generate_key_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_table = []
    used_chars = set()

    for char in key:
        if char not in used_chars and char != 'J':
            key_table.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            key_table.append(char)
            used_chars.add(char)

    return [key_table[i:i+5] for i in range(0, 25, 5)]

def preprocess_message(message):
    processed = []
    i = 0

    while i < len(message):
        if i == len(message) - 1:
            processed.append(message[i] + 'X')
            break

        if message[i] == message[i+1]:
            if message[i] == 'X':
                processed.append(message[i] + 'Q')
            else:
                processed.append(message[i] + 'X')
            i += 1
        else:
            processed.append(message[i] + message[i+1])
            i += 2

    return processed

def find_position(char, key_table):
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == char:
                return row, col
    return None

def encrypt_pair(pair, key_table):
    row1, col1 = find_position(pair[0], key_table)
    row2, col2 = find_position(pair[1], key_table)

    if row1 == row2:
        return key_table[row1][(col1 + 1) % 5] + key_table[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return key_table[(row1 + 1) % 5][col1] + key_table[(row2 + 1) % 5][col2]
    else:
        return key_table[row1][col2] + key_table[row2][col1]

def playfair_cipher(message, key):
    key_table = generate_key_table(key)
    preprocessed_message = preprocess_message(message)
    encrypted_message = ""

    for pair in preprocessed_message:
        encrypted_message += encrypt_pair(pair, key_table)

    return encrypted_message

# Input
message = input().strip().replace("J", "I")
key = input().strip().replace("J", "I")

# Encrypt message
encrypted_message = playfair_cipher(message, key)
print(encrypted_message)
