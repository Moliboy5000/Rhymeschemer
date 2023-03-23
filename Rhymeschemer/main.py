import tkinter as tk
import pronouncing

root = tk.Tk()
root.title("Rhymeschemer")

#All widgets of the GUI
frm_main = tk.Frame(master=root)
frm_results = tk.Frame(master=frm_main)
lbl_title = tk.Label(master=frm_main,text="Type text:")
txt_main = tk.Text(master=frm_main,width=50)
btn_submit = tk.Button(master=frm_main,text="Submit",width=50,height=5,command= lambda: generate_results())

frm_main.pack()
lbl_title.pack()
txt_main.pack()
btn_submit.pack()

def generate_results():
    """
    Function bound to btn_submit.
    Collects rhyming words and displays them in widgets.

    
    """

    text = txt_main.get("1.0","end-1c").split() #Get input text and split into list with words every word as element to facilitate iteration.
    rhyme_dict = {} #Keys = words in the text, value = list of rhyming words as retrieved from pronouncing.rhymes()

    for words in text: #Iterates through input text
        
        words = words.lower()
        if words not in rhyme_dict.keys(): #Create new key value pair if word does not exist in dict
            rhyme_dict[words] = []
            
            for possibleRhymes in text: #Nested loop iterates through the rest of the text to find rhyming words
                
                possibleRhymes = possibleRhymes.lower()
                
                if possibleRhymes in pronouncing.rhymes(words) and possibleRhymes not in rhyme_dict[words]: #Adds word to value list if found in pronouncing.rhymes()
                    rhyme_dict[words].append(possibleRhymes)
            
            if len(rhyme_dict[words]) == 0: #If no rhyming words were added to value list, remove key from dict.
                rhyme_dict.pop(words)

    def total_rhymes(dict):
        """
        Function used in lbl_results_1 to display total amount of rhymes in the text.
        Parameters: dict, dictionary with key value pairs of the rhyming words as defined above in function generate_results().
        Returns: total, int value representing total amount of rhyming words in input text.
        
        
        """

        total = 0

        for keys in dict.keys(): #Iterates through dict and adds length of each value list
            total += len(dict[keys]) 

        return total
    
    def rhyme_percentage(text,dict):
        """
        Function used in lbl_results_1 to display percentage of rhyming words in the text.
        Compares amount of rhyming words to total words in the text.
        Parameters: text, str containing input text from user. dict, dictionary with key value pairs of the rhyming words as defined above in function generate_results().
        Returns: rounded float representing percentage of words that rhyme in user input text.
        
        """

        text = list(dict.fromkeys(text))
        return round((len(dict.keys())/len(text))*100)
    
    max_rhyme = max(rhyme_dict.keys(), key=lambda k: len(rhyme_dict[k])) #Finds word with most rhymes in user input text

    #Widgets that are displayed after pressing submit button
    frm_results = tk.Frame(master=root)
    lbl_results_1 = tk.Label(master=frm_results,text= f"The text has a total of {total_rhymes(rhyme_dict)} rhyme combinations, with about {rhyme_percentage(text,rhyme_dict)} percent of words rhyming.")
    lbl_results_2 = tk.Label(master=frm_results,text=f"Most rhymed word was {max_rhyme} with {len(rhyme_dict[max_rhyme])} rhymes")
    lbl_listbox = tk.Label(master=frm_results,text= "All rhymed words (in order of most rhymes):")
    listbox_rhymes = tk.Listbox(master=frm_results)
    listbox_button = tk.Button(master=frm_results,text="Check rhymes",command= lambda: display_rhymes())
    label_rhymes = tk.Label(master=frm_results)

    for words in  sorted(rhyme_dict.keys(), key=lambda k: len(rhyme_dict[k]))[::-1]: #Inserts rhyming words into listbox widget, sorted by highest at the top.
        listbox_rhymes.insert(tk.END,words)

    def display_rhymes():
        """
        Function bound to listbox_button. Displays words rhyming with user highlighted word.
        """
        
        label_rhymes.config(text=f"Rhymes with {str(rhyme_dict[listbox_rhymes.get(tk.ANCHOR)])[1:-1]}")
        
    frm_results.pack(pady=10)
    lbl_results_1.pack()
    lbl_results_2.pack()
    lbl_listbox.pack()
    listbox_rhymes.pack()
    listbox_button.pack()
    label_rhymes.pack()



root.mainloop()
