#Ronuel Diaz
#Assignment 2
#Programming Language
#4/4/17
# Encryption/Decryption


global n
global phi
global d
p=2917
q=2239
n=p*q
phi=(p-1)*(q-1)
e=2243 #public
d=5819 #private 


print("Your public key is: ",n,e)

def Encryption(text,n1,e1):
    text_buf = [ord(c) for c in text]
    text_buf1 = [(m**e1)%n1 for m in text_buf]
    print ("this is the cypher:" , text_buf1)
    return text_buf1


def Decryption(text):
    global d
    global n
    text_buf =[(x**d)%n for x in text]
    print(''.join(chr(c)for c in text_buf))

    

