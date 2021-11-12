from sqlite3 import *
class connection:

	con=None

	def __init__(self,db_name):
		self.db=db_name
		self.con = connect(self.db)
		self.cursor = self.con.cursor()
		
			

	def insert(self,rn,name,marks):
		try:
			sql="insert into student_info values('%d','%s','%d')"
			self.cursor.execute(sql%(rn,name,marks))
			self.con.commit()
			return "OK"
		except IntegrityError:
			self.con.rollback()
			msg="Error : "+ "Roll number already present"
			return msg
		except Exception as e:
			self.con.rollback()
			msg="Error : "+str(e)
			return msg
		
	
	def view(self):
		info=""
	
		try:
			
			sql="select * from student_info ORDER BY rno ASC"
			self.cursor.execute(sql)
			
			data=self.cursor.fetchall()
			#vw_st.insert(INSERT,"Rno\t  Name\t\tMarks\n")
			for d in data:
				info=info+"  "+str(d[0])+"\t "+str(d[1])+"\t\t   "+str(d[2])+"\n"
			return info
		
		except Exception as e:
			print("Error",str(e))


	def update(self,rn,name,marks):
		try:
			sql="update student_info set name='%s', mark='%d' where rno='%d'"
			self.cursor.execute(sql % (name,marks,rn))
			if self.cursor.rowcount ==1:
				self.con.commit()
				msg="OK"
			else:
				msg="record does not exists"
			return msg
	
		except Exception as e:
			self.con.rollback()
			return "Error : ",str(e)
		
	
	def delete(self,rn):
		try:
			sql="delete from student_info where rno='%d'"
			self.cursor.execute(sql % (rn))
			if self.cursor.rowcount==1:
				self.con.commit()
				return "OK"
			else:
				return "record does not exists"	
		except Exception as e:
			self.con.rollback()
			return "Error : ",str(e)
		
	 
			
		
	
conn=connection("sms.db")
#conn.view()
#conn.insert(rn,name,marks)
#conn.update(rn,name,marks)
#conn.delete(rn)

