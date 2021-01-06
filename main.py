from tkinter import*
import tkinter.messagebox

import  backedn

class Student:
            def  __init__(self,root):
                              self.root = root
                              self.root.title("Student database Management system")
                              self.root.geometry("1350x750+0+0")
                              self.root.config(bg="cadet blue")

                              StdID =StringVar()
                              firstname =StringVar()
                              Surname=StringVar()
                              Dob=StringVar()
                              Age =StringVar()
                              Gender =StringVar()
                              Address =StringVar()
                              Mobile =StringVar()

                              MainFrame = Frame(self.root ,bg="cadet blue" )
                              MainFrame.grid()

                              TitFrame=Frame(MainFrame,  bd=2, padx=54,pady=8,bg="Ghost white",relief=RIDGE)
                              TitFrame.pack(side=TOP)
                              
                              self.lblTit=Label(TitFrame ,font=('arial',47,'bold'),text='Student Database Management Systems',bg="Ghost White")
                              self.lblTit.grid()
                              
                              ButtonFrame=Frame(MainFrame, bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
                              ButtonFrame.pack(side=BOTTOM)

                              DataFrame=Frame(MainFrame, bd=1,width=1300,height=400, padx=20 , pady=20 , relief=RIDGE,  bg="cadet blue")
                              DataFrame.pack(side=BOTTOM)

                              DataFrameLEFT=LabelFrame(DataFrame, bd=1 ,width=1000,height=600 ,padx=20,relief=RIDGE ,bg="Ghost White",
                                                  font=('arial',20,'bold'), text="Student info\n")
                              DataFrameLEFT.pack(side=LEFT)

                              DataFrameRIGHT=LabelFrame(DataFrame,bd=1 ,width=450 ,height=300 ,padx=31,pady=3,relief=RIDGE,bg="Ghost White",
                                                   font=('arial' , 20 ,' bold' ), text="Student Details\n")
                              DataFrameRIGHT.pack(side=RIGHT)

                              #Funtions------------------------------------------------------------------------------------------------------------------------------------------
                              def iexit():
                                              iexit=tkinter.messagebox.askyesno("Students Database system","confirm if you want to exit")
                                              if iexit > 0:
                                                root.destroy()
                                              return

                              def cleardata():
                                             self.txtStdID.delete(0,END)
                                             self.txtfna.delete(0,END)
                                             self.txtSna.delete(0,END)
                                             self.txtDob.delete(0,END)
                                             self.txtAge.delete(0,END)
                                             self.txtGender.delete(0,END)
                                             self.txtAdr.delete(0,END)
                                             self.txtMobile.delete(0,END)
                              def addData():
                                                if(len(StdID.get())!=0):
                                                                backedn.addStdRec(StdID.get() ,firstname.get() ,Surname.get() , Dob.get() , Age.get() , Gender.get() ,Address.get() ,Mobile.get())
                                                                studentlist.delete(0,END)
                                                                studentlist.insert(END,StdID.get() ,firstname.get() ,Surname.get() , Dob.get() , Age.get() , Gender.get() ,Address.get() ,Mobile.get())

                              def display():
                                              studentlist.delete(0,END)
                                              for row in backedn.viewData():
                                                              studentlist.insert(END,row,str(" "))

                              def StudentRec(event):
                                              global sd
                                              searchStd=studentlist.curselection()[0]
                                              sd=studentlist.get(searchStd)

                                              self.txtStdID.delete(0,END)
                                              self.txtStdID.insert(END,sd[1])
                                              self.txtfna.delete(0,END)
                                              self.txtfna.insert(END,sd[2])
                                              self.txtSna.delete(0,END)
                                              self.txtSna.insert(END,sd[3])
                                              self.txtDob.delete(0,END)
                                              self.txtDob.insert(END,sd[4])
                                              self.txtAge.delete(0,END)
                                              self.txtAge.insert(END,sd[5])
                                              self.txtGender.delete(0,END)
                                              self.txtGender.insert(END,sd[6])
                                              self.txtAdr.delete(0,END)
                                              self.txtAdr.insert(END,sd[7])
                                              self.txtMobile.delete(0,END)
                                              self.txtMobile .insert(END,sd[8])

                              def delete():
                                              if(len(StdID.get())!=0):
                                                   backedn.deleteRec(sd[0])
                                                   cleardata()
                                                   display()
                              def  search():
                                              studentlist.delete(0,END)
                                              for row in backedn.searchData(StdID.get() ,firstname.get() ,Surname.get() , Dob.get() , Age.get() , Gender.get() ,Address.get() ,Mobile.get()) :
                                                                            studentlist.insert( END,row,str(" "))
                                                                            
                                                                      

                              def update():
                                              if(len(StdID.get())!=0):
                                                              backedn.deleteRec(sd[0])
                                              if(len(StdID.get())!=0):
                                                 backedn.addStdRec(StdID.get() ,firstname.get() ,Surname.get() , Dob.get() , Age.get() , Gender.get() ,Address.get() ,Mobile.get())
                                              
                                                 studentlist.delete(0,END)
                                                 backedn.addStdRec( StdID.get() ,firstname.get() ,Surname.get() , Dob.get() , Age.get() , Gender.get() ,Address.get() ,Mobile.get())
                                
                                

                                           
                                                               
                                              
                              


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                              self.lblStdID=Label(DataFrameLEFT ,font=('arial',20,'bold'),text='Student ID', padx=2 , pady=2,  bg="Ghost White")
                              self.lblStdID.grid(row=0,column=0,sticky=W)
                              self.txtStdID=Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable=StdID,width=39)
                              self.txtStdID.grid(row=0,column=1)

                              self.lblfna=Label(DataFrameLEFT ,font=('arial',20,'bold'),text='FirstName', padx=2 , pady=2,  bg="Ghost White")
                              self.lblfna.grid(row=1,column=0,sticky=W)
                              self.txtfna=Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable= firstname,width=39)
                              self.txtfna.grid(row=1,column=1)

                              self.lblSna=Label(DataFrameLEFT ,font=('arial',20,'bold'),text='SurName', padx=2 , pady=2,  bg="Ghost White")
                              self.lblSna.grid(row=2,column=0,sticky=W)
                              self.txtSna=Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable= Surname,width=39)
                              self.txtSna.grid(row=2,column=1)



                              self.lblDob=Label(DataFrameLEFT ,font=('arial',20,'bold'),text='Mobile', padx=2 , pady=2,  bg="Ghost White")
                              self.lblDob.grid(row=3,column=0,sticky=W)
                              self.txtDob=Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable=Dob,width=39)
                              self.txtDob.grid(row=3,column=1)

                              self.lblAge=Label(DataFrameLEFT ,font=('arial',20,'bold'),text='Address', padx=2 , pady=2,  bg="Ghost White")
                              self.lblAge.grid(row=4,column=0,sticky=W)
                              self.txtAge=Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable=Age,width=39)
                              self.txtAge.grid(row=4,column=1)

                              self.lblGender=Label(DataFrameLEFT ,font=('arial',20,'bold'),text='Dob', padx=2 , pady=2,  bg="Ghost White")
                              self.lblGender.grid(row=5,column=0,sticky=W)
                              self.txtGender=Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable=  Gender ,width=39)
                              self.txtGender.grid(row=5,column=1)

                              self.lblAdr=Label(DataFrameLEFT ,font=('arial',20,'bold'),text='Age', padx=2 , pady=2,  bg="Ghost White")
                              self.lblAdr.grid(row=6,column=0,sticky=W)
                              self.txtAdr=Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable= Address,width=39)
                              self.txtAdr.grid(row=6,column=1)

                              self.lblMobile=Label(DataFrameLEFT ,font=('arial',20,'bold'),text='Gender', padx=2 , pady=2,  bg="Ghost White")
                              self.lblMobile.grid(row=7,column=0,sticky=W)
                              self.txtMobile=Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable= Mobile,width=39)
                              self.txtMobile.grid(row=7,column=1)

                              scrollbar =Scrollbar(DataFrameRIGHT)
                              scrollbar.grid(row=0 ,column=1,sticky='ns')
                              studentlist =Listbox(DataFrameRIGHT ,width=41 ,height=16 ,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
                              studentlist.bind("<<ListboxSelect>>",StudentRec)
                              studentlist.grid(row=0 ,column=0 ,padx=8)
                              scrollbar.config(command= studentlist.yview)


                              self.btnAddData =Button(ButtonFrame, text="Add New" ,font=('arial',20,'bold'),height=1,width=10,bd=4,command=addData)
                              self.btnAddData.grid(row=0,column=0)

                              self.btnDisplaydata =Button(ButtonFrame, text="Display" ,font=('arial',20,'bold'),height=1,width=10,bd=4,command=display)
                              self.btnDisplaydata .grid(row=0,column=1)

                              self.btnCleardata =Button(ButtonFrame, text="Clear" ,font=('arial',20,'bold'),height=1,width=10,bd=4,command=cleardata)
                              self.btnCleardata.grid(row=0,column=2)

                              self.btnDeleteData =Button(ButtonFrame, text="Delete" ,font=('arial',20,'bold'),height=1,width=10,bd=4,command=delete)
                              self.btnDeleteData.grid(row=0,column=3)

                              self.btnSearchData=Button(ButtonFrame, text="Search" ,font=('arial',20,'bold'),height=1,width=10,bd=4,command=search)
                              self.btnSearchData.grid(row=0,column=4)

                              self.btnUpdateData =Button(ButtonFrame, text="Update" ,font=('arial',20,'bold'),height=1,width=10,bd=4,command=update)
                              self.btnUpdateData.grid(row=0,column=5)

                              self.btnExit =Button(ButtonFrame, text="Exit" ,font=('arial',20,'bold'),height=1,command=iexit,width=10,bd=4)
                              self.btnExit.grid(row=0,column=6)
                              

                              

                              
                                
                                        
if  __name__=='__main__':
                root=Tk()
                application = Student(root)
                root.mainloop()
                
