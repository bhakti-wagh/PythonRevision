s='bacbcaabbaa'

def fun(s):
    x=""

    for ch in s:

        if ch not in x:
            x= x+ch+str(s.count(ch))

    return x


print(fun(s))
        

