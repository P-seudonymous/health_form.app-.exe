import os
import random
import requests
from lxml import etree

x = int(input("Ener user-id"))
y = int(input("Enter password"))


from tkinter import *

root = Tk()
root.title("Health form - No time limit!")
root.iconbitmap("/Users/pseudonymous/Desktop/Coding/dps.png")
root.geometry("400x600")
bg = PhotoImage(file = "bongo-cat.gif")
my_label1 = Label(root, image = bg)
my_label1.place(x = 0, y = 0)
my_label = Label(root, text="Welcome", font=("Helvetica",16,))
my_label.pack(pady=20)








root.mainloop()

from asyncio import exceptions
payload = {'txtUserId': x , 'txtPassword' : y , 'isSubmit':"Yes"}
    
with requests.Session() as s:
    s.post('https://dpsfsis.com/Users/index.php', data=payload)
    tree = etree.HTML(s.get('https://dpsfsis.com/Admin/SelfDeclarationForm.php').text)
    sname = tree.xpath('//*[@id="frmReg"]/div/div[2]/div/p/b/span[1]')[0].text
    sadmission = tree.xpath('//*[@id="frmReg"]/div/div[2]/div/p/b/span[2]')[0].text
    sclass = tree.xpath('//*[@id="frmReg"]/div/div[2]/div/p/b/span[3]')[0].text


    temperature = str(round(random.uniform(96.8, 98.6), 1))
    pulse = str(random.randint(72, 99))
    concentration = str(random.randint(97, 99))
    health_form = {'temperature': temperature, 'pulse': pulse, 'concentration': concentration, 'suffering': "NA", 'is_submit': "Yes", 'sname': sname, 'sclass': sclass, 'sadmission': sadmission}
    s.post('https://dpsfsis.com/Admin/SelfDeclarationForm.php', data=health_form)



print("Heath Form Successfully Updated, But maybe verify")