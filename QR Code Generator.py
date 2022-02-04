from tkinter import *
from tkinter import messagebox
import pyqrcode #import QR code generator
import os

window = Tk() #create a window to open the QR code
window.title("QR Code Generator") #title of the window 

#QR Code generation
def generate():
	if len(subject.get()) != 0: #check if subject is empty
		global myQr #global variable
		myQr= pyqrcode.create(subject.get()) #create QR code
		qrImage= myQr.xbm(scale=6) #create image
		global photo #global variable
		photo = BitmapImage(data= qrImage) #create photo
	else:
		messagebox.showinfo("Error!", "Please Enter Your URL") #error message
	try:
		showCode()  #show the QR code
	except:
		pass #error message
		
#code showing
def showCode():     #show the QR code
	global photo    #global variable
	notificationLabel.config(image= photo) #show the QR code
	subLabel.config(text= "Showing QR Code for: "+subject.get())    #show the subject
	
def save(): #save the QR code
	#folder to save all the codes
	dir= path1 = os.getcwd() + "\\QR Codes" #get the current directory
	
	#create a folder is it doesn't exist
	if not os.path.exists(dir):     #check if folder exists
		os.makedirs(dir)    #create folder
	
	try:
		if len(name.get())!=0:  #check if name is empty
			qrImage = myQr.png(os.path.join(dir, name.get()+".png"), scale= 6) #save the QR code
		else: 
			messagebox.showinfo("Error!", "File name can not be empty!") #error message
	except:
		messagebox.showinfo("Error!", "Please generate the code first") #error message
	

lab1 = Label(window, text="Enter Your URL",  font=("Helvetica", 12)) #label for subject entry box 
lab1.grid(row=0, column= 0, sticky= N+S+E+W) #grid the label 

lab2 = Label(window, text="Enter File Name",  font=("Helvetica", 12))   #label for name entry box
lab2.grid(row=1, column= 0, sticky= N+S+E+W) #grid the label    

subject= StringVar()    #subject variable
subjectEntry = Entry(window, textvariable = subject,font=("Helvetica", 12)) #subject entry box
subjectEntry.grid(row=0, column=1, sticky= N+S+E+W) #grid the subject entry box

name= StringVar()   #name variable
nameEntry = Entry(window, textvariable = name, font=("Helvetica", 12))  #name entry box
nameEntry.grid(row=1, column=1, sticky= N+S+E+W)    #grid the name entry box

createButton = Button(window, text= "Create QR Code", font=("Helvetica", 12), width= 15,command= generate)      #create button
createButton.grid(row=0, column=3, sticky= N+S+E+W) #grid the create button

notificationLabel= Label(window)    #label for QR code
notificationLabel.grid(row= 2, column=1, sticky= N+S+E+W)   #grid the label entry box

subLabel= Label(window, text="") #error message label    
subLabel.grid(row= 3, column=1, sticky= N+S+E+W) #grid the label entry box

showButton = Button(window, text ="Save as PNG", font=("Helvetica", 12), width= 15, command=save)   #show button 
showButton.grid(row=1, column=3, sticky= N+S+E+W) #grid the show button 


#Making responsive layout:
totalRows= 3    #total rows
totalCols = 3   #total columns 

for row in range(totalRows+1):  #loop for rows
	window.grid_rowconfigure(row, weight=1)     #make the rows responsive

for col in range(totalCols+1):  #loop for columns
	window.grid_columnconfigure(col, weight=1)  #make the columns responsive

#looping the GUI
window.mainloop()   #loop the GUI window 