import customtkinter as ct

myEmailList={"email1":{"sender": "mom@gmail.com", "subject": "This is Mom", "summary": "This is a summary of the email from Mom."},
             "email2":{"sender": "dad@gmail.com", "subject": "This is Dad", "summary": "This is a summary of the email from Dad."},
             "email3":{"sender": "brother@gmail.com", "subject": "This is Brother", "summary": "This is a summary of the email from Brother."},
             "email4":{"sender": "sister@gmail.com", "subject": "This is Sister", "summary": "This is a summary of the email from Sister."}, 
             "email5":{"sender": "myself@gmail.com", "subject": "This is Myself", "summary": "This is a summary of the email from Myself."}, 
            } 

class EmailStackApp:

    def __init__(self, emailList):
        self.root= ct.CTk()
        self.root.title("Gmail Summarizer")
        self.root.geometry("700x700")
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")

        self.headerFrame=ct.CTkFrame(master=self.root, width=70, height=70, fg_color="transparent")
        self.headerFrame.pack(side="top", anchor="n")
        
        self.applicationLabel_G = ct.CTkLabel(master=self.headerFrame, text="  G", font=("Georgia", 50), text_color="#009DFF")
        self.applicationLabel_G.pack(side="left", padx=1)
        self.applicationLabel_M = ct.CTkLabel(master=self.headerFrame, text="M", font=("Georgia", 50), text_color="#E20000")
        self.applicationLabel_M.pack(side="left", padx=1)
        self.applicationLabel_a = ct.CTkLabel(master=self.headerFrame, text="a", font=("Georgia", 50), text_color="#FFEA00")
        self.applicationLabel_a.pack(side="left",padx=1)
        self.applicationLabel_i = ct.CTkLabel(master=self.headerFrame, text="i", font=("Georgia", 50), text_color="#00BBFF")
        self.applicationLabel_i.pack(side="left", padx=1)
        self.applicationLabel_l = ct.CTkLabel(master=self.headerFrame, text="l", font=("Georgia", 50), text_color="#00BD16")
        self.applicationLabel_l.pack(side="left", padx=1)
        self.applicationLabel_Summarizer = ct.CTkLabel(master=self.headerFrame, text=" Summarizer", font=("Georgia", 50), text_color="#D6D6D6")
        self.applicationLabel_Summarizer.pack(side="left", padx=23)

        self.emails=emailList

        self.welcomeScreen=welcomeScreen(self)
        self.summaryScreen=summaryScreen(self)
        self.homeScreen=homeScreen(self)

        self.currentScreenFrame = None

        self.showWelcomeScreen()
        self.root.mainloop()

    def showWelcomeScreen(self):
        self.welcomeScreen.frame.pack(pady=120, padx=30, fill="both", expand=True)
        self.currentScreenFrame = self.welcomeScreen.frame
    
    def showSummaryScreen(self):
        self.welcomeScreen.frame.pack_forget()
        self.summaryScreen.frame.pack(fill="both", expand=True)
        self.currentScreenFrame = self.summaryScreen.frame

    def showHomeScreen(self):
        self.summaryScreen.frame.pack_forget()
        self.homeScreen.frame.pack()
        self.currentScreenFrame = self.homeScreen.frame
    
    
    def getEmail(self):
        myEmails=""

        for email in myEmailList:
            emailData = myEmailList[email]
            myEmails+=f"Sender: {emailData['sender']} \n Subject: {emailData['subject']} \n ========================\n"
        
        return myEmails

        

class welcomeScreen:
    def __init__(self,controller):
        self.frame=ct.CTkFrame(master=controller.root)

        self.backgroundEnvelopeFrame = ct.CTkFrame(master=self.frame, width=500, height=350, corner_radius=15, fg_color="#ffc800")
        self.backgroundEnvelopeFrame.pack(pady=20)

        self.backgroundEnvelopeFrame.pack_propagate(False)
        self.envelopeEmojiButton=ct.CTkButton(master=self.backgroundEnvelopeFrame, text="\U00002709", text_color= "#0091FF", font=("Georgia",300), fg_color="transparent", command=(lambda:controller.showSummaryScreen()))
        self.envelopeEmojiButton.place(relx=0.5, rely=0.3, anchor="center")

        self.numberEmailsLabel=ct.CTkLabel(master=self.backgroundEnvelopeFrame, text=f"You have {len(controller.emails)} \n new messages!", font=("Times New Roman", 50), text_color="#77003c")
        self.numberEmailsLabel.place(relx=0.5, rely=0.75, anchor="center")

        self.numberCircle=ct.CTkLabel(master=self.backgroundEnvelopeFrame, text=f"{len(controller.emails)}", font=("Times New Roman", 50), width=45, height=45, text_color="#FFFFFF", fg_color="#cc2e2e", corner_radius=30)
        self.numberCircle.place(relx=0.7, rely=0.15, anchor="center")
        
        
class summaryScreen:
    def __init__(self, controller):
        self.frame=ct.CTkFrame(master=controller.root, width=610, height=610, fg_color="transparent")

        self.summaryBoxFrame = ct.CTkFrame(master=self.frame, width=500, height=580, fg_color="#b1b1b1", corner_radius=15)
        self.summaryBoxFrame.pack(pady=30,padx=10)

        self.summaryText = ct.CTkLabel(master=self.summaryBoxFrame, text="Summary", font=("Georgia", 50), text_color="#020086", fg_color="transparent")
        self.summaryText.place(relx=0.5, rely=0, anchor="n")

        self.homeButton= ct.CTkButton(master=self.summaryBoxFrame, text="Home", font=("Comic Sans MS", 16), text_color="#BFBFBF", fg_color="#020086", command=lambda: controller.showHomeScreen())
        self.homeButton.place(x=185, y=550)


class homeScreen:
    def __init__(self, controller):
        self.frame=ct.CTkFrame(master=controller.root, width=600, height=600)
        self.frame.pack_propagate(False)

        self.summaryBoxScrollableFrame = ct.CTkScrollableFrame(master=self.frame, width=270, height=500, fg_color="#b1b1b1", corner_radius=15)
        self.summaryBoxScrollableFrame.pack(side="left",pady=50,padx=10)

        self.summaryText = ct.CTkLabel(master=self.summaryBoxScrollableFrame, text="Summary", font=("Georgia", 50), text_color="#020086", fg_color="#b1b1b1")
        self.summaryText.pack(pady=10)

        self.emailListFrame = ct.CTkScrollableFrame(master=self.frame, width=270, height=500, fg_color="#b1b1b1", corner_radius=15)
        self.emailListFrame.pack(side="left",pady=50,padx=10)

        self.emailList = ct.CTkLabel(master=self.emailListFrame, text=controller.getEmail(), font=("Georgia", 15), text_color="#020086", fg_color="#b1b1b1")
        self.emailList.pack(pady=10)



if __name__ == "__main__":
    app = EmailStackApp(myEmailList)
    
