import base64
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
 

import math



def mod_inv(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x

def nxtprimegen(n):
    m = n
    n = n + 100
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            if p > m:
                return p
            else:
                val = p

    return val


def rsa(p,q):
    p = int(p)
    q = int(q)
    p=nxtprimegen(p)
    q=nxtprimegen(q)
    print("prime: ", p, " ", q)
    n = p * q
    print("n: ", n)
    phi = (p - 1) * (q - 1)
    e = 2
    while (1):
        if math.gcd(e, phi) == 1:
            break
        else:
            e += 1
    print("public key: ", e)
    d = mod_inv(e, phi)
    if d == 1:
        print("no multiplicative_inverse")
        return

    print("private key: ", d)
    return e, d, n
    


def encryption():
    global screen6
    #screen3.destroy()
    screen6 = Toplevel(screen)
    screen6.title("Encryption")
    screen6.geometry("300x400")
    file1 = filedialog.askopenfilename()
    
    with open(username1,"r") as f:
        lines = f.read().splitlines()
    ee = int(lines[2])
    dd = int(lines[3])
    nn = int(lines[4])
    
    with open(file1, "rb") as image:
        f = image.read()
        msg = bytearray(f)
    en = []
    de = []

    for x in msg:
        en.append(pow(x, ee, nn))
    #print("\nencrypt msg: ", en)
    ss = ""
    f3 = open(file1+'.bin', 'w')
    for x in en:
        ss += (str(x) + " ")

    f3.write(ss)
    f3.close()
    os.remove(file1)
    messagebox.showinfo("Success!","Encryption Complete")
    screen6.destroy()



def decryption():
    #screen3.destroy()
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Decryption")
    screen7.geometry("300x400")
    file1 = filedialog.askopenfilename()
    print(file1)
    #Label(screen7, text = file1).pack()
    
    with open(username1,"r") as f:
        lines = f.read().splitlines()
    ee = int(lines[2])
    dd = int(lines[3])
    nn = int(lines[4])
    print(ee)
    print(dd)
    print(nn)
    en = []
    de = []
    f3 = open(file1, 'r')
    str2=f3.read()
    en2 = str2.split(" ")
    f3.close()
    for x in en2:
        if len(x) > 0:
            en.append(int(x))
    for x in en:
        de.append(pow(x, dd, nn))
    bytearray(de[:4])
    f2 = open(file1[:-4], 'wb')
    f2.write(bytearray(de))
    f2.close()
    #print("decrypt msg: ", de)
    os.remove(file1)
    messagebox.showinfo("Success!","Decryption Complete")
    screen7.destroy()




def delete2():
    screen3.destroy()
 
def delete3():
    screen4.destroy()
 
def delete4():
    screen5.destroy()



def logout():
    screen3.destroy()
    screen.destroy()
    main_screen()
    
    
def login_sucess():
    global screen3
    screen2.destroy()
    screen3 = Toplevel(screen)
    screen3.title("Encrypt or Decrypt")
    screen3.geometry("300x400")
    Label(screen3, text = "Login Successful").pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Encrypt", height = "2", font = ("Calibri", 11),command =encryption).pack()
    Label(screen3, text = "").pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Decrypt", height = "2", font = ("Calibri", 11),command =decryption).pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Logout", height = "2", font = ("Calibri", 11),command =logout).pack()
    screen3.mainloop()


 
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text = "Password Error").pack()
    Button(screen4, text = "OK", command =delete3).pack()
 
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text = "User Not Found").pack()
    Button(screen5, text = "OK", command =delete4).pack()
 
   
def register_user():
    print("working")
   
    username_info = username.get()
    password_info = password.get()
    
    exists = os.path.isfile(username.get())
    if exists:
        messagebox.showerror("Error!","Username already exists")
    else:
        primep_info = primep.get()
        primeq_info = primeq.get()
        file=open(username_info, "w")
        file.write(username_info+"\n")
        file.write(password_info+"\n")
        e, d, n = rsa(primep.get(),primeq.get())
        file.write(str(e)+"\n")
        file.write(str(d)+"\n")
        file.write(str(n)+"\n")
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        primep_entry.delete(0, END)
        primeq_entry.delete(0, END)
        messagebox.showinfo("Complete","Signup Successful")
        screen1.destroy()
    
  
 
def login_verify():
   
    global username1
    username1 = username_verify.get()
    print(username1)
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
 
    else:
        user_not_found()
   
 
 
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x400")
   
    global username
    global password
    global username_entry
    global password_entry
    global primep
    global primeq
    global primep_entry
    global primeq_entry
    username = StringVar()
    password = StringVar()
    primep = StringVar()
    primeq = StringVar()
 
    Label(screen1, text = "Please enter details below", bg = "wheat", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(screen1, text = "").pack()
    
    Label(screen1, text = "Username * ",font = ("Calibri", 11)).pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    
    Label(screen1, text = "Password * ",font = ("Calibri", 11)).pack()
    password_entry =  Entry(screen1, textvariable = password)
    password_entry.pack()
    
    Label(screen1, text = "1st Number * ",font = ("Calibri", 11)).pack()
    primep_entry = Entry(screen1, textvariable = primep)
    primep_entry.pack()
    
    Label(screen1, text = "2nd Number * ",font = ("Calibri", 11)).pack()
    primeq_entry = Entry(screen1, textvariable = primeq)
    primeq_entry.pack()
    
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, font = ("Calibri", 11), command = register_user).pack()
    
    
 
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x400")
    Label(screen2, text = "Please enter details below to login", bg = "wheat", width = "300", height = "2", font = ("Calibri", 11)).pack()
    Label(screen2, text = "").pack()
 
    global username_verify
    global password_verify
   
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_entry1
    global password_entry1
   
    Label(screen2, text = "Username * ", font = ("Calibri", 11)).pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ", font = ("Calibri", 11)).pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
   
   
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x400")
    screen.title("File Locker")
    Label(text = "File Locker", bg = "wheat", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register",height = "2", width = "30", command = register).pack()
 
    screen.mainloop()
 
main_screen()