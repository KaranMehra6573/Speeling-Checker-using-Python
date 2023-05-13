#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter


# In[2]:


from tkinter import*


# In[3]:


from textblob import TextBlob


# In[4]:


root=Tk()


# In[5]:


root.title("Spelling Checker")


# In[6]:


root.geometry("700x400")


# In[7]:


root.config(background="#dae6f6")


# In[8]:


def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())
    
    cs=Label(root,text="Correct text is :",font=("poppins",20),bg="#dae6f6",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)


# In[9]:


heading=Label(root,text="Spelling Checker",font=("Trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))


# In[10]:


enter_text=Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2)


# In[11]:


enter_text.pack(pady=10)


# In[12]:


enter_text.focus()


# In[13]:


button=Button(root,text="check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)


# In[14]:


button.pack()


# In[15]:


spell=Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")


# In[16]:


spell.place(x=350,y=250)


# In[ ]:


root.mainloop()


# In[ ]:




