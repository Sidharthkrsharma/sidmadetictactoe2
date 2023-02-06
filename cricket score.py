from tkinter import *
import time
import json

root=Tk()
rooot.geometry("500x250")

match_data=requests.get('http://cricapi.com/api/cricketScore?/unique_id=1166965&apikey=WmAyNvw3DDaEUQZalouX1Eh27II3')
json_data=match_data.json()


def times():
    current_score=json_data['stat']
    score.configure(text="current score : "+current_score)
    score.after(200,times)
    

score=Label(root,font=("time",15,"bold"),bg="white")
score.grid(row=2,column=2,pady=25,padx=100)
times()

root.mainloop()
