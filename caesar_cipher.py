txt=input("Enter text  :")
shift=int(input("Enter shift value:"))
cipher=""
for ch in txt:
    ordinal=ord(ch)+shift
    if(ordinal>=ord('z')):
        ordinal=ordinal-26
    cipher+=chr(ordinal)
print(f"Cipher text:{cipher}")

#decode
txt=''
for ch in cipher:
    ordinal=ord(ch)-shift
    if(ordinal<ord('a')):
        ordinal=ordinal+26
    txt+=chr(ordinal)
print(f"Decoded text:{txt}")
