letters = ["a", "b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w", "x" ,"y" ,"z" , "å", "ä", "ö"]

ord = input()

for x in ord:
    for y in letters:
        if y == x:
            letters.remove (x)

            



print (letters)