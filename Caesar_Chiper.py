def encrypt(plaintext, shift):
    enctext=""
    for x in plaintext:
       plainasciival=ord(x)
       enctext=enctext+(chr((plainasciival+shift)%256))
    return enctext 

def decrypt(ciphertext, shift):
    dectext=""
    for x in ciphertext:
       cipherasciival=ord(x)
       dectext=dectext+(chr((cipherasciival-shift)%256))
    return dectext

if __name__=="__main__":
    messagetext=input("Enter Message to be encrypted: ")
    shiftvalue=int(input("Enter Shift value to encrypt with: "))
    ciphertext=encrypt(messagetext,shiftvalue)
    print("Encrypted Text: ",ciphertext)
    decrypted_text=decrypt(ciphertext,shiftvalue)
    print("Decrypted Text:", decrypted_text)
