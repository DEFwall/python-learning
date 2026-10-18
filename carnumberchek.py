s = input()
count = 0

if len(s) != 9 and len(s) != 10:
    print('NO')
    exit()

else:
    if len(s) < 9:
        print('NO')

    if s[0] in 'АВЕКМНОРСТУХ':
        count += 1
    
    choce1 = s[1]
    choce2 = s[2]
    choce3 = s[3]

    if choce1.isdigit() == True and choce2.isdigit() == True and choce3.isdigit() == True:
        count += 1
    
    if s[4] in 'АВЕКМНОРСТУХ' and s[5] in 'АВЕКМНОРСТУХ':
        count += 1
    
    if s[6] in '_':
        count += 1
    
    chose4 = s[7]
    chose5 = s[8]

    if len(s) == 9:
        if chose4.isdigit() == True and chose5.isdigit() == True:
            count += 1
        
    if len(s) == 10:
        chose6 = s[9]
        if chose4.isdigit() == True and chose5.isdigit() == True and chose6.isdigit() == True:
            count += 1
    
    if len(s) == 9 or len(s) == 10:
        count += 1
    
    if count == 6:
        print('YES')
    else:
        print('NO')
