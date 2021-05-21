from tkinter import *
import tkinter.messagebox as MessageBox
import sqlite3

path_to_database="mydb.db"

def addEtudiant():
    idEtudiant = e_idEtudiant.get()
    idFilliereFK = e_idFilliereFK.get()
    nom = e_nom.get()
    prenom = e_prenom.get()
    age = e_age.get()

    if(idEtudiant=="" or idFilliereFK=="" or nom=="" or prenom=="" or age==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = sqlite3.connect(path_to_database)
        cursor = con.cursor()
        cursor.execute("insert into Etudiant values('"+ idEtudiant +"','"+ idFilliereFK +"','"+ nom +"','"+ prenom +"','"+ age +"')")
        cursor.execute("commit");
        
        e_idEtudiant.delete(0,'end')
        e_idFilliereFK.delete(0,'end')
        e_nom.delete(0,'end')
        e_prenom.delete(0,'end')
        e_age.delete(0,'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully");
        con.close();

def deleteEtudiant():
    if (e_idEtudiant.get()==""):
        MessageBox.showinfo("Delete Status","IdEtudiant is compolsary for delete")
    else :
        con = sqlite3.connect(path_to_database)
        cursor = con.cursor()
        cursor.execute("delete from Etudiant where idEtudiant='"+ e_idEtudiant.get() +"'" )
        cursor.execute("commit");

        e_idEtudiant.delete(0,'end')
        e_idFilliereFK.delete(0,'end')
        e_nom.delete(0,'end')
        e_prenom.delete(0,'end')
        e_age.delete(0,'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully");
        con.close();

def updateEtudiant():
        idEtudiant = e_idEtudiant.get()
        idFilliereFK = e_idFilliereFK.get()
        nom = e_nom.get()
        prenom = e_prenom.get()
        age = e_age.get()

        if(idEtudiant=="" or idFilliereFK=="" or nom=="" or prenom=="" or age==""):
           MessageBox.showinfo("Update Status", "All Fields are required")
        else:
           con = sqlite3.connect(path_to_database)
           cursor = con.cursor()
           cursor.execute("update Etudiant set idFilliereFK='"+ idFilliereFK +"', nom='"+ nom +"',prenom='"+ nom +"',age='"+ age +"' where idEtudiant='"+ idEtudiant +"'")
           cursor.execute("commit");
        
           e_idEtudiant.delete(0,'end')
           e_idFilliereFK.delete(0,'end')
           e_nom.delete(0,'end')
           e_prenom.delete(0,'end')
           e_age.delete(0,'end')
           show()
           MessageBox.showinfo("Update Status", "Updated Successfully");
           con.close();
def show():
        con = sqlite3.connect(path_to_database)
        cursor = con.cursor()
        cursor.execute("select * from Etudiant")
        rows=cursor.fetchall()
        list.delete(0,list.size())
        inserttitle='idEt'+'         '+'idFil'+'         '+'nom'+'         '+'prenom'+'         '+'age'
        listtitle.insert(listtitle.size(),inserttitle)
        for row in rows : 
            insertData=str(row[0])+'              '+str(row[1])+'               '+row[2]+'                '+row[3]+'                '+str(row[4])
            list.insert(list.size()+1,insertData)
        con.close

def addFilliere():
        idFilliere = e_idFilliere.get()
        nomFilliere = e_nomFilliere.get()

        if (idFilliere==""or nomFilliere==""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            con = sqlite3.connect(path_to_database)
            cursor = con.cursor()
            cursor.execute("insert into Filliere values('"+ idFilliere +"','"+ nomFilliere +"')")
            cursor.execute("commit");

            e_idFilliere.delete(0,'end')
            e_nomFilliere.delete(0,'end')
            showF()
            MessageBox.showinfo("Insert Status", "Inserted Successfully");
            con.close();

def deleteFilliere():
    if (e_idFilliere.get()==""):
        MessageBox.showinfo("Delete Status","IdEtudiant is compolsary for delete")
    else :
        con = sqlite3.connect(path_to_database)
        cursor = con.cursor()
        cursor.execute("delete from Filliere where idFilliere='"+ e_idFilliere.get() +"'" )
        cursor.execute("commit");

        e_idFilliere.delete(0,'end')
        e_nomFilliere.delete(0,'end')
        showF()
        MessageBox.showinfo("Delete Status", "Deleted Successfully");
        con.close();

def updateFilliere():
        idFilliere = e_idFilliere.get()
        nomFilliere = e_nomFilliere.get()
        
        if(idFilliere=="" or nomFilliere==""):
           MessageBox.showinfo("Update Status", "All Fields are required")
        else:
           con = sqlite3.connect(path_to_database)
           cursor = con.cursor()
           cursor.execute("update Filliere set  nomFilliere='"+ nomFilliere +"' where idFilliere = '"+ idFilliere +"'")
           cursor.execute("commit");
        
           e_idFilliere.delete(0,'end')
           e_nomFilliere.delete(0,'end')
           showF()
           MessageBox.showinfo("Update Status", "Updated Successfully");
           con.close();

def showF():
        con = sqlite3.connect(path_to_database)
        cursor = con.cursor()
        cursor.execute("select * from Filliere")
        rows1=cursor.fetchall()
        list1.delete(0,list1.size())
        inserttitle1='idFilliere'+'         '+'nomFilliere'
        listtitle1.insert(listtitle1.size(),inserttitle1)
        for row1 in rows1 : 
            insertData1=str(row1[0])+'              '+row1[1]
            list1.insert(list1.size()+1,insertData1)
        con.close

    

root = Tk()
root.geometry("800x600")
root.title("MiniProjet")

idEtudiant = Label(root, text="ID de l'étudiant :",font=('bold',10))
idEtudiant.place(x=20,y=30)

idFilliereFK = Label(root, text='ID de sa filière :',font=('bold',10))
idFilliereFK.place(x=20,y=60)

nom = Label(root, text='le Nom :',font=('bold',10))
nom.place(x=20,y=90)

prenom = Label(root, text='le Prenom :',font=('bold',10))
prenom.place(x=20,y=120)

age = Label(root, text="l'age",font=('bold',10))
age.place(x=20,y=150)

idFilliere = Label(root, text='ID de la filière :',font=('bold',10))
idFilliere.place(x=20,y=350)

nomFilliere = Label(root, text=' le Nom de la filière :',font=('bold',10))
nomFilliere.place(x=20,y=380)

e_idEtudiant = Entry()
e_idEtudiant.place(x=150,y=30)

e_idFilliereFK = Entry()
e_idFilliereFK.place(x=150,y=60)

e_nom = Entry()
e_nom.place(x=150,y=90)

e_prenom = Entry()
e_prenom.place(x=150,y=120)

e_age = Entry()
e_age.place(x=150,y=150)

e_idFilliere=Entry()
e_idFilliere.place(x=150,y=350)

e_nomFilliere=Entry()
e_nomFilliere.place(x=150,y=380)

addEtudiant = Button(root, text="Ajouter Etudiant", font=("italic",10), bg="green",fg="white",command=addEtudiant)
addEtudiant.place(x=20,y=180)

deleteEtudiant = Button(root, text="Supprimer Etudiant", font=("italic",10), bg="red",command=deleteEtudiant)
deleteEtudiant.place(x=20,y=210)

updateEtudiant = Button(root, text="Modifier Etudiant", font=("italic",10), bg="white",command=updateEtudiant)
updateEtudiant.place(x=150,y=180)

addFilliere = Button(root, text="Ajouter Filière", font=("italic",10), bg="green",fg="white",command=addFilliere)
addFilliere.place(x=20,y=410)

deleteFilliere = Button(root, text="Supprimer Filière", font=("italic",10), bg="red",command=deleteFilliere)
deleteFilliere.place(x=20,y=440)

updateFilliere = Button(root, text="Modifier Filière", font=("italic",10), bg="white",command=updateFilliere)
updateFilliere.place(x=150,y=410)

listtitle=Listbox(root,width=50, height=2,bg="yellow")
listtitle.place(x=350,y=15)
list = Listbox(root, width=50, height=15)
list.place(x=350,y=30)
show()

listtitle1=Listbox(root,width=40, height=2,bg="yellow")
listtitle1.place(x=375,y=350)
list1 = Listbox(root, width=40, height=10)
list1.place(x=375,y=365)
showF()

root.mainloop()






