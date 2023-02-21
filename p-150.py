# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:37:20 2023

@author: Ankan Datta
"""

from tkinter import * 
import random

root = Tk()
root.title("State and Country")
root.geometry("600x600")
root.configure(background='cyan')

enter_country = Entry(root)
enter_city = Entry(root)
enter_country.place(relx=0.5, rely=0.2, anchor=CENTER)
enter_city.place(relx=0.5, rely=0.3, anchor=CENTER)

country_list = Label(root)
city_list = Label(root)

random_number_country = Label(root)
random_number_city = Label(root)

random_country = Label(root)
random_city = Label(root)

list_country = []
list_city = []

def add_city_country(): 
    country_name = enter_country.get()
    city_name = enter_city.get()
    list_country.append(country_name)
    list_city.append(city_name)
    country_list["text"] = "Country List - " + str(list_country)
    city_list["text"] = "City List - " + str(list_city)
    
def random_number():
    length = len(list_country) 
    
    length2 = len(list_city)
    
    random_no = random.randint(0, length-1)
    
    
    
    random_no2 = random.randint(0, length2-1)
    
    
    
    random_number_country["text"] = "Random Country - " + str(random_no)
    
    random_number_city["text"] = "Random City - " + str(random_no2)
    
    generated_random_number = list_country[random_no]
    
    generated_random_number2 = list_city[random_no2]
    
    random_country["text"] = "Random Country - " + str(generated_random_number)
    random_city["text"] = "Random city - " + str(generated_random_number2)
    
    
    
btn = Button(root, text="Display Country And City name", command=add_city_country)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

country_list.place(relx=0.5, rely=0.5, anchor=CENTER)
city_list.place(relx=0.5, rely=0.6, anchor=CENTER)

btn = Button(root, text = "Display Country And City Name Randomly", command=random_number)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)

random_number_country.place(relx=0.5, rely=0.8, anchor=CENTER)
random_number_city.place(relx=0.5, rely=0.9, anchor=CENTER)


root.mainloop()