import math

def product(a):
    d=1
    for i in a:
        d*=i
    return d    
        
def ex ():

    f1='F1.txt'
    fi = open (f1, 'w+')
    f2='F2.txt'
    fi2 = open (f2, 'w+')
    f3='F3.txt'
    fi3 = open (f3, 'w+')

    n = int(input("Number of nubm.: "))
    print ("Input elements: ")
    for i in range (n):
        fi.write(input()+"\t")

    for line in fi:
        fi2.write(line)
    

    for i in fi:
        print(i)

    '''
    a=[]

    a=fi.read()
    for i in a:
        if(i%5==0):
            fi2.write(str(i))
        if((i<0) and (i%3==0)):
            fi3.write(str(i))
    print(a)
   

    for i in fi:
        print ("I: ",i)
        if(int(i)%5==0):
            fi2.write(str(i))
        if((int(i)<0) and (int(i)%3==0)):
            fi3.write(str(i))
    '''

    print(fi.read())
    print(fi2.read())
    print(fi3.read())

    fi.close()
    fi2.close()
    fi3.close()

def ex1 ():
    text='t.txt'
    t= open (text, 'w+' )

    t.write('AaBbCcDdEeFfGgHhIiJjKkLlMmN\nnOoPpQqRrSsTtUuV\nvWwXxYyZz')
    
    print(t.read())

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