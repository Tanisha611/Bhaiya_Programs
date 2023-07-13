import pickle
emp1={'RollNo':13,'Empno':1224,'Name':'Aditi','Age':'Negligible'}
emp2={'RollNo':12,'Empno':1234,'Name':'Tanisha','Age':'Negligible'}
emp3={'RollNo':14,'Empno':1245,'Name':'Kushal','Age':15}

file_o=open("student.dat","wb")

pickle.dump(emp1,file_o) #writing into file.
pickle.dump(emp2,file_o) #writing into file.
pickle.dump(emp3,file_o)

print("Successfully written two dicts")
file_o.close()

file_s=open("student.dat","rb")
try: #why was try & except used?
    while True: #why was a loop used?
        file_l=pickle.load(file_s) #reading a file
        print(file_l) #printing the data read above.
except EOFError:
    file_s.close()