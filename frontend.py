from tkinter import *
from backend_v2 import Database

database=Database("books.db")


   
class Window:
   def __init__(self,window):
      self.window=window
    
      self.window.wm_title("BookStore")
      l1=Label(window, text="Title").grid(row=0,column=0)

      l2=Label(window, text="Author").grid(row=0,column=2)

      l3=Label(window, text="Year").grid(row=1,column=0)

      l4=Label(window, text="ISBN").grid(row=1,column=2)

      self.title_text=StringVar()
      self.e1=Entry(window,textvariable=self.title_text).grid(row=0,column=1)

      self.author_text=StringVar()
      self.e2=Entry(window,textvariable=self.author_text).grid(row=0,column=3)

      self.year_text=StringVar()
      self.e3=Entry(window,textvariable=self.year_text).grid(row=1,column=1)

      self.isbn_text=StringVar()
      self.e4=Entry(window,textvariable=self.isbn_text).grid(row=1,column=3)

      self.list1=Listbox(window, height=6,width=35)
      self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)
 
      sb1=Scrollbar(window)
      sb1.grid(row=2,column=2,rowspan=6)
 
      self.list1.configure(yscrollcommand=sb1.set)
      sb1.configure(command=self.list1.yview)

      self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
      self.b1=Button(window, text="View all", width=12,command=self.view_command).grid(row=2,column=3)

      self.b2=Button(window, text="Search Entry", width=12,command=self.search_command).grid(row=3,column=3)

      self.b3=Button(window, text="Add entry", width=12,command=self.add_command).grid(row=4,column=3)

      self.b4=Button(window, text="Update", width=12,command=self.update_command).grid(row=5,column=3)

      self.b5=Button(window, text="Delete", width=12,command=self.delete_command).grid(row=6,column=3)

      self.b6=Button(window, text="Close", width=12,command=window.destroy).grid(row=7,column=3)

   def get_selected_row(self,event):
      try:
         global selected_tuple  
         index=self.self.list1.curselection()[0]
         selected_tuple=self.self.list1.get(index)
         self.e1.delete(0,END)
         self.e1.insert(END,selected_tuple[1])
         self.e2.delete(0,END)
         self.e2.insert(END,selected_tuple[2])
         self.e3.delete(0,END)
         self.e3.insert(END,selected_tuple[3])
         self.e4.delete(0,END)
         self.e4.insert(END,selected_tuple[4])
      except IndexError:
         pass

   def view_command(self):
      self.list1.delete(0,END)
      for row in database.view():
         self.list1.insert(END,row)

   def search_command(self):
      self.list1.delete(0,END)
      for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
         self.list1.insert(END,row)

   def add_command(self):
      database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
      self.list1.delete(0,END)
      self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

   def delete_command(self):
      database.delete(selected_tuple[0])

   def update_command(self):
      database.update(selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())


window=Tk()
Window(window)
window.mainloop()
