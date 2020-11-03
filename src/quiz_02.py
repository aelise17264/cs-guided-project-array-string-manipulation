from string import ascii_letters

def alphabeticShift(inputString):
    new_string = ''
    for char in inputString:
        if char in ascii_letters:
            new_string = new_string + ascii_letters[(ascii_letters.index(char)+1)%len(ascii_letters)]
        else:
            new_string += char
    return new_string.lower()

print(alphabeticShift("crazy"))
print(alphabeticShift("anna"))