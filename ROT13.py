def rot13ify(s):
    output = ""
    for c in s:
        if ord(c)>=65 and ord(c)<=90:
            output = output + chr((ord(c)-65+13)%26 + 65)
        elif ord(c)>=97 and ord(c)<=122:
            output = output + chr((ord(c)-97+13)%26 + 97)
        else:
            output = output + chr(ord(c))
    return output
            
print rot13ify("AAA")
