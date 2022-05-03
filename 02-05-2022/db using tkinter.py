##Clien/Server
##
##1.1 Security, Connection Handling Authentication
##1.1.1 LDAP - Lightweight Directory Access Protocol
##
##1.2 Thread Handling or Connection Handling
##
##1.3 Query Cache - Feature or mechanism which helps us speed up the query processing
##(Data Retrieval) - RAM
##
##
'''   SHOW VARIABLES LIKE 'have_query_cache';    '''

#proxySQL

##1.2 and 1.3 layers of MySQL is the main mechanism ---> Parsing, Analysis, Optimization, Caching
##Inbuilt layers (dates, times, encryption).
##
##
##SP, Triggers, Views ---> middle layer of MySQL
##
##1.4 Storage Engines ---> last layer
##
##
##
##Transaction: ACID
##
##A - Atomicity    --->  A group of operations for a transaction can either be fully done or nothing can be done,there is no half way.
##C - Consistency  --->  the data should be cosistent
##I - Isolation    --->
##D - Durability



from tkinter import *

root = Tk()
root.geometry('600x500')



##myLabel = Label(root, text = "MySQL")
##myLabel.pack()

def dbpage():
    dbframe = Frame()
    dbframe.place(x=0, y=0, width=600, height=500)

    dbButton = Button(dbframe, text = "DB Operations", command = nextpage)
    dbButton.place(x=220,y=100,height=100,width=150)

    backbutton = Button(dbframe, text = "back", command = Home)
    backbutton.place(x=400,y=330,height=50,width=100)


def oraclepage():
    oracleframe = Frame()
    oracleframe.place(x=0, y=0, width=600, height=500)

    dblabel = Label(oracleframe, text = "Oracle is not configured yet!")
    dblabel.place(x=220,y=100,height=100,width=150)

    backbutton = Button(oracleframe, text = "back", command = Home)
    backbutton.place(x=400,y=330,height=50,width=100)


def mongopage():
    mongoframe = Frame()
    mongoframe.place(x=0, y=0, width=600, height=500)

    dblabel = Label(mongoframe, text = "Mongo is not configured yet!")
    dblabel.place(x=220,y=100,height=100,width=150)

    backbutton = Button(mongoframe, text = "back", command = Home)
    backbutton.place(x=400,y=330,height=50,width=100)


def acidpage():
    acidframe = Frame()
    acidframe.place(x=0, y=0, width=500, height=500)

    acidlabel = Label(acidframe, text = """A -> Atomicity
C -> Consistency
I -> Isolation
D -> Durability""")
    #acidlabel.configure("tag_name", justify = 'center')
    acidlabel.place(x=250,y=100,width=100,height=100)
    
    backbutton = Button(acidframe, text = "back", command = nextpage)
    backbutton.place(x=400,y=330,height=50,width=100)

def select():
    selectlabel = Label(dmlframe, text = """SELECT [Column Names]
FROM Source""")
    selectlabel.place(x=70, y=200)

    clearbutton = Button(dmlframe, text = "clear example", command = selectlabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)

def insert():
    insertlabel = Label(dmlframe, text = """INSERT INTO [DestinationTable] ([Column1], [Column2],..., [ColumnN])
VALUES ([Column1_Value], [Column2_Value],..., [ColumnN_Value])""")
    insertlabel.place(x=70, y=200)

    clearbutton = Button(dmlframe, text = "clear example", command = insertlabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)

def update():
    updatelabel = Label(dmlframe, text = """UPDATE [Table_Name] 
SET [Column1] = [Value1], 
    [Column2] = [Value2],
    [ColumnN] = [ValueN]
WHERE Condition""")
    updatelabel.place(x=70, y=200)

    clearbutton = Button(dmlframe, text = "clear example", command = updatelabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)

def delete():
    deletelabel = Label(dmlframe, text = """DELETE FROM [Table_Name]
WHERE Condition""")
    deletelabel.place(x=70, y=200)

    clearbutton = Button(dmlframe, text = "clear example", command = deletelabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)


def dmlpage():
    global dmlframe
    dmlframe = Frame()
    dmlframe.place(x=0, y=0, width=500, height=500)    


    selectbutton = Button(dmlframe, text = "SELECT", command = select)
    selectbutton.place(x=100,y=100,height=50,width=70)

    insertbutton = Button(dmlframe, text = "INSERT", command = insert)
    insertbutton.place(x=190,y=100,height=50,width=70)

    updatebutton = Button(dmlframe, text = "UPDATE", command = update)
    updatebutton.place(x=280,y=100,height=50,width=70)

    deletebutton = Button(dmlframe, text = "DELETE", command = delete)
    deletebutton.place(x=370,y=100,height=50,width=70)
    
    backbutton = Button(dmlframe, text = "back", command = nextpage)
    backbutton.place(x=400,y=330,height=50,width=100)


def create():
    createlabel = Label(ddlframe, text = """CREATE TABLE [TableName]
(
    Column_Name1 Data_Type(Size) [NULL | NOT NULL],
    Column_Name2 Data_Type(Size) [NULL | NOT NULL],
     …
    Column_NameN Data_Type(Size) [NULL | NOT NULL]
);""")
    createlabel.place(x=70, y=200)

    clearbutton = Button(ddlframe, text = "clear example", command = createlabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)

def drop():
    droplabel = Label(ddlframe, text = """DROP TABLE table_name""")
    droplabel.place(x=70, y=200)

    clearbutton = Button(ddlframe, text = "clear example", command = droplabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)

def alter():
    alterlabel = Label(ddlframe, text = """ALTER TABLE [Table_Name]
ADD [New_Column_Name] Data_Type (Length) NULL | NOT NULL""")
    alterlabel.place(x=70, y=200)

    clearbutton = Button(ddlframe, text = "clear example", command = alterlabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)

def truncate():
    truncatelabel = Label(ddlframe, text = """TRUNCATE TABLE Database_Name.Schema_Name.Table_Name""")
    truncatelabel.place(x=70, y=200)

    clearbutton = Button(ddlframe, text = "clear example", command = truncatelabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)

def rename():
    renamelabel = Label(ddlframe, text = """SP_RENAME '[Old Table Name]', '[New Table Name]'""")
    renamelabel.place(x=70, y=200)

    clearbutton = Button(ddlframe, text = "clear example", command = renamelabel.destroy)
    clearbutton.place(x=200, y=330, height=50, width=100)


def ddlpage():
    global ddlframe
    ddlframe = Frame()
    ddlframe.place(x=0, y=0, width=500, height=500)    


    createbutton = Button(ddlframe, text = "CREATE", command = create)
    createbutton.place(x=70,y=100,height=50,width=70)

    dropbutton = Button(ddlframe, text = "DROP", command = drop)
    dropbutton.place(x=160,y=100,height=50,width=70)

    alterbutton = Button(ddlframe, text = "ALTER", command = alter)
    alterbutton.place(x=250,y=100,height=50,width=70)

    truncatebutton = Button(ddlframe, text = "TRUNCATE", command = truncate)
    truncatebutton.place(x=340,y=100,height=50,width=70)

    renamebutton = Button(ddlframe, text = "RENAME", command = rename)
    renamebutton.place(x=430,y=100,height=50,width=70)


    backbutton = Button(ddlframe, text = "back", command = nextpage)
    backbutton.place(x=400,y=330,height=50,width=100)

def nextpage():
    global nextframe
    nextframe = Frame()
    nextframe.place(x=0, y=0, width=500, height=500)
    


    acidbutton = Button(nextframe, text = "ACID", command = acidpage)
    acidbutton.place(x=100,y=100,height=50,width=100)

    dmlbutton = Button(nextframe, text = "DML", command = dmlpage)
    dmlbutton.place(x=250,y=100,height=50,width=100)

    ddlbutton = Button(nextframe, text = "DDL", command = ddlpage)
    ddlbutton.place(x=400,y=100,height=50,width=100)

    backbutton = Button(nextframe, text = "back", command = dbpage)
    backbutton.place(x=400,y=330,height=50,width=100)

def Home():
    homeframe = Frame()
    homeframe.place(x=0, y=0, width=600, height=500)
    homeframe.configure()
    
    mysqlButton = Button(homeframe, text = "MySQL", command = dbpage)
    mysqlButton.place(x=200,y=50,height=100,width=150)

    oracleButton = Button(homeframe, text = "Oracle", command = oraclepage)
    oracleButton.place(x=200,y=150,height=100,width=150)

    mongoButton = Button(homeframe, text = "Mongo", command = mongopage)
    mongoButton.place(x=200,y=250,height=100,width=150)

    exitbutton = Button(homeframe, text = "exit", command = root.destroy)
    exitbutton.place(x=400,y=330,height=50,width=100)

Home()

root.mainloop()




































