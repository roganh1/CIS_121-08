"""Rogan Helm

2/11/22
"""


def main():
    encodedWord = "WBLARF8TTS"
    encodedWord = "L8KAOUL"
    encodedWord = "E8N8N8"
    encodedWord = "8TRA8DY T8LA"
    encodedWord = "8TT LHA TILLTA LIMAS"
    encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
    encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"

    # encodedWord = "UUHO"  # Used for Bonus
    # encodedWord = "EOUUUUOUU"  # Used for Bonus

    print(DecodeWord(encodedWord))


# Your code goes here.
def DecodeWord(encodedWord):
    decodedWord = ""
    dist = 8
    for ch in encodedWord:
        if ch == 'L':
            plainTxt = ord('T')
        elif ch == 'T':
            plainTxt = ord('L')
        elif ch == '8':
            plainTxt = ord('A')
        elif ch == 'B':
            plainTxt = ord('A')
        elif ch == 'A':
            plainTxt = ord('E')
        elif ch == 'E':
            plainTxt = ord('B')
        else:
            plainTxt = ord(ch)
        decodedWord += chr(plainTxt)
    return decodedWord


# This code triggers the main to run
# we'll talk about this more in chapters 6,7, & 8.
if __name__ == "__main__":
    main()
