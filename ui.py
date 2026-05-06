from tkinter import ttk, StringVar
from auth import UserList
import tkinter as tk

class LoginInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Interface")
        self.master.geometry("300x200")
        self.master.resizable(False, False)
        self.auth = UserList()

#Username variable
        self.text_username = StringVar()
        self.text_username_value = ""
        self.text_password = StringVar()
        self.text_password_value = ""

#Username label and entry
        self.username_label = ttk.Label(self.master, 
                                        text="Enter your Username:"
                                        )
        self.username_label.place(relx=0.5, 
                                  rely=0.1, 
                                  anchor="center"
                                  )        
        self.username_entry = ttk.Entry(self.master, 
                                        textvariable= self.text_username
                                        )
        self.username_entry.place(relx=0.5, 
                                  rely=0.2, 
                                  anchor="center"
                                  )
#Password label and entry
        self.password_label = ttk.Label(self.master, 
                                        text="Enter your Password:"
                                        )
        self.password_label.place(relx=0.5, 
                                  rely=0.3, 
                                  anchor="center"
                                  )        
        self.password_entry = ttk.Entry(self.master, 
                                        show="*",
                                        textvariable=self.text_password
                                        )
        self.password_entry.place(relx=0.5, 
                                  rely=0.4, 
                                  anchor="center"
                                  )

#Login button
        self.login_enter_button = ttk.Button(self.master, 
                                       text="Login", 
                                       command=self.login_button
                                       )
        self.login_enter_button.place(relx=0.5,
                                rely=0.58,
                                anchor="center"
                                )

#Registration label and entry
        self.registration_Label = ttk.Label(self.master,
                                            text="Don't have an account? Register here!"
                                            )
        self.registration_Label.place(relx=0.5,
                                      rely=0.7,
                                      anchor="center"
                                      )

#Registration button
        self.registration_enter_button = ttk.Button(self.master,
                                              text="Register",
                                              command=self.registration_button
                                              )
        self.registration_enter_button.place(relx=0.5,
                                       rely=0.82,
                                       anchor="center"
                                       )

#Login button function 
    def login_button(self):
        self.text_username_value = self.text_username.get()
        self.text_password_value = self.text_password.get()
        self.validate_login()

#Login validation function
    def validate_login(self):
        user_login = self.text_username_value
        password_login = self.text_password_value

        if self.auth.login(user_login, password_login):
            LoginSuccessValidate(self.master).login_success_ok_button.config(command=self.welcome_login)  
        else:
            FailedLoginInterface(self.master)

#Registration button function
    def registration_button(self):
        RegistrationInterface(self.master)

#When the user clicks the OK button on the login success interface, it will close the login interface and open the welcome interface.     
    def welcome_login(self):
        self.master.destroy()
        
        janela_welcome = tk.Tk()
        start_janela = welcome_login_interface(janela_welcome)
        janela_welcome.mainloop()


class RegistrationInterface:
    def __init__(self, master):
        self.master = master
        self.master = tk.Toplevel(self.master)
        self.master.title("Registration")
        self.master.geometry("300x200")
        self.master.resizable(False, False)
        self.auth = UserList()

        self.registration_username = StringVar()
        self.registration_username_value = ""
        self.registration_password = StringVar()
        self.registration_password_value = ""

#Registration username label and entry
        self.registration_username_Label = ttk.Label(self.master,
                                            text="Create your username:"
                                            )
        self.registration_username_Label.place(relx=0.5,
                                      rely=0.1,
                                      anchor="center"
                                      )
        self.registration_username_entry = ttk.Entry(self.master,
                                            textvariable=self.registration_username
                                            )
        self.registration_username_entry.place(relx=0.5,
                                      rely=0.2,
                                      anchor="center"
                                      )

#Registration password label and entry
        self.registration_password_Label = ttk.Label(self.master,
                                                     text="Create your password:"
                                                     )
        self.registration_password_Label.place(relx=0.5,
                                               rely=0.3,
                                               anchor="center"
                                               )
        self.registration_password_entry = ttk.Entry(self.master,
                                                    show="*",
                                                    textvariable=self.registration_password
                                                    )
        self.registration_password_entry.place(relx=0.5,
                                               rely=0.4,
                                               anchor="center"
                                               )

#Registration button
        self.registration_button = ttk.Button(self.master,
                                              text="Register",
                                              command=self.registration_validate_button
                                            )
        self.registration_button.place(relx=0.5,
                                       rely=0.6,
                                       anchor="center"
                                       )
        
    def registration_validate_button(self):
        self.registration_username_value = self.registration_username.get()
        self.registration_password_value = self.registration_password.get()
        
        user_registration = self.registration_username_value
        password_registration = self.registration_password_value

        result = self.auth.registration(user_registration, password_registration)

        if result == "user_exists":
            FailedUsernameRegistration(self.master)
        elif result == "weak_password":
            FailedPasswordRegistration(self.master)
        else:
            self.auth.add_user(self.registration_username_value, self.registration_password_value)

#When the user clicks the OK button on the registration success interface, it will close the registration interface as well.
            RegistrationSuccessValidate(self.master).registration_success_ok_button.config(command=self.master.destroy) 


#Failed login interface -- username or password is incorrect
class FailedLoginInterface:
    def __init__(self, master):
        self.master = master
        self.master = tk.Toplevel(self.master)
        self.master.title("Login Failed")
        self.master.geometry("350x75")
        self.master.resizable(False, False)

        self.failed_login_label = ttk.Label(self.master,
                                            text="Your username or password is incorrect! Please try again."
                                            )
        self.failed_login_label.place(relx=0.5,
                                      rely=0.3,
                                      anchor="center"
                                      )
        self.failed_login_ok_button = ttk.Button(self.master,
                                                    text="OK",
                                                    command=self.master.destroy
                                                    )
        self.failed_login_ok_button.place(relx=0.5,
                                        rely=0.7,
                                        anchor="center"
                                        )
        

#Failed registration interface -- username is already taken
class FailedUsernameRegistration:
    def __init__(self, master):
        self.master = master
        self.master = tk.Toplevel(self.master)
        self.master.title("Registration Failed")
        self.master.geometry("350x75")
        self.master.resizable(False, False)

        self.failed_registration_label = ttk.Label(self.master,
                                            text="This username is already taken! Please try again."
                                            )
        self.failed_registration_label.place(relx=0.5,
                                      rely=0.3,
                                      anchor="center"
                                      )
        self.failed_registration_ok_button = ttk.Button(self.master,
                                                    text="OK",
                                                    command=self.master.destroy
                                                    )
        self.failed_registration_ok_button.place(relx=0.5,
                                        rely=0.7,
                                        anchor="center"
                                        )


#Password validation interface
class FailedPasswordRegistration:
    def __init__(self, master):
        self.master = master
        self.master = tk.Toplevel(self.master)
        self.master.title("Registration Failed")
        self.master.geometry("350x75")
        self.master.resizable(False, False)

        self.failed_registration_label = ttk.Label(self.master,
                                            text="This password is not good! Please try again."
                                            )
        self.failed_registration_label.place(relx=0.5,
                                      rely=0.3,
                                      anchor="center"
                                      )
        self.failed_registration_ok_button = ttk.Button(self.master,
                                                    text="OK",
                                                    command=self.master.destroy
                                                    )
        self.failed_registration_ok_button.place(relx=0.5,
                                        rely=0.7,
                                        anchor="center"
                                        )


#Success registration interface
class RegistrationSuccessValidate:
    def __init__(self, master):
        self.master = master
        self.master = tk.Toplevel(self.master)
        self.master.title("Registration Successful")
        self.master.geometry("350x75")
        self.master.resizable(False, False)

        self.registration_success_label = ttk.Label(self.master,
                                            text="Registration successful! You can now log in."
                                            )
        self.registration_success_label.place(relx=0.5,
                                      rely=0.3,
                                      anchor="center"
                                      )
        self.registration_success_ok_button = ttk.Button(self.master,
                                                    text="OK",
                                                    command=self.master.destroy
                                                    )
        self.registration_success_ok_button.place(relx=0.5,
                                        rely=0.7,
                                        anchor="center"
                                        )


#Success login interface
class LoginSuccessValidate:
    def __init__(self, master):
        self.master = master
        self.master = tk.Toplevel(self.master)
        self.master.title("Login Successful")
        self.master.geometry("350x75")
        self.master.resizable(False, False)

        self.login_success_label = ttk.Label(self.master,
                                            text="Login successful! Welcome back."
                                            )
        self.login_success_label.place(relx=0.5,
                                      rely=0.3,
                                      anchor="center"
                                      )
        self.login_success_ok_button = ttk.Button(self.master,
                                                    text="OK",
                                                    command=self.master.destroy
                                                    )
        self.login_success_ok_button.place(relx=0.5,
                                        rely=0.7,
                                        anchor="center"
                                        )


class welcome_login_interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome")
        self.master.geometry("350x75")
        self.master.resizable(False, False)

        self.welcome_label = ttk.Label(self.master,
                                            text="Welcome to the program! You have successfully logged in."
                                            )
        self.welcome_label.place(relx=0.5,
                                      rely=0.3,
                                      anchor="center"
                                      )
        self.welcome_ok_button = ttk.Button(self.master,
                                                    text="OK",
                                                    command=self.master.destroy
                                                    )
        self.welcome_ok_button.place(relx=0.5,
                                        rely=0.7,
                                        anchor="center"
                                        )
