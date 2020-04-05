fhandle = open('abc.txt','w')  #'w' means write mode. it can write file.
line1 = 'he is playing\n'  #it's a string
fhandle.write(line1)
line2 = 'he is running \n'
fhandle.write(line2)
#fhandle.close #here close the Previous files
#fhandle = open('abc.txt', 'r') # here 'r' means that read mode.
#data = fhandle.read()  #here read the files
#print(len(data))      #to count the Number of character of the file.

#how to numbers insert the files system
#fhandle = open('abc.txt','w')
name = 'Sohan'
Age = 23
CGPA = 3.75
fhandle.write(name + '\n')
fhandle.write(str(Age) + '\n')
fhandle.write(str(CGPA))
