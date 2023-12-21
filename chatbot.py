import customtkinter as ctk

#windowswindows
root = ctk.CTk()
root.geometry("360x600+600+130")
root.resizable(width=False,height=False)
root._set_appearance_mode("dark")

# #function
def chat():
    value = ent1.get()
    while(True):
        if value == "hello":     
            l4 = ctk.CTkLabel(root,text="hello",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))   
            l4.place(x = "300",y = "100")
            l3 = ctk.CTkLabel(root,text="🥱\njaldi bol",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))
            l3.place(x = "10",y = "130")
            break

        elif value == "developer":  
            l5 = ctk.CTkLabel(root,text="developer",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))   
            l5.place(x = "250",y = "200")      
            l3 = ctk.CTkLabel(root,text="😃AKASH😂",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))
            l3.place(x = "10",y = "230")
            break

        elif value == "collage":
            l6 = ctk.CTkLabel(root,text="collage",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))   
            l6.place(x = "250",y = "300") 
            l3 = ctk.CTkLabel(root,text="VIT 🫡 AP",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))
            l3.place(x = "10",y = "330")
            break


        else:
            l7 = ctk.CTkLabel(root,text="tell me something\nabout me",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))   
            l7.place(x = "200",y = "400") 

            l3 = ctk.CTkLabel(root,text="nai bolunga!",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))
            l3.place(x = "10",y = "430")
            break

# output



#display design
l1 = ctk.CTkLabel(root,text="CHATBOT",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",25))
l1.place(x = "130",y = "10")

l2 = ctk.CTkLabel(root,text="HI,,!\n🤗",text_color="#1DB954",fg_color="#242424",bg_color="#242424",font=("Helvetica",20))
l2.place(x = "10",y = "60")

#entry
ent1 = ctk.CTkEntry(root,text_color="#bdc9c9",fg_color="#242424",bg_color="#242424",font=("Helvetica",20),height=40,width=350,corner_radius=40)
ent1.place(x = "5",y = "560")

#button
but1 = ctk.CTkButton(root,text="@>>",fg_color="#1DB954",bg_color="#242424",height=25,width=0,corner_radius=100,command=chat)
but1.place(x = "294",y = "568")


root.mainloop()