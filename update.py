import pickle
stu={}
found=False
fin=open('student.dat','rb')
keys=['Aditi']

try:
    print("Searching inside file")
    while True:
        stu=pickle.load(fin)
        if stu['Name'] in keys:
            stu['Name']='Udbhav'
            found=True
        print(stu)    
except EOFError:
    if found==False:
        print("Nothing such keyword found")
    else: 
        print("Search succesful")
fin.close()                       
