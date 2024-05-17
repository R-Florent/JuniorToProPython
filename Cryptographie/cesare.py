code = "FaxvrjtTbxYaPadwOaajIdMWaP"
cle = [0, 15, 9, 4, 13, 100]
reversed_key = [26- e for e in cle ]#

def caesar_cipher_key(chaine, key):
    ascii_chaine = [ord(c) for c in chaine]
    print("Le code ASCII est :", ascii_chaine)
    result_chaine = ""
    result = []
    for i in range(len(chaine)):

        if 'a' <= chaine[i] <= 'z':
            result.append(chr((ord(chaine[i]) - ord('a') + key[i%len(key)]) % 26 + ord('a')))
        elif 'A' <= chaine[i] <= 'Z':
            result.append(chr((ord(chaine[i]) - ord('A') + key[i%len(key)]) % 26 + ord('A')))
    result_chaine = ''.join(result)

    print("le result est :", result_chaine)


caesar_cipher_key(code, reversed_key)
