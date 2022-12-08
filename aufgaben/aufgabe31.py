import re

def pruefe_isbn(str):
    pat = r'^\d{3}[- ]\d[- ]\d{5}[- ]\d{3}[- ]\d$'

    if not re.match(pat, str):
        return False
    
    str = re.sub(r'[- ]', '', str)

    pziffer = int(str[12])
    pcheck = int(str[0]) + int(str[2]) + int(str[4]) + int(str[6]) + int(str[8]) + int(str[10]) + 3 * int(str[1]) + int(str[3]) + int(str[5]) + int(str[7]) + int(str[9]) + int(str[11])
    pcheck = (10 - pcheck%10)%10

    if pcheck != pziffer:
        return False

    return True

my_isbn = "978-3-86680-192-9"
print(my_isbn + ":", pruefe_isbn(my_isbn))