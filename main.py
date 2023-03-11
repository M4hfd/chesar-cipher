message = input("Введите фразу: ")
cipher = []
step = int(input("Введите шаг сдвига: "))
ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

for symbol in message.lower():
    message_index = ALPHABET_RU.find(symbol)
    message_index += step
    cipher.append(ALPHABET_RU[message_index])

cipher_string = ''.join(cipher)
print("Шифр: " + cipher_string)

result = ''
for symbol in cipher_string:
    symbol_index = ALPHABET_RU.find(symbol)
    message_index = (symbol_index - step)
    result += ALPHABET_RU[message_index]

print("Расшифрованная фраза: ", result)
