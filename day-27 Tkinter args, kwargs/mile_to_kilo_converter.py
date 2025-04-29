#import tkinter

#if i want to get rid all of the tkinter.something and just write something 
from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934)
    kilometer_result_label.config(text=f"{km}")



window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300 , height=200)
window.config(padx=20 , pady=20)


#Label
miles_label = Label(text="Miles" , font =("Arial",16,"bold"))
miles_label.grid(column=2 , row=0)
miles_label.config(padx=50 , pady=20)

#Label
kilometer_label = Label(text="Km" , font =("Arial",16,"bold"))
kilometer_label.grid(column=2 , row=1)
kilometer_label.config(padx=50 , pady=20)

#Label
kilometer_result_label = Label(text="0" , font =("Arial",16,"bold"))
kilometer_result_label.grid(column=1 , row=1)
kilometer_result_label.config(padx=50 , pady=20)



#Label
is_equal_label = Label(text="is equal to" , font =("Arial",16,"bold"))
is_equal_label.grid(column=0 , row=1)
is_equal_label.config(padx=50 , pady=20)


#Button
calculate_button = Button(text="Calculate" , command=miles_to_km)
#button.pack()
calculate_button.grid(column=1 , row=2)



#Entry
miles_input = Entry(width=10 )
#print(input.get())
#input.pack()
miles_input.grid(column=1 , row=0)





window.mainloop()
