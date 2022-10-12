
def start():
    print("Enter")
    print("1 to read file")
    print("2 to add data in file")
    print("3 to update existing data")

def Print():
    file=open("123.txt",'r')
    print(file.read())
    file.close()
def add():
    file=open("123.txt",'a')
    z=input("enter the data in format=no.name")
    file.write('''
    '''+z)
    file.close()


def deleteLine(k):
    file = open("123.txt", 'r')
    output = []
    for line in file:
        if not line.startswith(k):
            output.append(line)
    file.close()
    file = open("123.txt", 'w')
    file.writelines(output)
    file.close()

def update():
    u=int(input("enter the line_no:"))
    file=open("123.txt",'r')
    a=file.readlines()
    k=a[u-1]
    z=input("enter the data in formet=line _no.data")
    a.insert(u-1,z+'\n')
    file.close()
    file=open("123.txt",'w')
    file.writelines(a)
    file.close()
    deleteLine(k)

def mainfunc():

    start()
    c=int(input())
    if(c==1):
        Print()
    elif(c==2):
        add()
    elif(c==3):
        update()
    j = input("do you want to do antother changes:(y/n):")
    if (j == 'y' or j == 'Y'):
        mainfunc()

mainfunc()
