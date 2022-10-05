import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from turtle import home
import customtkinter
from bart_summarizer import generate_bart
from sumy_summarizer import generate_sumy
from nltk_summarizer import generate_nltk
import time
import docx

import random

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

random_digits_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
timestamp = time.strftime("%d%m%Y-%H%M")
texttimestamp = time.strftime("%d/%m/%Y %H.%M")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):

    WIDTH = 800
    HEIGHT = 640

    def __init__(self):
        super().__init__()

        self.title("Automatic Text Summarizer")
        self.iconbitmap("logo.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_left.grid_rowconfigure(0, minsize=10) 
        self.frame_left.grid_rowconfigure(6, weight=1) 
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Automatic Text\n Summarizer",
                                              text_font=("Century Gothic Bold", -16))
        self.label_1.grid(row=1, column=0, pady=30, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Home",
                                                fg_color=("gray75", "gray30"),
                                                command=self.home_button)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="File",
                                                fg_color=("gray75", "gray30"), 
                                                command=self.file_button)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Comparison",
                                                fg_color=("gray75", "gray30"),
                                                command=self.comparison_button)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)


        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)
        self.home_button()


    def home_button(self):
       def summarizebtn_function():
        self.summary_result.configure(state="normal")
        input = self.entry.get("1.0",END)
        self.summary_result.delete("1.0", tkinter.END)
        self.summary_result.insert(INSERT,generate_nltk(input))
        self.summary_result.configure(state="disabled")
       
       def clearbtn_function():
        self.summary_result.configure(state="normal")
        self.entry.delete("1.0",tkinter.END)
        self.summary_result.delete("1.0", tkinter.END)
        self.summary_result.configure(state="disabled")
       
       def savesummarybtn_function():
           self.summary_result.configure(state="normal")
           input = self.entry.get("1.0",END)
           summary = generate_nltk(input)
           if(summary.endswith('.')==False):
            summary.join(".")
           file_name = "ATS"+random.choice(random_digits_list)+random.choice(random_digits_list)+random.choice(random_digits_list)+"_Summary_"+timestamp+'.txt'
           with open(file_name,'w', encoding="utf-8") as f:
               f.write(summary)
           result = texttimestamp + " - Your Summary Has Been Saved\nFile Name: " + file_name + "\nSummary:\n" + summary
           self.summary_result.delete("1.0", tkinter.END)
           self.summary_result.insert(INSERT,result)
           self.summary_result.configure(state="disabled")

       self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
       self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=8, pady=20, padx=20, sticky="nsew")
       self.frame_info.rowconfigure(0, weight=2)
       self.frame_info.rowconfigure(1, weight=3)
       self.frame_info.rowconfigure(2, weight=3)
       self.frame_info.rowconfigure(4, weight=5)
       self.frame_info.rowconfigure(6, weight=5)
       self.frame_info.rowconfigure(7, weight=3)
       self.frame_info.columnconfigure(0, weight=1)
       self.frame_info.columnconfigure((1,2), weight=1)
       self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Text Summarizer",
                                                   text_font=("Century Gothic Bold", -13),
                                                   fg_color=("white", "gray38"),
                                                   justify=tkinter.LEFT)
       self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=10,columnspan=3)
       self.entry = scrolledtext.ScrolledText(master=self.frame_info,
                                            width=10,
                                            height=10, font = ("Century Gothic",10),
                                            bd=3,wrap="word")
       self.entry.grid(row=1, column=0, sticky="we", padx=20, columnspan=3)
       self.summarizebtn = customtkinter.CTkButton(master=self.frame_info,
                                                text="Summarize",
                                                fg_color=("#5ACDA4"),
                                                command=summarizebtn_function)
       self.summarizebtn.grid(column=0, row=2, sticky = "nwe", padx=20,pady=10, columnspan=2)
       self.clearbtn = customtkinter.CTkButton(master=self.frame_info,
                                                text="Clear",
                                                fg_color=("#DEB887"),
                                                hover_color="#C77C78",
                                                command=clearbtn_function)
       self.clearbtn.grid(column=2, row=2, sticky="nwe", padx=20, pady=10)
       self.savesummarybtn = customtkinter.CTkButton(master=self.frame_info,
                                                text="Save Summary",
                                                fg_color=("#22AEFF"),
                                                hover_color="#6597EA",
                                                command=savesummarybtn_function)
       self.savesummarybtn.grid(row=3, column=0, columnspan=2, sticky="we", padx =20)
       self.summary = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Summary",
                                                   text_font=("Century Gothic Bold", -13),
                                                   justify=tkinter.LEFT)
       self.summary.grid(column=0, row=5, sticky="nwe", padx=15, columnspan=3)
       self.summary_result = scrolledtext.ScrolledText(master=self.frame_info,
                                            width=10,
                                            height=8, font = ("Century Gothic",10),
                                            bd=3,wrap="word")
       self.summary_result.grid(row=6, column=0, sticky="we", padx=20, columnspan=3)
       self.summary_result.configure(state="disabled")



    def file_button(self):
        def openfile():
            
            fileopened = tkinter.filedialog.askopenfilename(filetype=(('Text Files',".txt"),("Word Document",".docx"),("All Files","*")))
            if(fileopened.endswith(".docx")):
                doc = docx.Document(fileopened)
                read_para =[]
                for para in doc.paragraphs:
                    read_para.append(para.text)
                paragraphs = (''.join(read_para))
                self.filetext.configure(state="normal")
                self.filetext.delete("1.0",tkinter.END)
                self.filetext.insert(INSERT,paragraphs)        
                self.filetext.configure(state="disabled")
            elif(fileopened.endswith(".txt")):
                read_text = open(fileopened, encoding="utf-8").read()
                self.filetext.configure(state="normal")
                self.filetext.delete("1.0",tkinter.END)
                self.filetext.insert(END,read_text)        
                self.filetext.configure(state="disabled")
            
            
        def summarizebtn_function():
            self.filesummary.configure(state="normal")
            input = self.filetext.get("1.0",END)
            self.filesummary.delete("1.0", tkinter.END)
            self.filesummary.insert(INSERT,generate_nltk(input))
            self.filesummary.configure(state="disabled")
       
        def clearbtn_function():
            self.filetext.configure(state="normal")
            self.filesummary.configure(state="normal")
            self.filetext.delete("1.0",tkinter.END)
            self.filetext.configure(state="disabled")
            self.filesummary.delete("1.0", tkinter.END)
            self.filesummary.configure(state="disabled")
       
        def savesummarybtn_function():
           self.filesummary.configure(state="normal")
           input = self.filetext.get("1.0",END)
           summary = generate_nltk(input)
           if(summary.endswith('.')==False):
            summary.join(".")
           file_name = "ATS"+random.choice(random_digits_list)+random.choice(random_digits_list)+random.choice(random_digits_list)+"_Summary_"+timestamp+'.txt'
           with open(file_name,'w', encoding="utf-8") as f:
               f.write(summary)
           result = texttimestamp + " - Your Summary Has Been Saved\nFile Name: " + file_name + "\nSummary:\n" + summary
           self.filesummary.delete("1.0", tkinter.END)
           self.filesummary.insert(INSERT,result)
           self.filesummary.configure(state="disabled")
        
        self.frame_file= customtkinter.CTkFrame(master=self.frame_right)
        self.frame_file.grid(row=0, column=0, columnspan=2, rowspan=9, pady=20, padx=20, sticky="nsew")
        
        self.frame_file.rowconfigure(8, weight=2)

        self.frame_file.columnconfigure(0, weight=1)
        self.frame_file.columnconfigure((1,2), weight=1)
        self.label_file_1 = customtkinter.CTkLabel(master=self.frame_file,
                                                   text="Text Summarizer from File",
                                                   fg_color=("white", "gray38"),
                                                   text_font=("Century Gothic Bold", -13),
                                                   justify=tkinter.LEFT)
        self.label_file_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15,columnspan=3)
        self.openfilebtn = customtkinter.CTkButton(master=self.frame_file,
                                                text="Open File",
                                                fg_color=("#5ACDA4"),
                                                command=openfile)
        self.openfilebtn.grid(column=0, row=1, sticky = "nwe", padx=20,columnspan=2)
        self.textlabel = customtkinter.CTkLabel(master=self.frame_file,
                                                   text="Text from File",
                                                   text_font=("Century Gothic Bold", -13),
                                                   justify=tkinter.LEFT)
        self.textlabel.grid(column=0, row=2, sticky="nwe", padx=15, pady=(20,0),columnspan=3)
        self.filetext = scrolledtext.ScrolledText(master=self.frame_file,
                                            width=10,
                                            height=8, font = ("Century Gothic",10),
                                            bd=3,wrap="word")
        self.filetext.grid(row=3, column=0, sticky="nwe", padx=20,pady=(0,20), columnspan=3)
        self.filetext.configure(state="disabled")

        self.summarizebtn = customtkinter.CTkButton(master=self.frame_file,
                                                text="Summarize",
                                                fg_color=("#5ACDA4"),
                                                command=summarizebtn_function)
        self.summarizebtn.grid(column=0, row=4, sticky = "nwe", padx=20,pady=10, columnspan=2)
        self.clearbtn = customtkinter.CTkButton(master=self.frame_file,
                                                text="Clear",
                                                fg_color=("#DEB887"),
                                                hover_color="#C77C78",
                                                command=clearbtn_function)
        self.clearbtn.grid(column=2, row=4, sticky="nwe", padx=20, pady=10)
        self.savesummarybtn = customtkinter.CTkButton(master=self.frame_file,
                                                text="Save Summary",
                                                fg_color=("#22AEFF"),
                                                hover_color="#6597EA",
                                                command=savesummarybtn_function)
        self.savesummarybtn.grid(row=5, column=0, columnspan=2, sticky="we", padx =20,pady=(0,20))
        self.summarylabel = customtkinter.CTkLabel(master=self.frame_file,
                                                   text="Summary",
                                                   text_font=("Century Gothic Bold", -13),
                                                   justify=tkinter.LEFT)
        self.summarylabel.grid(column=0, row=6, sticky="nwe", padx=15,columnspan=3)
        self.filesummary = scrolledtext.ScrolledText(master=self.frame_file,
                                            width=10,
                                            height=6, font = ("Century Gothic",10),
                                            bd=3,wrap="word")
        self.filesummary.grid(row=7, column=0, sticky="nwe", padx=20,pady=(0,20), columnspan=3)
        self.filesummary.configure(state="disabled")

    def comparison_button(self):
        def clearbtn_function():
            self.compare_entry.delete("1.0", tkinter.END)
            self.summary_result_nltk.configure(state="normal")
            self.summary_result_sumy.configure(state="normal")
            self.summary_result_bart.configure(state="normal")
            self.summary_result_nltk.delete("1.0",tkinter.END)
            self.summary_result_sumy.delete("1.0",tkinter.END)
            self.summary_result_bart.delete("1.0",tkinter.END)
            self.summary_result_nltk.configure(state="disabled")
            self.summary_result_sumy.configure(state="disabled")
            self.summary_result_bart.configure(state="disabled")

        def compare_summary_function():
            self.summary_result_nltk.configure(state="normal")
            self.summary_result_sumy.configure(state="normal")
            self.summary_result_bart.configure(state="normal")
            
            input = self.compare_entry.get("1.0",END)
            self.summary_result_nltk.delete("1.0", tkinter.END)
            self.summary_result_nltk.insert(INSERT,generate_nltk(input))
            self.summary_result_sumy.delete("1.0", tkinter.END)
            self.summary_result_sumy.insert(INSERT,generate_sumy(input))
            self.summary_result_bart.delete("1.0", tkinter.END)
            self.summary_result_bart.insert(INSERT,generate_bart(input))

            self.summary_result_nltk.configure(state="disabled")
            self.summary_result_sumy.configure(state="disabled")
            self.summary_result_bart.configure(state="disabled")
        
        self.frame_comparison= customtkinter.CTkFrame(master=self.frame_right)
        self.frame_comparison.grid(row=0, column=0, columnspan=2, rowspan=12, pady=20, padx=20, sticky="nsew")
        
        self.frame_comparison.rowconfigure(11, weight=2)
        self.frame_comparison.columnconfigure(0, weight=1)
        self.frame_comparison.columnconfigure((1,2), weight=1)
        self.label_comparison_1 = customtkinter.CTkLabel(master=self.frame_comparison,
                                                   text="Summary Comparison with Different Library",
                                                   fg_color=("white", "gray38"),
                                                   text_font=("Century Gothic Bold", -13),
                                                   justify=tkinter.LEFT)
        self.label_comparison_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15,columnspan=3)

        self.compare_entry = scrolledtext.ScrolledText(master=self.frame_comparison,
                                                    width=10,
                                                    height=5, font = ("Century Gothic",10),
                                                    bd=3,wrap="word")                          
        self.compare_entry.grid(row=1, column=0, sticky="we", padx=20, columnspan=3)
        self.summarizebtn = customtkinter.CTkButton(master=self.frame_comparison,
                                                text="Summarize",
                                                fg_color=("#5ACDA4"),command=compare_summary_function)
        self.summarizebtn.grid(column=0, row=2, sticky = "nwe", padx=20,pady=10, columnspan=2)
        self.clearbtn = customtkinter.CTkButton(master=self.frame_comparison,
                                                text="Clear",
                                                fg_color=("#DEB887"),
                                                hover_color="#C77C78",command=clearbtn_function)
        self.clearbtn.grid(column=2, row=2, sticky="nwe", padx=20, pady=10)
        self.summary_nltk = customtkinter.CTkLabel(master=self.frame_comparison,
                                            text="NLTK Summary",
                                            text_font=("Century Gothic Bold", -13),
                                            justify=tkinter.LEFT)
        self.summary_nltk.grid(column=0, row=3, sticky="nwe", padx=15, columnspan=3)
        self.summary_result_nltk = scrolledtext.ScrolledText(master=self.frame_comparison,
                                            width=10,
                                            height=4, font = ("Century Gothic",10),
                                            bd=3,wrap="word")
        self.summary_result_nltk.grid(row=4, column=0, sticky="we", padx=20, columnspan=3)

        self.summary_sumy = customtkinter.CTkLabel(master=self.frame_comparison,
                                            text="Sumy Summary",
                                            text_font=("Century Gothic Bold", -13),
                                            justify=tkinter.LEFT)
        self.summary_sumy.grid(column=0, row=5, sticky="nwe", padx=15, columnspan=3,pady=(10,0))
        self.summary_result_sumy = scrolledtext.ScrolledText(master=self.frame_comparison,
                                            width=10,
                                            height=4, font = ("Century Gothic",10),
                                            bd=3,wrap="word")
        self.summary_result_sumy.grid(row=6, column=0, sticky="we", padx=20, columnspan=3)
        self.summary_bart = customtkinter.CTkLabel(master=self.frame_comparison,
                                            text="BART Summary",
                                            text_font=("Century Gothic Bold", -13),
                                            justify=tkinter.LEFT)
        self.summary_bart.grid(column=0, row=7, sticky="nwe", padx=15, columnspan=3,pady=(10,0))
        self.summary_result_bart = scrolledtext.ScrolledText(master=self.frame_comparison,
                                            width=10,
                                            height=4, font = ("Century Gothic",10),
                                            bd=3,wrap="word")
        self.summary_result_bart.grid(row=8, column=0, sticky="we", padx=20, columnspan=3)
        self.summary_result_nltk.configure(state="disabled")
        self.summary_result_sumy.configure(state="disabled")
        self.summary_result_bart.configure(state="disabled")
    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()