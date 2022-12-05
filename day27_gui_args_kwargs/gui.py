from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
#my_label.pack(side="left")  # label'ı ekranda ortalamamızı, paketlememizi sağlar.
# pack() fonksiyonu incelenebilir. side = left, right, bottom vb, expand=True,False vb.
my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    #my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text= new_text)


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=20)
input.pack()
#print(input.get())









window.mainloop()