def flipflop(tup):
    s = 0
    e = len(tup) - 1
    while (s < e):
        if (tup[s] != tup[e]):
            return False
        
        s += 1
        e -= 1

    return True

tuplex = (1, 2, 3, 3, 2, 1)

if(flipflop(tuplex)):
    print("This tuple is flip-flop")

else:
    print("This tuple is not flip-flop")