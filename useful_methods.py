import win32com.client
import threading
import customtkinter as ctk
import tkinter as tk
from datetime import datetime

class SpeechThread(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.text = text

    def run(self):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(self.text)


def speak_text(text):
    speech_thread = SpeechThread(text)
    speech_thread.start()


# At the top of your file, make sure you have these imports
import customtkinter as ctk
from PIL import Image


import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from datetime import datetime

