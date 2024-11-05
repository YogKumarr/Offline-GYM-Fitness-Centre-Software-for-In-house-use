from tkinter import*
import pygame   #for sounds only
splash_root = Tk()
splash_root.geometry("1080x320+0+0")
splash_root.state('zoomed')
splash_root.configure(background='LemonChiffon2')
splash_label = Label(splash_root,text="☯\nWelcome!",bg ='LemonChiffon2',pady=340,font=("Comic Sans MS",154))
splash_label.pack()

def main():
     splash_root.destroy()

     #Execute music
     pygame.mixer.init()
     pygame.mixer.music.load("lounge.mp3")
     pygame.mixer.music.play()

     #Execute tkinter
     newroot = Tk()
     newroot.geometry("1080x320+0+0")
     newroot.title("Menu")
     newroot.state("zoomed")
     newroot.configure(background='LemonChiffon2')

     def enter1():
         newroot.destroy()
         import diygym
     def enter2():
         newroot.destroy()
         import diyfood
     press_btn = Button(newroot, text="➤DIY Fitness",width = 18, height=2, bd = 0, bg ='pink',activebackground="maroon3", pady = 5, font=("Times New Roman",54), command= enter1)
     press_btn.pack(padx = 0, pady = 5)
     press1_btn = Button(newroot, text="➤HEALTH CAFÉ",width = 18, height=2, bd = 0, bg ='silver',activebackground="thistle4", pady = 5,font=("Times New Roman",54), command= enter2)
     press1_btn.pack(padx = 0, pady = 10)
     Label_title = Label(newroot, text="❃⫷Muscle Madness⫸❃", width = 40, height=2,bg ='LemonChiffon2',font=("Times New Roman",60))
     Label_title.pack(padx=0, pady= 20)
     newroot.mainloop()

     # Set Interval for Splashscreen to end
     splash_root.after(3000,main)
