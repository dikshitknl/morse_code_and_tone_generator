import winsound as s
from time import sleep
moarse = {' ':' ','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'--.-','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..'}
while(1):
    string = raw_input("Input string to be converted:").lower()
    for i in range(0,len(string)):
        ch = string[i]
        temp = moarse[ch]
        for j in range(0,len(temp)):
            if temp[j]=='.':
                s.Beep(1000,100)
            elif temp[j]=='-':
                s.Beep(1000,300)
            else:
                sleep(0.5)
            sleep(0.5)
        print ch,"(",temp,")"
        sleep(0.5)
