#LM 1st Recursion Notes

#does not work
'''
def recur(num,stuff=[]):
    if num==0:
        return stuff
    else:
        if num % 2==0:
            stuff.append(num)
            num-=1
            return recur(num,stuff=stuff)
        
print(recur(7))
'''


#factorial
def factor(num,sum=1):
    if num<=1:
        return sum
    else:
        sum*=num
        num-=1
        return factor(num,sum)
    
#better version:

def factor2(x):
    if x<=1:return 1
    return x*factor2(x-1)

print(factor2(13))

#saves some variables, annoying

def lucas(n,seq=[2,1]):
    if n<=2:return seq
    seq.append(seq[len(seq)-2]+seq[len(seq)-1])
    return lucas(n-1,seq)

def find_lucas(n):
    if n==2:return 1
    if n==0:return 2
    return find_lucas(n-1)+find_lucas(n-2)

print(lucas(6))

print(find_lucas(6))