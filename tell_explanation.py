import pickle
fh=open('student.txt','r')
print(fh.tell())
print(fh.read())
print("Current position", fh.tell())