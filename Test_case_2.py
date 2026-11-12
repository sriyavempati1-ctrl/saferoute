import tkinter as tk
#Group 12 saferoute task tracker
#group members: Susan Syed

#NEW
#A list of valid ids in our "system"
VALID_LOGIN_IDS = [
    "manager01",
    "manager02",
    "firelord123",
    "nanamiforever36",
    "JohnDoe59",
    "puppylover5"
    ]

#NEW
#A dictionary of passwords that match/correlate to the ids above
matching_passwords = {
    "manager01" : "password123",
    "manager02" : "fakepassword",
    "firelord123" : "fakepassword2",
    "nanamiforever36" : "jjkszn2suks",
    "JohnDoe59" : "123password",
    "puppylover5" : "iluvpuppies<3"
    }

available_tasks = []

#check construction login
def login():
    manager_id = id_entry.get().strip()
    password = password_entry.get().strip()
    #check if login information is valid
    if manager_id in VALID_LOGIN_IDS and matching_passwords[manager_id] == password:
        #cases for if task available or not
        login_frame.pack_forget()
        task_frame.pack(pady=20)
        if len(available_tasks)==0:
            task_result_label.config(
                text = "There are no available texts"
            )
        else:
            task_result_label.config(
                text = "Available Tasks:\n" + "\n".join(available_tasks)
            )
    else:
        login_result_label.config(
            text = "Invalid login, try again"
        )
#main saferoute window
root = tk.Tk()
root.title("SafeRoute Task Tracker")
root.geometry("600x350")

#main title top window display
title_label = tk.Label(
    root,
    text = "SafeRoute Task Tracker"
    font = ("Ariel",20,"bold")
)
title_label.pack(pady=20)

#password label and entry box
password_label = tk.Label(
    login_frame,
    text="Enter Password:"
)
password_label.pack()

password_entry = tk.Entry(
    login_frame,
    width = 30,
    show = "*"
)
password_entry.pack(pady=5)

#login button
login_button = tk.Button(
    login_frame,
    text="Login"
    command = login
)
login_button.pack(pady=10)

#Displays login error
login_result_label = tk.Label(
    login_frame,
    text="",
    font=("Arial",11)
)
login_result_label.pack()

#Task section displayed after successful login.
task_frame = tk.Frame(root)
task_label = tk.Label(
    task_frame,
    text="Task List",
    font=("Arial",16,"bold")
)
task_label.pack(pady=10)

#available and no-task message
task_result_label = tk.Label(
    task_frame,
    text = ""
    font=("Arial",12)
)
task_result_label.pack(pady=10)

root.mainloop()

