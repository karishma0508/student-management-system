def rn_validator(rn):
	rn=rn.strip()
	if rn.isdigit() and int(rn)>0: 
		return True
	else:
		msg="Issue In roll number : \n"+"Roll number shud  be  non empty and positive integer only "
		return msg
		return False

def name_validator(name):
	name=name.strip()
	l=len(name)
	if name.isalpha() and l>=2:
		return True
	else:
		msg="Issue In name : \n"+"name shud  be non empty alphabetic only and minimum length is two"
		return msg
		return False
		

def marks_validator(marks):
	marks=marks.strip()
	if marks.isdigit() and marks!="" and 0<int(marks)<=100:
		return True
	else:
		msg="issue In Marks :\n"+"marks shud  be non empty and positive integer upto 100" 
		return msg	
		return False

"""rn_validator(input("rn : "))
name_validator(input("name: "))
marks_validator(input("marks : "))"""