import numpy as np
import time
import math
from num2words import num2words

def Euler1():
    i=0.0
    T=0
    while i<1000:
        if i%3==0 or i%5==0:
            T+=i

        i+=1
    print T

def Euler2():
    i=0
    j=1
    k=0
    T=0
    while k<4000000:
        k=i+j
        if k%2==0:
            T=T+k
        print k
        i=j
        j=k
    print T


def isprime(i):
    j = 2
#    print 'checking if ',i,' is prime'
    while j < i:
        if i % j == 0:
#            print i, ' is not prime'
            return 0
        j+=1
#    print i, ' is prime'
    return 1

def Euler3():

    a=600851475143.0
    i=2
    #primes = np.array()

    while i < a:
        #print 'checking ', i
        #time.sleep(0.01)
        if a%i == 0.0:
            print i, 'is a factor'
            prime = isprime(i)
            if prime == 1:
                print 'prime factor #############',i
                #a/=i
                #i=1
        prime = 0
        i+=1

def ispal(i):
    i=str(i)
    #print i
    j=i[::-1]
    #print j
    if i==j:
        return 1
    else:
        return 0


def Euler4():
    a=999
    M=0
    while a>100:
        #print a
        b=999
        while b>100:
            #print b
            c=a*b
            if ispal(c)==1:
                print c, 'is a palendrome'
                if c>M:
                    M=c
                #break
            b-=1
        a-=1
    print 'largest Palendrome: ',M


def Euler5():
    a=20
    while a<10000000000:
        a+=1
        i=1
        div = 1
        while i < 21:
            if a%i <> 0:
                div=0
                print a, ' not divisible by ',i
                i+=1
                break
            i+=1
        if div ==1:
            print a
            break


def Euler6():
    i=1.0
    I=0.0
    #sum of squares
    while i<101:
        I=I+i**2
        i+=1

    j=1.0
    J=0.0
    #square of sums
    while j<101:
        J=J+j
        j+=1
    J=J**2

    print J-I


def Euler7():
    st=1
    i=2
    while st<>10000001:
        if isprime(i):
            print st, 'th prime is',i
            st+=1
        i+=1

def Euler8():
    a= '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    i=0
    T=0
    while i<len(a)-1:
        b=a[i:i+13]
        print b
        t=1
        for j in b:
            t = int(j)*t
        if t>T:
            T=t
        i+=1
    print T

def Euler9():
    a=1
    b=1
    t=1
    a=1
    while a<800:
        b=a
        while b<800:
            c=math.sqrt((a*a)+(b*b))
            if c%1 == 0:
                t=a+b+c
                print t
                if t==1000:
                    print '########### found #############', a*b*c
                    break
            b+=1
        a+=1
    print t
    print a*b*c


def Euler10():
    i=1
    t=1
    while i<2000000:
        if isprime(i):
            t=t+i
            print i
        i+=1
    print t


def Euler11():
    a=np.array([8,02])#,22,97,38,15,00,40,00,75,04,05,07,78,52,12,50,77,91,08,49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,04,56,62,00,81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,03,49,13,36,65,52,70,95,23,04,60,11,42,69,24,68,56,01,32,56,71,37,02,36,91,22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80,24,47,32,60,99,03,45,02,44,75,33,53,78,36,84,20,35,17,12,50,32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70,67,26,20,68,02,62,12,20,95,63,94,39,63,08,40,91,66,49,94,21,24,55,58,05,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72,21,36,23,09,75,00,76,44,20,45,35,14,00,61,33,97,34,31,33,95,78,17,53,28,22,75,31,67,15,94,03,80,04,62,16,14,09,53,56,92,16,39,05,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57,86,56,00,48,35,71,89,07,05,44,44,37,44,60,21,58,51,54,17,58,19,80,81,68,05,94,47,69,28,73,92,13,86,52,17,77,04,89,55,40,04,52,08,83,97,35,99,16,07,97,57,32,16,26,26,79,33,27,98,66,88,36,68,87,57,62,20,72,03,46,33,67,46,55,12,32,63,93,53,69,04,42,16,73,38,25,39,11,24,94,72,18,08,46,29,32,40,62,76,36,20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,04,36,16,20,73,35,29,78,31,90,01,74,31,49,71,48,86,81,16,23,57,05,54,01,70,54,71,83,51,54,69,16,92,33,48,61,43,52,01,89,19,67,48])
    i=0
    M=0
    while i<400-63:
        m=a[i]*a[i+21]+a[1+42]+a[i+63]#diagonal backslash
        if m>M:
            M=m
        i+=1
    i=3
    while i<400-80:
        m = a[i] * a[i + 19] + a[1 + 38] + a[i + 57]  # diagonal forwardslash
        if m>M:
            M=m
    i=0
    while i<400-4:
        m = a[i] * a[i + 1] + a[1 + 2] + a[i + 3]  # left right
        if m>M:
            M=m
    i=0
    while i<400-80:
        m = a[i] * a[i + 20] + a[1 + 40] + a[i + 60]  # up down
        if m>M:
            M=m


def countDivs(I):
    divs = 1
    for a in range(1,I):
        if I%a==0:
            divs+=1
    return divs


def Euler12():
    i=1
    divs=0
    I=0
    while divs<500:
        I=I+i
        i+=1
        divs = countDivs(I)
        print I, divs
    print I

def Euler15():
    a=2**39
    routes=0
    while a < 2**40:
        b=str(bin(a))
        i=0
        #print b
        #time.sleep(0.01)
        for c in b:
            #print c
            if c=='1':
                i+=1
        if i==20:
            #print '########## route found!!! #########'
            routes+=1
            print routes, 'rts'
        a+=1
    print routes


def Euler14():
    startn=1
    Mlen = 1
    while startn<1000000:
        n=startn
        len=1
        while n <> 1:
            if n % 2 == 0:
                n = n/2
            else:
                n=3*n+1
            len+=1
            #print n
        print startn, len
        if len>Mlen:
            Mlen = len
            Mdex = startn
        startn+=1
    print Mdex, Mlen


def Euler16():
    a=2**1000
    i=0
    for b in str(a):
        i=i+int(b)
    print i


def Euler17():
    T=0
    for n in range(1,1001):
        a = num2words(n)
        a=a.replace("-", "")
        a=a.replace(" ", "")
        T=T+len(a)
        print n,a,len(a)
    print T


def Euler18():
    a=np.array(15,15)
    a[1] = 75
    a[2] = 95, 64
    a[3] = 17, 47, 82
    a[4] = 18, 35, 87, 10
    a[5] = 20, 04, 82, 47, 65
    a[6] = 19, 01, 23, 75, 03, 34
    a[7] = 88, 02, 77, 73, 07, 63, 67
    a[8] = 99, 65, 04, 28, 06, 16, 70, 92
    a[9] = 41, 41, 26, 56, 83, 40, 80, 70, 33
    a[10] = 41, 48, 72, 33, 47, 32, 37, 16, 94, 29
    a[11] = 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14
    a[12] = 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57
    a[13] = 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48
    a[14] = 63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31
    a[15] = 04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23


def Euler20():
    a=math.factorial(100)
    T=0
    for b in str(a):
        T=T+int(b)
    print T

def Euler21():
    T=0
    for i in range(1,10000):
        t=0
        for j in range(1,i):
            if i%j==0:
                t+=j #t is the sum of the factors in i
        k=0
        for j in range(1,t):
            if t%j==0:
                k+=j
        if k==i and t<>i:
            print 'amicable',t,i
            T+=i
    print T


def inabundent(i):
    t=0
    for j in range(1,i):
        if i%j==0:
            t+=j
    if t>i:
        return 1
    else:
        return 0

def Euler23():
    return 1



Euler20()

