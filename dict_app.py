from tkinter import *
import dictionary_client as dc


win = Tk()
win.geometry("750x250")

packingRequestMaiden = True

def exec_search_request(widgets,text):
    response_data = dc.load_data(text)
    # widgets = currentWord , Origin , meaningTitle;
    # if this is the first request, pack the elements after changing the text.  
    if(packingRequestMaiden):
        widgets.currentWord.config(text=response_data.getWord()).pack(pady=10)
        widgets.origin.config(text=response_data.getOrigin()).pack(pady=10)
        widgets.meaningTitle.config(text=response_data.meanings()).pack(pady=10)
    
    # if they are already packed , just change the text and no needing for packing. 
    else:
        widgets.currentWord.config(text=response_data.getWord())
        widgets.origin.config(text=response_data.getOrigin())
        widgets.meaningTitle.config(text=response_data.meanings())

        
    packingRequestSerial = False


    
Label(win, text="Search a word", font=('Helvetica 20 bold')).pack(pady=20)
name_entry = Entry(win, font=('calibre',10,'normal')).pack()


currentWord = Label(win,text="word", font=('Helvetica 10 bold'))
origin = Label(win,text="origin", font=('Helvetica 10 bold'))
meaningTitle = Label(win,text="Meanings : ", font=('Helvetica 10 bold'))

Button(win, text="Search", command=lambda: exec_search_request({
    currentWord:currentWord,
    origin:origin,
    meaningTitle:meaningTitle
},name_entry.get())).pack(pady=10)

win.mainloop()
