name = ["A"];

n = int(raw_input("Enter number of fixed points:"))

for i in range(1,n+1):
	name = name + ["test"+`i`];


# List name should look like this:
#name = ["A", "test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8"];



fp = len(name);


for j in range(0,fp):

	f=open(name[j])
	lines=f.read().splitlines()

	#print(len(lines))

	foo=open('Singular'+name[j],'wb+')

	if len(lines)>1:
		for i in range(0,len(lines)):
			foo.write('vector s'+`i+1`+'='+'['+lines[i]+'];\n')

	string = ""
	
	if len(lines)>1:
		for i in range(0,len(lines)):
			if i == 0:
				string = 's' +`i+1`
			else:		
				string = string + ','+'s' +`i+1`
	#print string+';'


	if len(lines)>1:
		foo.write('module m'+'='+ string + ';')	

	f.close()
	foo.close()


import string

foo=open('Singularlists','wb+')

#n = int(raw_input("Enter number of files to be formatted:"))

vertex = [];



for i in range(1,n+1):
	vertex = vertex + [i]	


s = str(vertex);

foo.write("list vertex" + "=" + s[1:len(s)-1] + ";")

sing = [];

for i in range(1,n+1):
	sing = sing + ["\"Singulartest"+`i`+"\""] # Note the bounding ""	

s = str(sing).replace('\'',''); #this replaces the '' with a blank character


 
foo.write("\n\nlist sing "+ "=" +  str(s[1:len(s)-1])+";")


foo.close()
	



	

