# Name : Peter Geevarghese Alex
# Final_Project
# Course number : ITMD 513-01

import time
print("ITMD 513-01")
print("Final_Project")
print("Programmer: Peter Geevarghese Alex")

x = 12
print("-" * 25)
## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))


#military time
print ("Current time:",time.strftime("%X"))


#Importing Libraries,the most important!!

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from data import df

# In order to maintain Security, A Function created for    login purpose. 
def Check_login():
    your_username = userEntry.get()
    your_password = passEntry.get()

    # My Credentials  
    valid_username = "crime"
    valid_password = "crimein"

    if your_username == valid_username and your_password == valid_password:
        myloginWindow.destroy()  
        openMain()
    else:
        messagebox.showerror("Thats an Error", "Invalid username / password")



# First Function for the graphs.
# Funtion for plotting the Top 5 Crimes by Count

def top5crimes_graph():
    
    s = df[['primary_type']]  
    crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
    data = crime_count.iloc[-10:-5] 

    print(data[::-1])

    data.plot(kind='barh')
    plt.title('Figure 1 Top 5 Crimes by Count')
    plt.xlabel('Crime Count')
    plt.ylabel('Crime Type')
    plt.subplots_adjust(left=0.33, right=0.89)
    plt.show()
    
# Second Function for the graphs.
# Funtion for plotting the arrest and non_arrest by pie chart

def arrest_and_non_arrest_chart():

    
    arrestedCount = 100
    notarrestedCount = 150
    labels = ["Arrested", "Not Arrested"]
    sizes = [arrestedCount, notarrestedCount]
    colors = ['#0000FF', '#FFA500']  

    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.title("Figure 2 Arrest vs Non-Arrest Ratio")

    # Add a legend inside the pie chart
    plt.legend(title="Legend", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), labels=labels, prop={'size': 12})

    plt.show()

# Thrid Function for the graphs.
# Funtion for plotting the specific_crime over time 


def specific_to_crime_chart(crime_type):
    
    crimeDatas = df[df['primary_type'] == crime_type].copy()  
    crimeDatas['date'] = pd.to_datetime(crimeDatas['date'])
    crimeDatas.sort_values(by='date', inplace=True)
    incidentCount = crimeDatas['date'].value_counts().sort_index()
    

    plt.figure(figsize=(10, 6))
    plt.plot(incidentCount.index, incidentCount.values, marker='o')
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator(interval=1))
    plt.xlabel('Date')
    plt.ylabel('Number of Incidents')
    plt.title(f'Figure 3 {crime_type} Incidents Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



## login window
myloginWindow = tk.Tk()
myloginWindow.title("Login")
myloginWindow.geometry("300x150")

userLabel = tk.Label(myloginWindow, text="Your_Username:")
userLabel.pack()
userEntry = tk.Entry(myloginWindow)
userEntry.pack()

password_label = tk.Label(myloginWindow, text="Your_Password:")
password_label.pack()
passEntry = tk.Entry(myloginWindow, show="*")
passEntry.pack()

logButton = tk.Button(myloginWindow, text="Login", command=Check_login)
logButton.pack()

# Opening the main window
def openMain():
    global mywindowTitle, graph_dropdown,crime_type_var

    mywindowTitle = tk.Tk()
    mywindowTitle.title("Crime Data")
    mywindowTitle.geometry("800x600")

  

  # Drop-down list - graph selection
    graph_options = ["Select a Chart", "Bar chart", "Pie chart", "Line chart"]
    graph_dropdown = ttk.Combobox(mywindowTitle, values=graph_options)
    graph_dropdown.set("Select a Graph")  
    graph_dropdown.pack()
    # Option button creation for crime type and arrests filtering.
    crime_types = ["Select Crime"] + df['primary_type'].unique().tolist()
    crime_type_var = tk.StringVar(mywindowTitle)
    crime_type_var.set("Select Crime")
    crime_type_label = tk.Label(mywindowTitle, text="Select Crime Type:")
    crime_type_label.pack()
    crime_type_option = ttk.OptionMenu(mywindowTitle, crime_type_var, *crime_types)
    crime_type_option.pack()

   

    # Button for updating the graph and hence display based on the user's selection
    updatesButton = tk.Button(mywindowTitle, text="Update Graph", command=update_graph_display)
    updatesButton.pack()

    mywindowTitle.mainloop()
# This function will update the graph display based on the user's selection
def update_graph_display():
    selectedGraph = graph_dropdown.get()

    if selectedGraph == "Bar chart":
        top5crimes_graph()
    elif selectedGraph == "Pie chart":
        arrest_and_non_arrest_chart()
    elif selectedGraph == "Line chart":
        selected_crime_type = crime_type_var.get()
        specific_to_crime_chart(selected_crime_type)

myloginWindow.mainloop()
