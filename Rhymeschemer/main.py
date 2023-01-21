import tkinter as tk
import eng_to_ipa as ipa
from random import randint


#Creates window
root = tk.Tk()
root.resizable(width=False,height=False)
root.title("Rhymeschemer")


#All widgets of the GUI
frm_main = tk.Frame(master=root)
lbl_title = tk.Label(master=frm_main,text="Type text:")
txt_main = tk.Text(master=frm_main,width=50)
#Button is tied to generate_scheme function
btn_submit = tk.Button(master=frm_main,text="Submit",width=50,height=5,command= lambda: generate_scheme())

#Packs the widgets
frm_main.pack()
lbl_title.pack()
txt_main.pack()
btn_submit.pack()


def generate_scheme():
    """
    Parameters: text (string) to be schemed

    Returns: dict with rhyme tag as key and word array as values
    
    """
    generate_hex = lambda: hex(randint(0, 16777215))


    ipa_dict = {}

    text = txt_main.get("1.0","end-1c").split()
    print(text)
    
    for words in text:

        ipa_dict[words] = ipa.convert(words)



    print(ipa_dict)

    

    word_to_ipa = {}




root.mainloop()