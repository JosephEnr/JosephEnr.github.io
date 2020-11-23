import tkinter as tk
import winsound

cookie = 0
audio = "True"

def music():
    winsound.Beep(400,500)
    winsound.Beep(500,500)
    winsound.Beep(600,500)
    winsound.Beep(700,800)

#Root formes the browser
root = tk.Tk()

#Forms the canvas for everything to be held in
canvas = tk.Canvas(root, height=900, width = 1000)
canvas.pack()

#Forms the backgrounds color/image
background_image = tk.PhotoImage(file="cookies.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1,relheight=1)

#Forms the frame that hold text
name_frame = tk.Frame(root,bg="light blue",bd=5)
name_frame.place(relx=0.5, rely=0.04, relwidth=0.75, relheight=0.1, anchor="n")

#Puts text on name_frame
inst = tk.Label(name_frame,text="Enter name below",font=40)
inst.place(relheight = 1, relwidth = 0.4)

def mute():
    global audio
    if audio == "True":
        audio = "False"
    else:
        audio = "True"

#Allows you to mute the site
mute = tk.Button(name_frame,text="Mute",font=40,command = mute)
mute.place(relheight=1,relwidth=0.13,relx=0.86)

#Forms the top frame where the entry and button are held
frame = tk.Frame(root, bg="light blue", bd = 5)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor="n")

#Allows text to be input and held
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65,relheight=1)

#Forms the bottom frame for the text to be held
frame2 = tk.Frame(root,bg = "light blue",bd = 10)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(frame2, text="Start clicking", bg = "#c78b42")
label.place(relwidth=0.7,relheight=1)

def end(entry):
    #Reads all the scores

    global cookie

    with open("Scores.txt","r") as file:
        scores_list = file.readlines()

    for i in range(1, len(scores_list), 2):
        if cookie > int(scores_list[i]):
            scores_list.insert(i - 1, str(cookie) + '\n')
            scores_list.insert(i - 1, str(entry) + '\n')
            del scores_list[-1]
            del scores_list[-1]
            break

    with open("Scores.txt","w") as file:
        for i in scores_list:
            file.write(i)

    exit()


def cook(entry):
    #The Label is reset whenever the button is clicked since its re defined every time
    global audio
    global cookie
    cookie = cookie + 1
    text_box = "Your name is: " + str(entry) + "\nCookies: " + str(cookie)
    label = tk.Label(frame2)
    if cookie == 100 and audio == "True":
        label = tk.Label(frame2, text=text_box, bg = "white")
        music()
    elif cookie >= 100:
        label = tk.Label(frame2, text=text_box, bg = "white")
    elif cookie == 60 and audio == "True":
        label = tk.Label(frame2, text=text_box, bg = "green")
        music()
    elif cookie >= 60:
        label = tk.Label(frame2, text=text_box, bg = "green")
    elif cookie == 30 and audio == "True":
        label = tk.Label(frame2, text=text_box, bg = "blue")
        music()
    elif cookie >= 30:
        label = tk.Label(frame2, text=text_box, bg = "blue")
    elif cookie == 10 and audio == "True":
        label = tk.Label(frame2, text=text_box, bg = "pink")
        music()
    elif cookie > 10:
        label = tk.Label(frame2, text=text_box, bg = "pink")
    elif cookie <= 10:
        label = tk.Label(frame2, text=text_box, bg = "#c78b42")
    label.place(relwidth=0.7,relheight=1)

end_button = tk.Button(name_frame, text = "End", bg = "black",fg = "red",font = 40, command = lambda: end(entry.get()))
end_button.place(relheight=1,relwidth=0.3,relx=0.48)

#Makes the button and refreshes the page due to the function
button = tk.Button(frame, text = "Cookie Click", command = lambda: cook(entry.get()), font = 40)
button.place(relx=0.7, relwidth=0.3, relheight=1)

with open("Scores.txt","r") as file:
    scores_list = file.readlines()

scores = "Top Scores:\n" + str(scores_list[0]) + "Scored:" + str(scores_list[1]) + "\n" + str(scores_list[2]) + "Scored:" + str(scores_list[3]) + "\n" + str(scores_list[4]) + "Scored:" + str(scores_list[5]) + "\n" + str(scores_list[6]) + "Scored:" + str(scores_list[7]) + "\n" + str(scores_list[8]) + "Scored:" + str(scores_list[9])
label2 = tk.Label(frame2, text=scores, bg = "black", fg = "green")
label2.place(relheight = 1, relwidth = 0.29, relx = 0.71)

root.mainloop()