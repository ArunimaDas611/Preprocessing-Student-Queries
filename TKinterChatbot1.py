from tkinter import *
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
root = Tk()
root.title("FAQ Chatbot")

def send():
    stop_words = set(stopwords.words('english'))
    punc = string.punctuation

    send = "You - " + e.get()
    txt.insert(END, "\n" + send)
    user = e.get().lower()
    no_punct_user = user.translate(str.maketrans('', '', punc))
    corrected_user = TextBlob(no_punct_user)
    tokenised_user = word_tokenize(corrected_user.correct().string)
    cleaned_user = [word for word in tokenised_user if word not in stop_words]


    if "student" in cleaned_user and "accommodation" in cleaned_user:
        txt.insert(END, "\n" + "Bot - Accommodation for students is available for boys and girls. However, extra charges will be incured.")
    elif "entry" in cleaned_user and "requirements" in cleaned_user:
        txt.insert(END, "\n" + "Bot - You need atleast 65% percentile in any engineering entrance exam (JEE/State Exam).")
    elif "documents" in cleaned_user and "application" in cleaned_user:
        txt.insert(END, "\n" + "Bot - Any government-approved identification, 10th and 12th certificates, entrance exam admit cards.")
    elif "long" in cleaned_user and "approval" in cleaned_user and "list" in cleaned_user:
        txt.insert(END, "\n" + "Bot - Around 15-20 days.")
    elif "campus" in cleaned_user:
        txt.insert(END, "\n" + "Bot - The campus is lively indeed! Our campus is the second largest in SIU, with architecture inspired from the Vatican City.")
    elif "fees" in cleaned_user:
        txt.insert(END, "\n" + "Bot - The fees are normally around 12 lakh for the entire course, but if you have a domicile in Nagpur, the fees can be reduced by Rs. 40,000.")
    elif "facilities" in cleaned_user and "available" in cleaned_user:
        txt.insert(END, "\n" + "Bot - We have a large library, a sports complex, a gym, a mess for the hostellers and a cafeteria. There is also a stationery shop near the mess.")
    elif (("internship" in cleaned_user or "internships" in cleaned_user) and ("placement" in cleaned_user or "placements" in cleaned_user)):
        txt.insert(END, "\n" + "Bot - For placements, we make a lot of effort in ensuring that our students get placed at great companies. This ranges from training the students in soft skills & interviews to assigning industry-relevant projects.\n\nFor the internship, it is mandatory for students to get a summer internship after completing their second year.")
    elif "internship" in cleaned_user or "internships" in cleaned_user:
        txt.insert(END, "\n" + "Bot - For the internship, it is mandatory for students to get a summer internship after completing their second year.")
    elif "placement" in cleaned_user or "placements" in cleaned_user:
        txt.insert(END, "\n" + "Bot - For placements, we make a lot of effort in ensuring that our students get placed at great companies. This ranges from training the students in soft skills & interviews to assigning industry-relevant projects.")
    elif "companies" in cleaned_user or "company" in cleaned_user:
        txt.insert(END, "\n" + "Bot - From the giants of Accenture and Acquia to growing companies like Cognizant and GlobalLogic, a lot of reputed companies hire our prestigious students.\n\nFor more information, check out our website.")
    elif "medical" in cleaned_user and "leave" in cleaned_user:
        txt.insert(END, "\n" + "Bot - To apply for a medical leave, you have to inform the HOD, Academic Incharge and Class Incharge by email atleast a day before. Then, after receiving receiving the medical certificate, submit an application with the certificate attached to the HOD.")
    elif "research" in cleaned_user:
        txt.insert(END, "\n" + "Bot - We do indeed cultivate research culture into students. Most of our faculty are doctorates after all. By assigning semester projects, we give students the opportunity to tackle real-life problems and engage in continuous learning. Students can use these projects to move further in the field of scientific research.")
    else:
        txt.insert(END, "\n" + "Bot - Sorry! I didn't got you.")
    e.delete(0, END)    


txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()