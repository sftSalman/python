def minion_game(string):
    s = len(string)
    vow = 0
    cons = 0
    for i in range(s):
        if string[i] in 'AEIOU':
            vow = vow+(s-i)
        else:
            cons=cons+(s-i)
    if vow<cons:
        print('Stuart ' + str(cons))
    elif vow>cons:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')
minion_game('BANANA')