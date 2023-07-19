fh=open("Student.txt",'rb')
fh.seek(-15,2)
str1=fh.read(15)
print("Last 15 bytes of file contain:", str1)