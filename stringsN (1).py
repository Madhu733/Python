def Upper(string):
    n=""
    for i in string:
        y=ord(i)
        if y>=97 and y<=122:
            n+=chr(y-32)
        else:
            n+=i
    return n

def Lower(string):
    n=""
    for i in s:
        y=ord(i)
        if y>=65 and y<=90:
            n+=chr(y+32)
        else:
            n+=i
    return n

def Capital(s):
    n=""
    for i in range(len(s)):
        y=ord(s[i])
        if i==0 and y>=65 and y<=90:
            n+=s[i]
        elif i==0 and y>=97 and y<=122:
            n+=chr(y-32)
        else:
            if y>=65 and y<=90:
                n+=chr(y+32)
            else:
                n+=s[i]
    return n

def Swapcase(s):
    n=""
    for x in s:
        if ord(x)>=65 and ord(x)<=90:
            n+=chr(ord(x)+32)
        elif ord(x)>=97 and ord(x)<=122:
            n+=chr(ord(x)-32)
        else:
            n+=x
    return n

def isalpha1(a):
    n=0
    for i in a:
        if ord(i)>=65 and ord(i)<=122:
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False


def isdigit1(a):
    n=0
    for i in a:
        if ord(i)>=33 and ord(i)<=64:
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False
    
def isalnum1(an):
    n=0
    for i in an:
        if ord(i)>=65 and ord(i)<=90 or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
            n+=1
        else:
            continue
    if n==len(an):
        return True
    else:
        return False
    
    
def isdigit1(d):
    n=0
    for i in d:
        if ord(i)>=33 and ord(i)<=64:
            n+=1
        else:
            continue
    if n==len(d):
        return True
    else:
        return False
    
def islower1(a):
    n=0
    for x in a:
        if ord(x)>=97 and ord(x)<=122 or (ord(x)>=32 and ord(x)<=64) or (ord(x)>=91 and ord(x)<=96):
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False

def isupper1(a):
    n=0
    for x in a:
        if ord(x)>=65 and ord(x)<=90 or (ord(x)>=32 and ord(x)<=64) or (ord(x)>=91 and ord(x)<=96):
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False

    
def Title(s):
    if type(s)==str:
        temp=[]
        if 97<=ord(s[0])<=122:
            temp.append(chr(ord(s[0])-32))
        else:
            temp.append(s[0])
        for x in range(1,len(s)):
            if s[x-1]==' ':
                if 97<=ord(s[x])<=122:
                    temp.append(chr(ord(s[x])-32))
                else:
                    temp.append(s[x])
            else:
                if 65<=ord(s[x])<=90:
                    temp.append(chr(ord(s[x])+32))
                else:
                    temp.append(s[x])
    else:
        return 'please enter string'
    return ''.join(temp)


   