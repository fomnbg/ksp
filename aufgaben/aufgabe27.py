import re

string = input("String eingeben: ")

pattern = [
    "Michael",
    "^Michael",
    "Michael$",
    "[Mm]ichael",
    "[ \t]"
    "[ \t]+\n",
    "[a-z0-9<>_]",
    "[0-9+\-]",
    "[^a-zA-Z]",
    "ab?c",
    "[aeiu]da",
    ".da",
    "^$",
    "^...$"
]

i=0

for pat in pattern:
    
    i=i+1
    print(str(i)+". Checking for: ", pat)
    
    if re.search(pat, string):
        print(pat, "erkannt!\n")