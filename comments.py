s=input("give the name of the file that is in the same directory as comments.py ")
myfile= open(s,"r", encoding="utf-8")
lines = myfile.readlines()
myfile.close()
print(type(lines))
for line in lines:
	if "#" in line: #briskoyme an rxizei me #

		thisline=line.strip()
		if thisline[0]!="#":
			temp=line.split("#") #kano split se sxesh me to #
			#metrao ""
			a=temp[0].count("'")
			b=temp[0].count('"')
			#an to plhthos einai mono tote briskete se string kai den prepei na sbhstei
			if a%2==1 or b%2==1:
				print (line)
			else:
				print (line.split("#")[0])
	else:
		print (line)
