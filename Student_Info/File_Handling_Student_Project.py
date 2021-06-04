a=True
def exit():
    global a
    a=False
def addstudent():
    name=input("What is your name")
    m1=input("Enter marks for subject 1")
    m2=input("Enter marks for subject 2")
    m3=input("Enter marks for subject 3")
    f=open("Student.txt","a")
    f.write(name+","+m1+", "+m2+", "+m3+"\n")
    f.close()
def percentage():
    n=input("What is your name")
    f=open("Student.txt","r")
    lines=f.readlines()
    for i in lines:
        data=i.split(",")
        if data[0]==n:
            percentage_res=int(data[1])+int(data[2])+int(data[3].replace("\n",""))/300*100
            print(percentage_res)
    f.close()
while a:
    print("Choose your options")
    print("1: Add Student")
    print("2: Get Percentage")
    print("3: Exit")
    option = int(input("Enter your option "))
    
    if option==3:
        exit()
        
    if option==2:
        percentage()
        
    if option==1:
        addstudent()