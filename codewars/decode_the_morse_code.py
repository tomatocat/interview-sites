#https://www.codewars.com/kata/54b724efac3d5402db00065e

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    string = ''
    word = ''
    spaces = 0
    for char in morse_code:
        if char != ' ':
        #add char component
            if spaces == 1 and word != '':
            #add and lookup word to string, reset word
                string = string + MORSE_CODE[word]
                word = char
            elif spaces == 3 and word != '':
            #add space to string
                string = string + MORSE_CODE[word] + ' '
                word = char
            else:
            #add char to word
                word = word + char
            spaces = 0
        else:
            spaces = spaces + 1
    if word == '':
        return string
    else:
        return string + MORSE_CODE[word]
