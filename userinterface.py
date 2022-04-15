
""""
school management appliaction by jonah walakira
tool still under developemt
its basic main line logic that has been implemented sofar
project still under developemt


 jonahwalakira650@gmail.com
 last updated on 3rd Dec 2021
"""











from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from database import datacon




class home(Tk):


    def __init__(self):
        super(home, self).__init__()
        self.top_menue()
        self.Nbook()
        self.set_Registration_tab_content()
        self.set_fees_tab_content()
        self.set_results_tab_content()
        self.set_store_tab_content()


    def top_menue(self):

        self.menubar = Menu(self)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Staff registration", command=self.donothing)
        self.filemenu.add_command(label="Staff payment", command=self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="STAFF", menu=self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=self.donothing)
        self.helpmenu.add_command(label="About...", command=self.donothing)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=self.menubar)




    def donothing(self):
        filewin = Toplevel(self)
        button = Button(filewin, text="Do nothing button")
        button.pack()


    def Nbook(self):
        self.tab_control = ttk.Notebook(self)

        self.Registration_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Registration_tab, text="Registration")

        self.Fees_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Fees_tab, text="Fees")
        self.title("cyber school  uganda  0753049317 jonahwalakira650@gmail.com")
        self.Results_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Results_tab, text="Results")

        self.Store_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.Store_tab, text="Store/Equipments")

        self.tab_control.place(relheight=1, relwidth=1)

    def set_Registration_tab_content(self):
        self.Detailsframe = LabelFrame(self.Registration_tab, text="Student Details")
        self.Detailsframe.place(relheight=0.2, relwidth=0.9,relx=0.05)
        self.idlb = ttk.Label(self.Detailsframe, text="Student/Pupil ID:")
        self.idlb.place(relheight=0.7, relwidth=0.1)
        self.stuentv = StringVar()
        self.stuent = ttk.Entry(self.Detailsframe, textvariable=self.stuentv)
        self.stuent.place(relheight=0.5, relwidth=0.5, rely=0.0, relx=0.15)
        self.viewbtn = ttk.Button(self.Detailsframe, text="View ", command=self.donothing1)
        self.viewbtn.place(relheight=0.5, relwidth=0.2, rely=0.0, relx=0.75)

        self.Registerframe = LabelFrame(self.Registration_tab, text="Register New Student")
        self.Registerframe.place(relheight=0.73, relwidth=0.9, relx=0.05,rely=0.23)
        self.sirnamelb = ttk.Label(self.Registerframe, text="Sir Name:")
        self.sirnamelb.place(relheight=0.05, relwidth=0.1)
        self.snamev = StringVar()
        self.sname = ttk.Entry(self.Registerframe, textvariable=self.snamev)
        self.sname.place(relheight=0.05, relwidth=0.2,relx=0.1)
        self.secnamelb = ttk.Label(self.Registerframe, text="Second Name:")
        self.secnamelb.place(relheight=0.05, relwidth=0.1,relx=0.3)
        self.secnamev = StringVar()
        self.secname = ttk.Entry(self.Registerframe, textvariable=self.secnamev)
        self.secname.place(relheight=0.05, relwidth=0.2,relx=0.4)
        self.Onamelb = ttk.Label(self.Registerframe, text="Other Names:")
        self.Onamelb.place(relheight=0.05, relwidth=0.1, relx=0.6)
        self.otnamev = StringVar()
        self.otname = ttk.Entry(self.Registerframe, textvariable=self.otnamev)
        self.otname.place(relheight=0.05, relwidth=0.2, relx=0.7)
        #########################################
        self.Reslb = ttk.Label(self.Registerframe, text="Residence:")
        self.Reslb.place(relheight=0.05, relwidth=0.1,rely=0.2)
        self.Residv = StringVar()
        self.Resid = ttk.Entry(self.Registerframe, textvariable=self.Residv)
        self.Resid.place(relheight=0.05, relwidth=0.2, relx=0.1,rely=0.2)
        self.Natlb = ttk.Label(self.Registerframe, text="Nationality:")
        self.Natlb.place(relheight=0.05, relwidth=0.1, relx=0.3,rely=0.2)
        self.Natv = StringVar()
        self.Nat = ttk.Entry(self.Registerframe, textvariable=self.Natv)
        self.Nat.place(relheight=0.05, relwidth=0.2, relx=0.4,rely=0.2)
        self.Schlb = ttk.Label(self.Registerframe, text="Former School:")
        self.Schlb.place(relheight=0.05, relwidth=0.1, relx=0.6,rely=0.2)
        self.Schv = StringVar()
        self.Sch = ttk.Entry(self.Registerframe, textvariable=self.Schv)
        self.Sch.place(relheight=0.05, relwidth=0.2,relx=0.7,rely=0.2)

        # ###############
        #########################################
        self.btlb = ttk.Label(self.Registerframe, text="Date of Birth:")
        self.btlb.place(relheight=0.05, relwidth=0.1, rely=0.3)
        self.dtv = StringVar()
        self.dt = ttk.Entry(self.Registerframe, textvariable=self.dtv)
        self.dt.place(relheight=0.05, relwidth=0.2, relx=0.1, rely=0.3)
        self.mnlb = ttk.Label(self.Registerframe, text="Mothers names:")
        self.mnlb.place(relheight=0.05, relwidth=0.1, relx=0.3, rely=0.3)
        self.Mnv = StringVar()
        self.Mn = ttk.Entry(self.Registerframe, textvariable=self.Mnv)
        self.Mn.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.3)
        self.mclb = ttk.Label(self.Registerframe, text="Mothers contact :")
        self.mclb.place(relheight=0.05, relwidth=0.1, relx=0.6, rely=0.3)
        self.mcv = StringVar()
        self.mc = ttk.Entry(self.Registerframe, textvariable=self.mcv)
        self.mc.place(relheight=0.05, relwidth=0.2, relx=0.7, rely=0.3)

        # ###############

        # other rely=0.03
        #########################################
        self.glb = ttk.Label(self.Registerframe, text="Gender:")
        self.glb.place(relheight=0.05, relwidth=0.1, rely=0.4)

        self.Rvar = StringVar()
        self.A = Radiobutton(self.Registerframe, text="Male", variable=self.Rvar, value="M",  anchor=W, wraplength=500)
        self.A.place(relheight=0.05, relwidth=0.1, rely=0.4)
        self.B = Radiobutton(self.Registerframe, text="Female", variable=self.Rvar, value="F",anchor=W, wraplength=500)
        self.B.place(relheight=0.05, relwidth=0.1, rely=0.4,relx=0.2)
        self.classlb = ttk.Label(self.Registerframe, text="Class:")
        self.classlb.place(relheight=0.05, relwidth=0.1, rely=0.4,relx=0.3)
        self.CA = tk.StringVar()
        self.qzichoiceKombo = ttk.Combobox(self.Registerframe,  textvariable=self.CA)
        self.qzichoiceKombo['state'] = 'readonly'
        self.qzichoiceKombo['values'] = ('Day care','Babby',' Middle','Top','P1','P2','P3','P4','P5','P6','P7',)
        self.qzichoiceKombo.current()
        self.qzichoiceKombo.place(relheight=0.05, relwidth=0.1, rely=0.4,relx=0.4)
        # ###############
        #########################################
        self.viewbtn = ttk.Button(self.Registerframe, text="Register", command=lambda : self.view_student_details())
        self.viewbtn.place(relheight=0.05, relwidth=0.2, relx=0.3, rely=0.6)
        self.Clearbtn = ttk.Button(self.Registerframe, text="Clear", command=self.clear)
        self.Clearbtn.place(relheight=0.05, relwidth=0.2, relx=0.7, rely=0.6)
        # ###############

    def donothing1(self):
        self.filewin = Toplevel(self)
        self.Registerframe = Frame(self.filewin)
        self.Registerframe.place(relheight=1, relwidth=1)

        # self.sirnamelb = ttk.Label(self.Registerframe, text="shows table values of selected class in com")
        # self.sirnamelb.place(relheight=1, relwidth=1)
        self.columnsi = ('Student_id', 'Sirname', 'lastname', 'Fees_paid', 'Balance', 'continues_Balance')
        self.fees_t = ttk.Treeview(self.Registerframe, columns=self.columnsi, show='headings')
        self.fees_t.heading('Student_id', text='Student_i')
        self.fees_t.heading('Sirname', text='sirname')
        self.fees_t.heading('lastname', text='lastname')
        self.fees_t.heading('Fees_paid', text='Fees_paid')
        self.fees_t.heading('Balance', text='Term_Balance')
        self.fees_t.heading('continues_Balance', text='Old_Balance')
        self.fees_t.place(relheight=1, relwidth=0.92)
        self.scrollbar = ttk.Scrollbar(self.Registerframe, orient=tk.VERTICAL, command=self.fees_t.yview)

        self.fees_t.bind('<<TreeviewSelect>>', self.item_selected)
        self.fees_t.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(relheight=1, relwidth=0.08, relx=0.92)
        try:
            self.z = datacon()
            self.data=  self.z.view_stable_d()
            for da in self.data:

                self.fees_t.insert('', tk.END, values=da)

            print("connection sussfull")
        except:
            print("failed")
        # self.contacts = []
        # for n in range(1, 100):
        #     self.contacts.append((f'student_id{n}', f'Sirname{n}', f'lastname{n}', f'Fees_paid{n}', f'Balance{n}',
        #                           f'continues_Balance{n}'))
        # for contact in self.contacts:
        #     self.fees_t.insert('', tk.END, values=contact)

    #gets text id and checks if it exists in the school databese
    #if student exist returns form with details else retrns erro diagle
    def view_student_details(self):
        self.sname.get()
        self.secname.get()
        self.otname.get()
        self.dt.get()
        self.Rvar.get()
        self.qzichoiceKombo.get()
        self.Resid.get()
        self.Sch.get()
        self.Nat.get()
        self.Mn.get()
        self.mc.get()
        try:
            z = datacon()
            z.reg_new_pupil(self.sname.get(),self.secname.get(),self.otname.get(),self.dt.get(),self.Rvar.get(),self.qzichoiceKombo.get(),self.Resid.get(),self.Sch.get(),self.Nat.get(),self.Mn.get(),self.mc.get())

            messagebox.showinfo("Views method",f"Sir Name : {self.sname.get() } " 
                                                 f"saved as new student in  {self.qzichoiceKombo.get()} class")
            self.clear()
        except:
            print("error encountered")

    def create_student_id(self):
        #smp/2018/31178
        pass

    def clear(self):
        self.sname.delete("0", "end")
        self.secname.delete("0", "end")
        self.otname.delete("0", "end")
        self.Resid.delete("0", "end")
        self.Nat.delete("0", "end")
        self.Sch.delete("0", "end")
        self.dt.delete("0", "end")
        self.Mn.delete("0", "end")
        self.mc.delete("0", "end")

    def set_fees_tab_content(self):
        self.Detailsframe = LabelFrame(self.Fees_tab, text="Student/class Fess Details")
        self.Detailsframe.place(relheight=0.2, relwidth=0.9, relx=0.05)

        self.idlb = ttk.Label(self.Detailsframe, text="Student/Pupil ID:")
        self.idlb.place(relheight=0.7, relwidth=0.1)
        self.stuentv = StringVar()
        self.stuent = ttk.Entry(self.Detailsframe, textvariable=self.stuentv)
        self.stuent.place(relheight=0.5, relwidth=0.5, rely=0.0, relx=0.15)
        self.feesbtn = ttk.Button(self.Detailsframe, text="Pay Fees", command=lambda :self.payfees_ui())
        self.feesbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0)
        self.Uniformbtn = ttk.Button(self.Detailsframe, text="Uniform", command=lambda : self.buy_uniform())
        self.Uniformbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.15)
        self.paperworkbtn = ttk.Button(self.Detailsframe, text="Exam/paperwork", command=self.donothing)
        self.paperworkbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.25)

        self.Daycarebtn = ttk.Button(self.Detailsframe, text="1-Daycare", command=self.donothing)
        self.Daycarebtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.35)


        self.viewbtn = ttk.Button(self.Detailsframe, text="View stutdent", command=self.donothing)
        self.viewbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.45)



        self.viewbtn2 = ttk.Button(self.Detailsframe, text="View Class", command=lambda :self.donothing1())
        self.viewbtn2.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.55)
        self.CA = tk.StringVar()
        self.qzichoiceKombo = ttk.Combobox(self.Detailsframe, textvariable=self.CA)
        self.qzichoiceKombo['state'] = 'readonly'
        self.qzichoiceKombo['values'] = (
        'Day care', 'Babby', ' Middle', 'Top', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7')
        self.qzichoiceKombo.current()
        self.qzichoiceKombo.place(relheight=0.5, relwidth=0.2, rely=0.0, relx=0.65)

        self.Registerframe = LabelFrame(self.Fees_tab, text="Class details")
        self.Registerframe.place(relheight=0.73, relwidth=0.9, relx=0.05, rely=0.23)

        # self.sirnamelb = ttk.Label(self.Registerframe, text="shows table values of selected class in com")
        # self.sirnamelb.place(relheight=1, relwidth=1)
        self.columnsi = ('Student_id','Sirname','lastname','Fees_paid','Balance','continues_Balance')
        self.fees_t=ttk.Treeview(self.Registerframe,columns=self.columnsi,show='headings')
        self.fees_t.heading('Student_id', text='Student_i')
        self.fees_t.heading('Sirname', text='sirname')
        self.fees_t.heading('lastname', text='lastname')
        self.fees_t.heading('Fees_paid', text='Fees_paid')
        self.fees_t.heading('Balance', text='Term_Balance')
        self.fees_t.heading('continues_Balance', text='Old_Balance')
        self.fees_t.place(relheight=1, relwidth=0.92)
        self.scrollbar = ttk.Scrollbar(self.Registerframe, orient=tk.VERTICAL, command=self.fees_t.yview)

        self.fees_t.bind('<<TreeviewSelect>>', self.item_selected)
        self.fees_t.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(relheight=1, relwidth=0.08,relx=0.92)
        self.contacts = []
        for n in range(1, 100):
            self.contacts.append((f'student_id{n}',f'Sirname{n}',f'lastname{n}',f'Fees_paid{n}',f'Balance{n}',f'continues_Balance{n}'))
        for contact in self.contacts:
            self.fees_t.insert('', tk.END, values=contact)
    def item_selected(self):
        for selected_item in self.fees_t.selection():
            self.item = self.fees_t.item(selected_item)
            self.record = self.item['values']
            # show a message
            self.messagebox.showinfo(title='Information', message=','.join(self.record))

    def payfees_ui(self):
        self.filewin = Toplevel(self)
        self.Registerframe = Frame(self.filewin)
        self.Registerframe.place(relheight=1, relwidth=1)

        self.stidlb = ttk.Label(self.Registerframe, text="Student ID:")
        self.stidlb.place(relheight=0.1, relwidth=0.2,relx=0,rely=0)
        self.stuidv = StringVar()
        self.pupilidentry = ttk.Entry(self.Registerframe, textvariable=self.stuidv)
        self.pupilidentry.place(relheight=0.1, relwidth=0.3,relx=0.2,rely=0)
        self.findbtn = ttk.Button(self.Registerframe, text="Find", command=lambda :self.checkstudent())
        self.findbtn.place(relheight=0.1, relwidth=0.2,relx=0.6,rely=0)

        self.amountlb = ttk.Label(self.Registerframe, text="Amount:")
        self.amountlb.place(relheight=0.1, relwidth=0.2,relx=0,rely=0.15)
        self.amountrec = StringVar()#needs to be converted to intvar
        self.pamountrec = ttk.Entry(self.Registerframe, textvariable=self.amountrec)
        self.pamountrec.place(relheight=0.1, relwidth=0.6,relx=0.2,rely=0.15)
        self.rcvdlb = ttk.Label(self.Registerframe, text="Received by:")
        self.rcvdlb.place(relheight=0.1, relwidth=0.2,relx=0,rely=0.35)
        self.amountrecby = StringVar()  # needs to be converted to intvar
        self.amountrecbyent = ttk.Entry(self.Registerframe, textvariable=self.amountrecby)
        self.amountrecbyent.place(relheight=0.1, relwidth=0.4,relx=0.2,rely=0.35)
        self.uploadbtn = ttk.Button(self.Registerframe, text="Submit", command=lambda: self.upload_paidfees())
        self.uploadbtn.place(relheight=0.1, relwidth=0.25, relx=0.6, rely=0.5)
    def checkstudent(self):
        print("checks in student details if student exists")
    def upload_paidfees(self):
        print("uploads fees in the paid fees table")

    def buy_uniform(self):
        self.filewin = Toplevel(self)
        self.stuidlb1=Label(self.filewin ,text="Student_ID:")
        self.eidv = StringVar()  # needs to be converted to intvar
        self.entdid=Entry(self.filewin, textvariable=self.eidv)
        self.finbtn=Button(self.filewin,text="find")
        self.fuln=IntVar()
        self.fuluni=Checkbutton(self.filewin,
                                variable=self.fuln,
                                text="Full Set",
                                onvalue=1,
                                offvalue=0)
        self.hamount = Label(self.filewin,text="Amount")

        self.shirtv = IntVar()
        self.shirt = Checkbutton(self.filewin,
                                  variable=self.shirtv,
                                  text="Shirt",
                                  onvalue=1,
                                  offvalue=0)

        self.Ssshortv = IntVar()
        self.Ssshort= Checkbutton(self.filewin,
                                  variable=self.Ssshortv,
                                  text="School Short",
                                  onvalue=1,
                                  offvalue=0)

        self.Sshirtv = IntVar()
        self.Sshirt = Checkbutton(self.filewin,
                                 variable=self.Sshirtv,
                                 text="Sports Shirt",
                                 onvalue=1,
                                 offvalue=0)

        self.Sshortv = IntVar()
        self.Sshort = Checkbutton(self.filewin,
                                  variable=self.Sshortv,
                                  text="Sports Short",
                                  onvalue=1,
                                  offvalue=0)

        self.Dressv = IntVar()
        self.Dress = Checkbutton(self.filewin,
                                  variable=self.Dressv,
                                  text="Dress",
                                  onvalue=1,
                                  offvalue=0)

        self.Sweaterv = IntVar()
        self.Sweater = Checkbutton(self.filewin,
                                 variable=self.Sweaterv,
                                 text="Sweater",
                                 onvalue=1,
                                 offvalue=0)

        self.Stockingsv = IntVar()
        self.Stockings = Checkbutton(self.filewin,
                                   variable=self.Stockingsv,
                                   text="Stockings",
                                   onvalue=1,
                                   offvalue=0)

        self.Scarfv = IntVar()
        self.Scarf = Checkbutton(self.filewin,
                                     variable=self.Scarfv,
                                     text="Scarf",
                                     onvalue=1,
                                     offvalue=0)
        self.Tiev = IntVar()
        self.Tie = Checkbutton(self.filewin,
                                 variable= self.Tiev,
                                 text="Tie",
                                 onvalue=1,
                                 offvalue=0)

        self.Purchasebtn = ttk.Button(self.filewin, text="Purchase", command=lambda: self.Buy_uniform())




        self.stuidlb1.grid(row=0,column=0,sticky=E,pady=2)
        self.entdid.grid(row=0,column=1,sticky=E,pady=2)
        self.finbtn.grid(row=0,column=2,sticky=E,pady=2)
        self.fuluni.grid(row=1,column=0,columnspan=2,sticky=E,pady=2)
        self.hamount.grid(row=1,column=2,sticky=W,pady=5)
        self.shirt.grid(row=2,column=0,sticky=E,pady=2)
        self.Ssshort.grid(row=2,column=1,sticky=E,pady=2)
        self.Tie.grid(row=2,column=2,sticky=E,pady=2)
        self.Sshirt.grid(row=3,column=0,sticky=E,pady=2)
        self.Sshort.grid(row=3,column=1,sticky=E,pady=2)
        self.Dress.grid(row=3,column=2,sticky=E,pady=2)
        self.Sweater.grid(row=4,column=0,sticky=E,pady=2)
        self.Stockings.grid(row=4,column=1,sticky=E,pady=2)
        self.Scarf.grid(row=4,column=2,sticky=E,pady=2)
        self.Purchasebtn.grid(row=5,column=0,columnspan=2,sticky=E,pady=2)


    def check_selected_uniform(self):
        self.zigdy=[]
        print("returns selected uniform choice returns")
        print("use dictionaries to map uniform name tagg to prices")
        return self.zigdy
    def Buy_uniform(self):
        self.selecteduni=self.check_selected_uniform()
        if len(self.selecteduni) <=0:
            print("cant take null values")
        else:
            print("inserted selected items")

    def set_results_tab_content(self):
        self.Detailsframe = LabelFrame(self.Results_tab, text="Student/class Fess Details")
        self.Detailsframe.place(relheight=0.2, relwidth=0.9, relx=0.05)
        self.idlb = ttk.Label(self.Detailsframe, text="Student/Pupil ID:")
        self.idlb.place(relheight=0.7, relwidth=0.1)
        self.stuentv = StringVar()
        self.stuent = ttk.Entry(self.Detailsframe, textvariable=self.stuentv)
        self.stuent.place(relheight=0.5, relwidth=0.5, rely=0.0, relx=0.15)

        self.paperworkbtn = ttk.Button(self.Detailsframe, text="Student marks", command=self.donothing)
        self.paperworkbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.25)

        self.Daycarebtn = ttk.Button(self.Detailsframe, text="view marks", command=self.donothing)
        self.Daycarebtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.35)

        self.viewbtn = ttk.Button(self.Detailsframe, text="Upload marks", command=self.donothing)
        self.viewbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.45)

        self.viewbtn2 = ttk.Button(self.Detailsframe, text="Edit marks", command=lambda: self.donothing1())
        self.viewbtn2.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.55)
        self.CA = tk.StringVar()
        self.qzichoiceKombo = ttk.Combobox(self.Detailsframe, textvariable=self.CA)
        self.qzichoiceKombo['state'] = 'readonly'
        self.qzichoiceKombo['values'] = (
            'Day care', 'Babby', ' Middle', 'Top', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7')
        self.qzichoiceKombo.current()
        self.qzichoiceKombo.place(relheight=0.5, relwidth=0.2, rely=0.0, relx=0.65)

        self.Registerframe = LabelFrame(self.Results_tab, text="Class marks")
        self.Registerframe.place(relheight=0.73, relwidth=0.9, relx=0.05, rely=0.23)

        # self.sirnamelb = ttk.Label(self.Registerframe, text="shows table values of selected class in com")
        # self.sirnamelb.place(relheight=1, relwidth=1)
        self.columnsi = ('Student_id', 'Sirname', 'lastname', 'Eng', 'SST', 'SCI','MTC','AVG','AGT')
        self.fees_t = ttk.Treeview(self.Registerframe , columns=self.columnsi, show='headings')
        self.fees_t.heading('Student_id', text='Student_i')
        self.fees_t.heading('Sirname', text='sirname')
        self.fees_t.heading('lastname', text='lastname')
        self.fees_t.heading('Eng', text='Eng')
        self.fees_t.heading('SST', text='SST')
        self.fees_t.heading('MTC', text='MTC')
        self.fees_t.heading('AVG', text='AVG')
        self.fees_t.heading('AGT', text='AGT')
        self.fees_t.place(relheight=1, relwidth=0.92)
        self.vscrollbar = ttk.Scrollbar(self.Registerframe, orient=tk.VERTICAL, command=self.fees_t.yview)

        self.fees_t.bind('<<TreeviewSelect>>', self.item_selected)
        self.fees_t.configure(yscroll=self.vscrollbar.set)
        self.vscrollbar.place(relheight=1, relwidth=0.05, relx=0.92)

        self.hscrollbar = ttk.Scrollbar(self.Registerframe, orient=tk.HORIZONTAL, command=self.fees_t.xview)
        self.fees_t.configure(xscroll=self.hscrollbar.set)
        self.hscrollbar.place(relheight=0.05, relwidth=1, rely=0.97)
        self.contacts = []
        for n in range(1, 5101):
            self.contacts.append((f'student_id{n}', f'Sirname{n}', f'lastname{n}', f'{n}', f'{n}',
                                  f'{n}', f'{n}', f'{n}'))
        for contact in self.contacts:
            self.fees_t.insert('', tk.END, values=contact)


    def set_store_tab_content(self):

        self.Detailsframe = LabelFrame(self.Store_tab, text="Student/class Fess Details")
        self.Detailsframe.place(relheight=0.2, relwidth=0.9, relx=0.05)
        self.idlb = ttk.Label(self.Detailsframe, text="Student/Pupil ID:")
        self.idlb.place(relheight=0.7, relwidth=0.1)
        self.stuentv = StringVar()
        self.stuent = ttk.Entry(self.Detailsframe, textvariable=self.stuentv)
        self.stuent.place(relheight=0.5, relwidth=0.5, rely=0.0, relx=0.15)

        self.paperworkbtn = ttk.Button(self.Detailsframe, text="product flow", command=self.donothing)
        self.paperworkbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.25)

        self.Daycarebtn = ttk.Button(self.Detailsframe, text="Product statics", command=self.donothing)
        self.Daycarebtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.35)

        self.viewbtn = ttk.Button(self.Detailsframe, text="New item", command=self.donothing)
        self.viewbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.45)

        self.viewbtn2 = ttk.Button(self.Detailsframe, text="Outgoing", command=lambda: self.donothing1())
        self.viewbtn2.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.55)
        self.CA = tk.StringVar()
        self.qzichoiceKombo = ttk.Combobox(self.Detailsframe, textvariable=self.CA)
        self.qzichoiceKombo['state'] = 'readonly'
        self.qzichoiceKombo['values'] = (
            'Day care', 'Babby', ' Middle', 'Top', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7')
        self.qzichoiceKombo.current()
        self.qzichoiceKombo.place(relheight=0.5, relwidth=0.2, rely=0.0, relx=0.65)

        self.Registerframe = LabelFrame(self.Store_tab, text="Class marks")
        self.Registerframe.place(relheight=0.73, relwidth=0.9, relx=0.05, rely=0.23)

        # self.sirnamelb = ttk.Label(self.Registerframe, text="shows table values of selected class in com")
        # self.sirnamelb.place(relheight=1, relwidth=1)
        self.columnsi = ('item_id', 'Item_name', 'Instock')
        self.fees_t = ttk.Treeview(self.Registerframe, columns=self.columnsi, show='headings')
        self.fees_t.heading('item_id', text='item_id')
        self.fees_t.heading('Item_name', text='Item_name')
        self.fees_t.heading('Instock', text='Instock')


        self.fees_t.place(relheight=1, relwidth=0.92)
        self.vscrollbar = ttk.Scrollbar(self.Registerframe, orient=tk.VERTICAL, command=self.fees_t.yview)

        self.fees_t.bind('<<TreeviewSelect>>', self.item_selected)
        self.fees_t.configure(yscroll=self.vscrollbar.set)
        self.vscrollbar.place(relheight=1, relwidth=0.05, relx=0.97)


        self.contacts = []
        for n in range(1, 5101):
            self.contacts.append((f'{n}', f'{n}', f'{n}'))
        for contact in self.contacts:
            self.fees_t.insert('', tk.END, values=contact)


z=home()
z.mainloop()