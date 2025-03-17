import tkinter as tk
from tkinter import ttk
import sqlite3

win = tk.Tk()
win.title('User Data Collection Form')

# win.geometry("600x350")
win.resizable('false','false')

ttk.Label(win,text='User Data Collection Form',font=('arial',20,'bold')).grid(row=0,column=0,columnspan=4,pady=20)

ttk.Label(win,text="FirstName ",font=('arial',10,'bold')).grid(row=1,column=0,sticky=tk.W,padx=15,pady=5)
first_name = tk.StringVar()
ttk.Entry(win,width=22,textvariable=first_name).grid(row=1,column=1,sticky=tk.W,pady=5)

ttk.Label(win,text="LastName ",font=('arial',10,'bold')).grid(row=1,column=2,sticky=tk.W,padx=15,pady=5)
last_name = tk.StringVar()
ttk.Entry(win,width=22,textvariable=last_name).grid(row=1,column=3,sticky=tk.W,padx=15,pady=5)


ttk.Label(win,text="PhoneNumber ",font=('arial',10,'bold')).grid(row=2,column=0,sticky=tk.W,padx=15,pady=5)
phone_number = tk.IntVar()
ttk.Entry(win,width=22,textvariable=phone_number).grid(row=2,column=1,sticky=tk.W,pady=5)


ttk.Label(win,text="EmailId ",font=('arial',10,'bold')).grid(row=3,column=0,sticky=tk.W,padx=15,pady=5)
email_id = tk.StringVar()
ttk.Entry(win,width=22,textvariable=email_id).grid(row=3,column=1,sticky=tk.W,pady=5)


ttk.Label(win,text='Gender',font=('arial',10,'bold')).grid(row=4,column=0,sticky=tk.W,padx=15,pady=5)
gender = tk.StringVar()
gender_combobox = ttk.Combobox(win,width=20,textvariable=gender,state='readonly')
gender_combobox['values'] = ('Male','Female','others')
gender_combobox.grid(row=4,column=1,sticky=tk.W)
gender_combobox.current(0)


ttk.Label(win,text="Nationality",font=('arial',10,'bold')).grid(row=5,column=0,sticky=tk.W,padx=15,pady=5)
nationality = tk.StringVar()
ttk.Radiobutton(win,text="India",value="IN",variable=nationality).grid(row=5,column=1,sticky=tk.W)
ttk.Radiobutton(win,text="USA",value='US',variable=nationality).grid(row=5,column=2,sticky=tk.W)


ttk.Label(win,text="College Name",font=('arial',10,'bold')).grid(row=6,column=0,sticky=tk.W,padx=15,pady=5)
college_name = tk.StringVar()
college_name_combobox = ttk.Combobox(win,width=20,textvariable=college_name,state='readonly')
college_name_combobox.grid(row=6,column=1,sticky=tk.W)
college_name_combobox['values'] = ('Arka jain university','RVS','BIT Sindri','BIT Mesra','Silicon Valley')



ttk.Label(win,text="Course",font=('arial',10,'bold')).grid(row=7,column=0,sticky=tk.W,padx=15,pady=5)
course = tk.StringVar()
course_combobox = ttk.Combobox(win,width=20,textvariable=course)
course_combobox.grid(row=7,column=1,sticky=tk.W)
course_combobox['values'] = ['Diploma','BTECH','MTECH','PHD']
course_combobox.current(0)


#options

ttk.Label(win,text="Hobbies",font=('arial',10,'bold')).grid(row=8,column=0,sticky=tk.W,padx=15,pady=5)
hobbies = tk.StringVar()
hobbies_combobox = ttk.Combobox(win,width=20,textvariable=hobbies)
hobbies_combobox.grid(row=8,column=1,sticky=tk.W)
hobbies_combobox['values'] = ('cricket','football','badminton')
hobbies_combobox.current(0)

conditions = tk.BooleanVar()
ttk.Checkbutton(win,text='Accept our Terms and conditions',variable=conditions).grid(row=9,column=0,sticky=tk.W,padx=15,pady=5)

connection = sqlite3.connect('sql.db')
cursor = connection.cursor()

# This function take only 10 user numbers 
def taketenNumber(phoneNumber):
    phno = phoneNumber  # Get the input value from the entry
    if len(phno) == 10 and phno.isdigit():  # Check if the input is exactly 10 digits and numeric
        return phno
    else:
        return "Phone number must be 10 digits."
          

def collect_user_data():
     if  taketenNumber(phone_number.get()) == "Phone number must be 10 digits.":
       ttk.Label(win,text="check your phone number",font=('arial',10,'bold')).grid(row=14,column=0,sticky=tk.W,padx=15,pady=5)
     else:
        firstname = first_name.get()
        lastname = last_name.get()
        emailid = email_id.get()
        phonenumber = phone_number.get()
        collegename = college_name.get()
        coursevalue = course.get()
        nationalityvalue = nationality.get()
        hobbiesvalue = hobbies.get()
        conditionsvalue = conditions.get()
        
        query = 'INSERT INTO user VALUES (?,?,?,?);'
        cursor.execute(query,(firstname,lastname,emailid,phonenumber))
        connection.commit()

submit_btn = ttk.Button(win,text='Submit',width=50,command=collect_user_data)
submit_btn.grid(row=10,column=0,columnspan=4,pady=20)

def selectdata():
     
     query = """
               SELECT * FROM user;
             """
     data = cursor.execute(query)
     retrive_data = data.fetchall()
     for row in retrive_data:
          print(row)

     return retrive_data

selectbtn = ttk.Button(win,text="Select data",width=50,command=selectdata)
selectbtn.grid(row=12,column=0,columnspan=4,pady=20)


win.mainloop()
