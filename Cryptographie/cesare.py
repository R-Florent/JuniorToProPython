code = "SyberagRfgYrCyhfOrnhMmMNnN"

def caesar_cipher(chaine):
    ascii_chaine = [ord(c) for c in chaine]
    print("Le code ASCII est :", ascii_chaine)

    for i in range(1, 27):
        result = []
        for c in chaine:
            if 'a' <= c <= 'z':
                result.append(chr((ord(c) - ord('a') + i) % 26 + ord('a')))
            elif 'A' <= c <= 'Z':
                result.append(chr((ord(c) - ord('A') + i) % 26 + ord('A')))

        result_chaine = ''.join(result)
        print(f"La phrase avec un décalage de {i} est : {result_chaine}")


print("Code ASCII de 'a' :", ord("a"))
print("Code ASCII de 'z' :", ord("z"))
print("Code ASCII de 'A' :", ord("A"))
print("Code ASCII de 'Z' :", ord("Z"))

caesar_cipher(code)