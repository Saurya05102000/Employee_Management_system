from tkinter import *
from requests import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt



# functions for opening and reverse windows

def open_add_emp_win():
	add_emp_win.deiconify()
	root.withdraw()

def back_add_emp_win():
	root.deiconify()
	add_emp_win.withdraw()

def open_view_emp_win():
	view_emp_win.deiconify()
	root.withdraw()

def back_view_emp_win():
	root.deiconify()
	view_emp_win.withdraw()

def open_update_emp_win():
	update_emp_win.deiconify()
	root.withdraw()

def back_update_emp_win():
	root.deiconify()
	update_emp_win.withdraw()

def open_delete_emp_win():
	delete_emp_win.deiconify()
	root.withdraw()

def back_delete_emp_win():
	root.deiconify()
	delete_emp_win.withdraw()
	
def open_charts_win():
	charts_win.deiconify()
	root.withdraw()	

def back_charts_win():
	root.deiconify()
	charts_win.withdraw()


def insert_data():
	con = None
	try:
		con = connect("Employee2.db")
		cursor = con.cursor()
		sql = "insert into employee_rec values('%d','%s','%f')"
		id = id_ent.get()
		id = id.strip()
		
			
		if len(id)==0:
				
			showerror("wrong","id should not be empty")
			id_ent.delete(0,END)
			id_ent.focus()
			return
		
		
		if (id==""):
			showerror("wrong","invalid input")
			id_ent.delete(0,END)
			id_ent.focus()
			return
		try:
			id = int(id)
		except ValueError:
			showerror("wrong","id must be integers only")
			id_ent.delete(0,END)
			id_ent.focus()
			return
		
		if id<1:
			showerror("wrong","Minimum id should be 1")
			id_ent.delete(0,END)
			id_ent.focus()
			return
		
		
		
		name = name_ent.get()
		name= name.strip()
		if len(name)==0:
			showerror("wrong","name should not be empty")
			name_ent.delete(0,END)
			name_ent.focus()
			return
		
		elif (name.isdigit()):
			showerror("wrong","Name can't have integers")
			name_ent.delete(0,END)
			name_ent.focus()
			return

		if (not name.isalpha()):
			showerror("wrongs","Invalid input")
			name_ent.delete(0,END)
			name_ent.focus()
			return
		
		salary = salary_ent.get()
		salary = salary.strip()
		if len(salary)==0:
			showerror("wrong","salary should not be empty")
			salary_ent.delete(0,END)
			salary_ent.focus()
			return
		if (not salary.isdigit):
			showerror("wrong","salary can't have characters")
			salary_ent.delete(0,END)
			salary_ent.focus()
			return
		try:
			salary = float(salary)
		except:
			showerror("wrong","invalid input")
			salary_ent.delete(0,END)
			salary_ent.focus()
			return
		if salary<0:
			showerror("wrong","salary should not be negative")
			salary_ent.delete(0,END)
			salary_ent.focus()
			return
		
		cursor.execute(sql % (id,name,salary))
		con.commit()
		showinfo("Success"," Thank you \n Record inserted ")
		id_ent.delete(0,END)
		name_ent.delete(0,END)
		salary_ent.delete(0,END)
		id_ent.focus()
	except IntegrityError:
		showerror("Ohho","Id alredy exist")
		id_ent.delete(0,END)
		return
	finally:
		if con is not None:
			con.close()

def view_record():
	view_emp_win.deiconify()
	root.withdraw()
	view_data.delete(1.0, END)
	con = None	
	try:
		con = connect("Employee2.db")
		cursor = con.cursor()
		sql = "select * from employee_rec"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info += "Id= " + str(d[0]) + "\n" + "Name= " + str(d[1]) + "\n" + "Salary= " + str(d[2]) +"\n" +"\n"	
		view_data.insert(INSERT,info)
	except Exception as e:
		con.rollback()
		showerror("error",e)
		return
	finally : 
		if con is not None :
			con.close()		


def update_record():
	con = None
	try:
		con = connect("Employee2.db")
		cursor = con.cursor()
		sql = "update employee_rec set name = '%s', salary= '%f' where id ='%d'"
		id = id_ent3.get()
		id = id.strip()
		
			
		if len(id)==0:
				
			showerror("wrong","id should not be empty")
			id_ent3.delete(0,END)
			id_ent3.focus()
			return
		
		if (id==""):
			showerror("wrong","invalid input")
			id_ent3.delete(0,END)
			id_ent3.focus()
			return
		try:
			id = int(id)
		except ValueError:
			showerror("wrong","id must be integers only")
			id_ent3.delete(0,END)
			id_ent3.focus()
			return
		if id<1:
			showerror("wrong","Minimum id should be 1")
			id_ent3.delete(0,END)
			id_ent3.focus()
			return
		
		
		name = name_ent3.get()
		name= name.strip()
		if len(name)==0:
			showerror("wrong","name should not be empty")
			name_ent3.delete(0,END)
			name_ent3.focus()
			return
		
		elif (name.isdigit()):
			showerror("wrong","Name can't have integers")
			name_ent3.delete(0,END)
			name_ent3.focus()
			return

		if (not name.isalpha()):
			showerror("wrongs","Invalid input")
			name_ent3.delete(0,END)
			name_ent3.focus()
			return
	

		salary = salary_ent3.get()
		salary = salary.strip()
		if len(salary)==0:
			showerror("wrong","salary should not be empty")
			salary_ent3.delete(0,END)
			salary_ent3.focus()
			return
		if (not salary.isdigit):
			showerror("wrong","salary can't have characters")
			salary_ent3.delete(0,END)
			salary_ent3.focus()
			return
		try:
			salary = float(salary)
		except:
			showerror("wrong","invalid input")
			salary_ent3.delete(0,END)
			salary_ent3.focus()
			return
		if salary<0:
			showerror("wrong","salary should not be negative")
			salary_ent3.delete(0,END)
			salary_ent3.focus()
			return

		cursor.execute(sql%(name,salary,id))
		if cursor.rowcount == 1 : 
			con.commit()
			showinfo("Success" , "Records updated")
			id_ent3.delete(0 , END)
			name_ent3.delete(0 , END)
			salary_ent3.delete(0 , END)
			id_ent3.focus()
		else:
			showerror("wrong","Id does not exist")
			id_ent3.delete(0 , END)
			name_ent3.delete(0 , END)
			salary_ent3.delete(0 , END)
			id_ent3.focus()
			return
	except Exception as e:
		con.rollback()
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

def delete_rec():
	delete_emp_win.deiconify()
	root.withdraw()
	con = None
	try:
		con = connect("Employee2.db")
		cursor = con.cursor()
		sql = "delete from employee_rec where id='%d'"
		id  = id_ent4.get()
		id = id.strip()
		if len(id)==0:
				
			showerror("wrong","id should not be empty")
			id_ent4.delete(0,END)
			id_ent4.focus()
			return
		
		if (id==""):
			showerror("wrong","invalid input")
			id_ent4.delete(0,END)
			id_ent4.focus()
			return
		try:
			id = int(id)
		except ValueError:
			showerror("wrong","id must be integers only")
			id_ent4.delete(0,END)
			id_ent4.focus()
			return
		
		if id<1:
			showerror("wrong","Minimum id should be 1")
			id_ent4.delete(0,END)
			id_ent4.focus()
			return
		cursor.execute(sql %(id))
		if cursor.rowcount==1:
			con.commit()
			showinfo("Success" , "Record deleted")
			id_ent4.delete(0,END)
			id_ent4.focus()
		else :
			showerror("Failed" , "Record does not exists ")
			id_ent4.delete(0,END)
			id_ent4.focus()
			return
	except Exception as e:
		con.rollback()
		showerror("Issue" , e)
		id_ent4.delete(0,END)
		id_ent4.focus()
		return
	finally:
		if con is not None:
			con.close()

def view_chart():
	root.withdraw()	
	con = None
	try:
		con = connect("Employee2.db")
		cursor = con.cursor()
		sql = '''SELECT name, salary FROM employee_rec ORDER BY salary DESC LIMIT 5'''
		cursor.execute(sql)
		data = cursor.fetchall()
		name = []
		salary = []
		for i in data:
			name.append(i[0])
			salary.append(i[1])
		plt.figure(figsize=(8,6))
		c = ['green', 'white', 'yellow', 'blue' , 'pink' ]
		plt.rcParams.update({'text.color': "red", 'axes.labelcolor': "blue"})
		ax = plt.axes()
		ax.set_facecolor("black")  
		
		
		plt.bar(name, salary ,  color= c)
		plt.xlabel("Names of Employee" , fontsize = 15)
		plt.ylabel("Salary of Employee", fontsize = 15)
		plt.title("Top 5 Highest Salaried Employee", fontsize = 15)
		plt.grid()
		plt.show()
	except Exception as e:
        	showerror("issue ", e)
	        con.rollback()
	finally:
		if con is not None:
			con.close() 


	
	
			


# This coding is for main window that is "root"________

#creating window
#giving title
#setting dimensions
#adding font to the window
#setting some background colour

root = Tk()
root.title("Employee management system")
root.geometry("600x500+370+100")
f = ("Arial", 20, "bold")
f1 = ("Arial", 30, "bold")
f2 = ("Segoe UI", 20)
root.iconbitmap("Icon.ico")
root.configure(bg="Light gray")


# creating buttons

add_btn = Button(root, text="Add", font=f, width=15, relief="ridge",bg="yellow", command=open_add_emp_win)
view_btn = Button(root, text="View", font=f, width=15, relief="ridge", bg="yellow", command=view_record)
update_btn = Button(root, text="Update", font=f, width=15, relief="ridge", bg="yellow", command=open_update_emp_win)
delete_btn = Button(root, text="Delete", font=f, width=15, relief="ridge", bg="yellow", command= open_delete_emp_win)
char_btn = Button(root, text="Charts", font=f, width=15, relief="ridge", bg="yellow", command= view_chart)


# packing/placing button in root window

add_btn.place(x=165, y=70)
view_btn.place(x=165, y=130)
update_btn.place(x=165, y=190)
delete_btn.place(x=165, y=250)
char_btn.place(x=165, y=310)

# creating lables in root window

location_label = Label(root, text="Location: ", font=f, bg="Light gray")
temp_label= Label(root, text="Temp: ", font=f, bg="Light gray")
ans_location_label = Label(root, text="", font=f, bg="Light gray")
ans_temp_label= Label(root, text="", font=f, bg="Light gray")


# packing/placing labels in root window

location_label.place(x=20,y=400)
temp_label.place(x=350,y=400)
ans_location_label.place(x=160,y=400)
ans_temp_label.place(x=450,y=400)



# getting city name
wa = "https://ipinfo.io/" 
res = get(wa)	
data = res.json()	
city_name = data["city"]
ans_location_label.config(text=city_name)

# for temperature
a1 = "https://api.openweathermap.org/data/2.5/weather"
a2 = "?q=pune"
a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
a4 = "&units=" + "metric"

wa = a1+a2+a3+a4
res = get(wa)	
data = res.json()
temp = data["main"]["temp"]
ans_temp_label.config(text=temp)


# This coding is for add_emp_win window___________

add_emp_win = Toplevel(root)
add_emp_win.title("Add Employee")
add_emp_win.geometry("500x900+400+0")
add_emp_win.iconbitmap("Icon.ico")
add_emp_win.configure(bg="Light gray")
add_emp_win.withdraw()

# creating labels and entries

id_label = Label(add_emp_win, text="Enter id ", font=f, bg="Light gray")
id_ent= Entry(add_emp_win, font=f2, relief="solid")
name_label = Label(add_emp_win,text ="Enter name ", font=f,bg="Light gray")
name_ent = Entry(add_emp_win,font=f2, relief="solid")
salary_label = Label(add_emp_win,text="Enter salary", font=f, bg="Light gray")
salary_ent= Entry(add_emp_win,font=f2, relief="solid")

# placing and packing

id_label.place(x=190, y=70)
id_ent.place(x=97, y= 120)
name_label.place(x=170, y=200)
name_ent.place(x=97, y= 250)
salary_label.place(x=170, y=330)
salary_ent.place(x=97, y= 380)

# creating buttons for save and back

save_btn_1 = Button(add_emp_win, text="Save", font=f, width=10, bg="green", fg="white",relief = "solid" ,command = insert_data)
back_btn_1= Button(add_emp_win, text="Back", font=f, width=10, bg="yellow", relief="ridge" ,command=back_add_emp_win)

# placing buttons

save_btn_1.place(x=155,y=470)
back_btn_1.place(x=155,y=550)

# This coding is for view_emp_win window________

view_emp_win = Toplevel(root)
view_emp_win.title("Employee Data")
view_emp_win.geometry("900x500+200+100")
view_emp_win.iconbitmap("Icon.ico")
view_emp_win.configure(bg="Light gray")
view_emp_win.withdraw()

view_data = ScrolledText(view_emp_win, font=f, width=57,height=11)
view_data.place(x=10, y=10)


# creating buttons for back

back_btn_2= Button(view_emp_win, text="Back", font=f, width=10, bg="yellow", relief="ridge" ,command=back_view_emp_win)

# placing button

back_btn_2.place(x=355,y=430)


# This coding is for update_emp_win window________

update_emp_win = Toplevel(root)
update_emp_win.title("Update Employee")
update_emp_win.geometry("500x900+400+0")
update_emp_win.iconbitmap("Icon.ico")
update_emp_win.configure(bg="Light gray")
update_emp_win.withdraw()

# creating labels and entries

id_label3 = Label(update_emp_win, text="Enter id ", font=f, bg="Light gray")
id_ent3= Entry(update_emp_win, font=f2, relief="solid")
name_label3 = Label(update_emp_win,text ="Enter name ", font=f,bg="Light gray")
name_ent3 = Entry(update_emp_win,font=f2, relief="solid")
salary_label3 = Label(update_emp_win,text="Enter salary", font=f, bg="Light gray")
salary_ent3= Entry(update_emp_win,font=f2, relief="solid")

# placing and packing

id_label3.place(x=190, y=70)
id_ent3.place(x=97, y= 120)
name_label3.place(x=170, y=200)
name_ent3.place(x=97, y= 250)
salary_label3.place(x=170, y=330)
salary_ent3.place(x=97, y= 380)

# creating buttons for save and back

save_btn_3 = Button(update_emp_win, text="Save", font=f, width=10, bg="green", fg="white",relief = "solid", command=update_record )
back_btn_3= Button(update_emp_win, text="Back", font=f, width=10, bg="yellow", relief="ridge" ,command=back_update_emp_win)

# placing buttons

save_btn_3.place(x=155,y=470)
back_btn_3.place(x=155,y=550)


# This coding is for delete_emp_win window________

delete_emp_win = Toplevel(root)
delete_emp_win.title("Delete Employee")
delete_emp_win.geometry("500x900+400+0")
delete_emp_win.iconbitmap("Icon.ico")
delete_emp_win.configure(bg="Light blue")
delete_emp_win.withdraw()

# creating label and entry

id_label4 = Label(delete_emp_win, text="Enter id ", font=f, bg="Light blue")
id_ent4= Entry(delete_emp_win, font=f2, relief="solid")

id_label4.place(x=190, y=70)
id_ent4.place(x=97, y= 120)


# creating buttons for save and back

save_btn_4 = Button(delete_emp_win, text="Save", font=f, width=10, bg="red", fg="white",relief = "solid" , command= delete_rec )
back_btn_4= Button(delete_emp_win, text="Back", font=f, width=10, bg="yellow", relief="ridge" ,command=back_delete_emp_win)

# placing buttons

save_btn_4.place(x=155,y=250)
back_btn_4.place(x=155,y=330)


# This coding is for charts_win window________

charts_win = Toplevel(root)
charts_win.title("Charts")
charts_win.geometry("1000x700")
charts_win.iconbitmap("Icon.ico")
charts_win.configure(bg="Light blue")
charts_win.withdraw()

back_btn_5 = Button(charts_win, text="Back",font=f, width=10, relief="ridge", bg="yellow",command = back_charts_win)
back_btn_5.place(x=400,y=600)




def on_closing():
    if askyesno("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
add_emp_win.protocol("WM_DELETE_WINDOW", on_closing)
view_emp_win.protocol("WM_DELETE_WINDOW", on_closing)
update_emp_win.protocol("WM_DELETE_WINDOW", on_closing)
delete_emp_win.protocol("WM_DELETE_WINDOW", on_closing)




root.mainloop()