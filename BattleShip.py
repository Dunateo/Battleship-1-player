from random import*
l=randint(1,10)
c=randint(1,10)
x=int(input("enter the location of the boat line="))
y=int(input("column="))
diffx=abs(x-l)
diffy=abs(y-c)
for ligne in range(1,11):
	for colonne in range(1,11):
		if l==ligne and c==colonne:
			while diffx!=0 and diffy!=0:
				print("retry")
				if diffx==1 and diffy==1:
					print("you see it")
				else:
					print("in water")
				x=int(input("line="))
				y=int(input("column="))
				diffx=abs(x-l)
				diffy=abs(y-c)
			else:
				print("You touch it!!")
	
