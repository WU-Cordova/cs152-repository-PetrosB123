

def starstring(string):
    result = ""
    star = 0
    while string != "":
        if string[-1] == "*":
            string = string[0: -1]
            star += 1
        else:
            result += (string[-1])
            string = string[0: -1]

    return result

print(starstring("*h**e**ll*o"))