import math

def product(a):
    d=1
    for i in a:
        d*=i
    return d    
        
def ex ():

    f1='F1.txt'
    fi = open (f1, 'w')
    f2='F2.txt'
    fi2 = open (f2, 'w')
    f3='F3.txt'
    fi3 = open (f3, 'w')

    n = int(input("Number of nubm.: "))
    print ("Input elements: ")
    for i in range (n):
        fi.write(input()+"\n")
    fi.close()
    fi = open (f1, 'r')

    '''
    for i in fi:
        fi2.write(i)
    '''    

    fi.flush()
    
    a=[]

    for i in fi.readlines():
        a.append(int(i))
    
    for i in a:
        if(i%5==0):
            fi2.write(str(i)+"\n")
        if((i<0) and (i%3==0)):
            fi3.write(str(i)+"\n")
    print(a)

    fi.close()
    fi2.close()
    fi3.close()
    fi2 = open (f2, 'r')
    fi3 = open (f3, 'r')

    '''
    for i in fi:
        print ("I: ",i)
        if(int(i)%5==0):
            fi2.write(str(i))
        if((int(i)<0) and (int(i)%3==0)):
            fi3.write(str(i))
    '''

    print("\nF2: ")
    print(fi2.read())
    print("\nF3: ")
    print(fi3.read())

    fi.close()
    fi2.close()
    fi3.close()

def ex1 ():
    text='t.txt'
    t= open (text, 'r' )

    print("Text: ")
    print(t.read())

    #t.flush()
    
    a=[]

    for i in t.readlines():
        a.append(chr(i))

    data = t.read().splitlines()
    print(data)

    t.seek(0)
    first = t.readline()
 
    print("\n1 line 1 char: ")
    print(first[0])

    print("\n1 line 5 char: ")
    print(first[4])

    print("\n1 line 10 char-s: ")
    for i in range(10):
        print(first[i])

    print ("\nS1: ")
    s1 = int(input())
    print ("S2: ")
    s2 = int(input())

    print("\n1 line from s1 to s2: ")
    i=0
    for i in range(s2):
        if (i>=s1 and i<=s2):
            print(first[i])

    print("\n2 line: ")
    second=t.readline()
    print(second)

    print("\n2 line 1 char: ")
    print(second[0])

    print ("Line N: ")
    n = int(input())
    print ("\nChar K: ")
    k = int(input())

    t.seek(0)
    for i in range(n):
        line=t.readline()
    print("\n",n,"line ",k," char: ")
    print(line[k])


    print()

    '''
    
    for i in txt:
        first = i[0] 
        break
    print(first)
'''
    t.close()

print ("N: ")
n = int(input())

match n:
        case 1:
            ex()
        case 2:
            ex1()
        case default:
            print ("Error")