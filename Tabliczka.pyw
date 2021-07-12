import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pygame import mixer

def main():

    music = True
    good = 0
    bad = 0
    seconds = 181
    hard = 0
    hard_1 = 0
    hard_2 = 0
    hard_3 = 0
    hard_4 = 0
    lista = []

    class Base:

        def __init__(self, container):

            windowWidth = root.winfo_reqwidth()
            windowHeight = root.winfo_reqheight()
            positionRight = int(root.winfo_screenwidth() / 2.7 - windowWidth / 2.7)
            positionDown = int(root.winfo_screenheight() / 3.7 - windowHeight / 3.7)
            self.container = container
            self.container.title('Test Mnożenia')
            self.container.windowWidth = root.winfo_reqwidth()
            self.container.windowHeight = root.winfo_reqheight()
            self.container.geometry('500x600+{}+{}'.format(positionRight, positionDown))
            self.container.grid_rowconfigure(0, weight=1)
            self.container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for F in (Window_1, Window_2, Window_3):
                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(Window_1)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

    class Window_1(tk.Frame):

        def __init__(self, parent, controller):

            tk.Frame.__init__(self, parent)

            def zmiana():
                nonlocal music
                music = not music

            def go():
                test_title = tk.Label(self, text='TEST MNOŻENIA', height=20, width=50,
                                      font=("Verdana", 36, "bold", "italic"))
                test_title.pack(side="top", fill="x", pady=10)
                test_title.place(x=0, y=30, height=100, width=500)

                img = PhotoImage(file="media/button.png")
                button1 = tk.Button(self, text="Dalej", image=img, borderwidth=0, font=("Fixedsys", 36, "bold"),
                                      command=lambda: choice())
                button1.image = img
                button1.config()
                button1.pack()
                button1.place(x=150, y=450, height=110, width=200)

                r1 = Radiobutton(self, text="Łatwy", variable = c, value=0, font=("Fixedsys", 30, "bold"))
                r1.pack(anchor=W)
                r1.place(x=40, y=170)

                r2 = Radiobutton(self, text="Trudny", variable = c, value=1, font=("Fixedsys", 30, "bold"))
                r2.pack()
                r2.place(x=270, y=170)

                r3 = Radiobutton(self, text="Średni", variable=c, value=2, font=("Fixedsys", 30, "bold"))
                r3.pack()
                r3.place(x=40, y=250)
                r3.select()

                r4 = Radiobutton(self, text="Ręcznie", variable=c, value=3, font=("Fixedsys", 30, "bold"))
                r4.pack()
                r4.place(x=270, y=250)

                music_check = Checkbutton(self, text='Muzyczka ?', variable=music, command=lambda: zmiana())
                music_check.place(x=200, y=370)
                music_check.select()

                def choice():
                    nonlocal hard, hard_3, hard_4, img
                    hard = c.get()

                    if int(hard) == 3:
                        test_title.destroy()
                        button1.destroy()
                        r1.destroy()
                        r2.destroy()
                        r3.destroy()
                        r4.destroy()
                        music_check.destroy()

                        type_1 = Label(self, text='TRYB RĘCZNY', height=20, width=50,
                                      font=("Verdana", 30, "bold", "italic"))
                        type_1.pack()
                        type_1.place(x=0, y=0, height=100, width=500)

                        type_2 = Label(self, text='Pierwsza liczba', height=20, width=50,
                                      font=("Verdana", 20, "bold"))
                        type_2.pack()
                        type_2.place(x=0, y=90, height=100, width=500)

                        type_3 = Label(self, text='Druga liczba', height=20, width=50,
                                      font=("Verdana", 20, "bold"))
                        type_3.pack()
                        type_3.place(x=0, y=255, height=100, width=500)

                        type_4 = Label(self, text='OD:', height=20, width=50,
                                      font=("Verdana", 12, "bold"))
                        type_4.pack()
                        type_4.place(x=50, y=210, height=30, width=40)

                        type_5 = Label(self, text='DO:', height=20, width=50,
                                      font=("Verdana", 12, "bold"))
                        type_5.pack()
                        type_5.place(x=290, y=210, height=30, width=40)

                        type_6 = Label(self, text='OD:', height=20, width=50,
                                      font=("Verdana", 12, "bold"))
                        type_6.pack()
                        type_6.place(x=50, y=375, height=30, width=40)

                        type_7 = Label(self, text='DO:', height=20, width=50,
                                      font=("Verdana", 12, "bold"))
                        type_7.pack()
                        type_7.place(x=290, y=375, height=30, width=40)

                        entry1 = tk.Entry(self, font=('Trebuchet MS', 20, 'bold'), justify='center')
                        entry1.pack()
                        entry1.place(x=100, y=365, height=50, width=75)

                        entry2 = tk.Entry(self, font=('Trebuchet MS', 20, 'bold'), justify='center')
                        entry2.pack()
                        entry2.place(x=340, y=365, height=50, width=75)

                        entry3 = tk.Entry(self, font=('Trebuchet MS', 20, 'bold'), justify='center')
                        entry3.pack()
                        entry3.place(x=100, y=200, height=50, width=75)
                        entry3.focus_set()

                        entry4 = tk.Entry(self, font=('Trebuchet MS', 20, 'bold'), justify='center')
                        entry4.pack()
                        entry4.place(x=340, y=200, height=50, width=75)

                        img = PhotoImage(file="media/button.png")
                        button3 = tk.Button(self, text="Dalej", image=img, borderwidth=0, font=("Fixedsys", 36, "bold"),
                                            command=lambda: choice2())
                        button3.pack()
                        button3.image = img
                        button3.place(x=270, y=450, height=110, width=200)

                        img_2 = PhotoImage(file="media/wroc.png")
                        button4 = tk.Button(self, text="Dalej", image=img_2, borderwidth=0, font=("Fixedsys", 36, "bold"),
                                            command=lambda: cofnij())
                        button4.pack()
                        button4.image = img_2
                        button4.place(x=30, y=450, height=110, width=200)

                        def choice2():
                            nonlocal hard, hard_1, hard_2, hard_3, hard_4
                            hard_1 = entry3.get()
                            hard_2 = entry4.get()
                            hard_3 = entry1.get()
                            hard_4 = entry2.get()
                            if (hard_1.isdigit()) and (hard_2.isdigit()) and (hard_3.isdigit()) and (hard_4.isdigit()):
                                if int(hard_2) < int(hard_1) or int(hard_3) > int(hard_4):
                                    messagebox.showinfo('Test Mnożenia',
                                                        'Złe dane: OD: "mniejsza liczba" DO: "większa liczba" ')
                                else:
                                    controller.show_frame(Window_2)
                            else:
                                messagebox.showinfo('Test Mnożenia',
                                                    'Błąd danych')
                        def cofnij():
                            type_1.destroy()
                            type_2.destroy()
                            type_3.destroy()
                            type_4.destroy()
                            type_5.destroy()
                            type_6.destroy()
                            type_7.destroy()
                            entry1.destroy()
                            entry2.destroy()
                            entry3.destroy()
                            entry4.destroy()
                            button3.destroy()
                            button4.destroy()
                            go()
                    else:
                        controller.show_frame(Window_2)


            c = StringVar()

            go()

    class Window_2(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)

            liczba = 0
            a = 0
            b = 0



            def pytanko():

                nonlocal a, b, good, hard, hard_3, hard_4

                a = random.randint(2, 9)

                if int(hard) == 0:
                    b = random.randint(2, 9)
                if int(hard) == 1:
                    b = random.randint(11, 99)
                if int(hard) == 2:
                    b = random.randint(11, 20)
                if int(hard) == 3:
                    a = random.randint(int(hard_1), int(hard_2))
                    b = random.randint(int(hard_3), int(hard_4))

                question = tk.Label(self, text=(a, "*", b), font=("Fixedsys", 50, "bold"))
                question.pack()
                question.place(x=0, y=150, height=100, width=500)

                def check():
                    nonlocal liczba
                    liczba = button1.get()
                    sprawdzanie()
                    question.destroy()
                    pytanko()

                button1 = tk.Entry(self, font=('Trebuchet MS', 30, 'bold'), justify='center')
                button1.bind("<Return>", lambda x: check())
                button1.pack()
                button1.place(x=175, y=300, height=100, width=150)
                button1.focus_set()

            def czas():

                def timer():
                    nonlocal music, button2, seconds
                    if seconds > 0:
                        seconds = seconds - 1
                        mins = seconds // 60
                        m = str(mins)

                        if mins < 10:
                            m = '0' + str(mins)
                        se = seconds - (mins * 60)
                        s = str(se)

                        if se < 10:
                            s = '0' + str(se)
                        time.set(m + ':' + s)
                        timer_display.config(textvariable=time)
                        root.after(1000, timer)

                    elif seconds == 0:
                        messagebox.showinfo('Test Mnożenia', 'Koniec!!!')
                        controller.show_frame(Window_3)


                    if music == True:
                        if seconds == 150:
                            mixer.init()
                            mixer.music.load('media/Grieg.mp3')
                            mixer.music.play()


                pytanko()

                time = StringVar()

                timer_display = Label(self, font=('Trebuchet MS', 30, 'bold'))

                timer_display.place(x=195, y=0)
                timer()
                button2.destroy()

            def sprawdzanie():

                nonlocal a, b, good, bad, liczba, lista
                iloczyn = a*b
                if int(liczba) == iloczyn:
                    good = good + 1
                else:
                    lista.append((a, "*", b, '  -  ', 'Źle:', int(liczba), '  -  ', 'Dobrze:', iloczyn))
                    bad = bad + 1





            frames = tk.Frame(self, width=500, height=1000)

            frames.pack()
            start_img = PhotoImage(file='media/start.png')
            button2 = tk.Button(self, text="START", image=start_img, borderwidth=0, font=("Fixedsys", 36, "bold"),
                                command=lambda: czas())
            button2.image = start_img
            button2.config()
            button2.pack()
            button2.place(x=150, y=400, height=110, width=200)

            timer_display = Label(self, font=('Trebuchet MS', 30, 'bold'))

            timer_display.place(x=200, y=0)

    class Window_3(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)

            nonlocal good, bad, seconds

            def wyniki():
                score.destroy()

                title = tk.Label(self, text='WYNIK', height=20, width=50, font=("Verdana", 35, "bold", "italic"))
                title.pack(fill="x", pady=10)
                title.place(x=10, y=10, height=100, width=500)

                good_box = tk.Label(self, text="Dobrze", height=20, width=50, font=("Verdana", 24, "bold", "italic"))
                good_box.pack(fill="x", pady=10)
                good_box.place(x=10, y=110, height=70, width=240)

                wrong_box = tk.Label(self, text='Źle', height=20, width=50, font=("Verdana", 24, "bold", "italic"))
                wrong_box.pack(fill="x", pady=10)
                wrong_box.place(x=260, y=110, height=70, width=240)

                good_box_sum = tk.Label(self, text=good, fg='limegreen', height=20, width=50, font=("Fixedsys", 30))
                good_box_sum.pack(fill="x", pady=10)
                good_box_sum.place(x=10, y=170, height=70, width=240)

                wrong_box_sum = tk.Label(self, text=bad, fg='red', height=20, width=50, font=("Fixedsys", 30))
                wrong_box_sum.pack(fill="x", pady=10)
                wrong_box_sum.place(x=255, y=170, height=70, width=240)

                score_box = tk.Label(self, text='Twój wynik', height=20, width=50,
                                     font=("Verdana", 24, "bold", "italic"))
                score_box.pack(side="top", fill="x", pady=10)
                score_box.place(x=10, y=240, height=70, width=480)

                score_box_sum = tk.Label(self, fg='#0059b3', text=(good - bad), height=20, width=50,
                                         font=("Fixedsys", 30))
                score_box_sum.pack(side="top", fill="x", pady=10)
                score_box_sum.place(x=10, y=300, height=70, width=480)

                def again():

                    nonlocal seconds
                    root.destroy()
                    main()

                def mistakes():

                    nonlocal lista, score_image, score
                    title.destroy()
                    good_box.destroy()
                    wrong_box.destroy()
                    good_box_sum.destroy()
                    wrong_box_sum.destroy()
                    score_box.destroy()
                    score_box_sum.destroy()
                    mistake.destroy()

                    frame = Frame(self)
                    frame.pack()
                    frame.place(x=10, y=10, height=330, width=480)

                    scrollbar = Scrollbar(frame, orient=VERTICAL)

                    wynik = Listbox(frame, borderwidth=1, yscrollcommand=scrollbar.set, font=("Verdana", 12, "bold"))
                    scrollbar.config(command=wynik.yview)
                    scrollbar.pack(side=RIGHT, fill=Y)
                    wynik.pack(side="left", fill="y")
                    wynik.insert(END, "Błędy:")
                    wynik.insert(END, " ")
                    wynik.place(height=330, width=460)

                    def re_wyniki():
                        wynik.destroy()
                        scrollbar.destroy()
                        wyniki()
                    for i in lista:
                        wynik.insert(END, i)
                        wynik.insert(END, ' ')
                    wynik_image = PhotoImage(file='media/wynik.png')
                    score = tk.Button(self, text="Wynik", image=wynik_image, borderwidth=0,
                                      font=("Fixedsys", 24, "bold"), command=lambda: re_wyniki())
                    score.image = wynik_image
                    score.place(x=150, y=370, height=72, width=200)

                restart_image = PhotoImage(file='media/restart.png')
                ok = tk.Button(self, text="Jeszcze raz?", image=restart_image, borderwidth=0,
                               font=("Fixedsys", 36, "bold"), command=lambda: again())
                ok.image = restart_image
                ok.place(x=10, y=460, height=110, width=480)

                mistake_image = PhotoImage(file='media/error.png')
                mistake = tk.Button(self, text="Błędy", image=mistake_image, borderwidth=0,
                               font=("Fixedsys", 24, "bold"), command=lambda: mistakes())
                mistake.image = mistake_image
                mistake.place(x=150, y=370, height=72, width=200)

            score_image = PhotoImage(file='media/score.png')
            score = tk.Button(self, text="Pokaż wynik", image = score_image, borderwidth=0,
                              font=("Fixedsys", 36, "bold"), command=lambda: wyniki())
            score.image = score_image
            score.place(x=10, y=235, height=110, width=480)

    root = Tk()
    gui = Base(root)
    root.mainloop()


if __name__ == '__main__':
    main()
