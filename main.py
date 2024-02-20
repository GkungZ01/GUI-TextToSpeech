from gtts import gTTS
from pygame import mixer
import tkinter as tk
import time, pyperclip
import Components.Thread as thread

mixer.init(44100, -16, 2, 2048)

stopSpeech = False

def text2speech(text:str,filename="temp"):
    audio = gTTS(text=text, lang="en", slow=False)
    audio.save(filename+".mp3")
    
def playSound(filename):
    global stopSpeech, mixer
    mixer.music.load(filename+'.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.5)
    while mixer.music.get_busy():
        if stopSpeech:
            stopSpeech = False
            mixer.music.stop()
            break
        time.sleep(0.1)


filename = "temp"

app = tk.Tk()
window_width = 800
window_height = 600

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

app.geometry(f"{window_width}x{window_height}+{x}+{y}")
app.title("Text to Speech")

text = tk.Text(app)
text.pack(expand=True, fill='both', pady=10, padx=10)

frame = tk.Frame(app,height=20)
frame.pack(fill='x', pady=10, padx=10)

def clearText():
    text.delete('1.0','end')

def pasteText():
    clearText()
    text.insert('end', pyperclip.paste())
    
def soundStop():
    mixer.music.unload()
    
def playText():
    text2speech(text.get('1.0','end'),filename)
    ps = thread.Thread(playSound, [filename])
    ps.Stopped(soundStop)
    ps.Start()
    
def stop_Speech():
    global stopSpeech
    if not mixer.music.get_busy() : return 
    stopSpeech = True

    
submit = tk.Button(frame,width=7, height=1,text="Submit", command=playText)
submit.pack(side='right')
    
clear = tk.Button(frame,width=7, height=1,text="Clear", command=clearText)
clear.pack(side='right')

stopspeech_btn = tk.Button(frame,width=13, height=1,text="Stop Speech", command=stop_Speech)
stopspeech_btn.pack(side='left')

paste = tk.Button(frame,width=7, height=1,text="Paste", command=pasteText)
paste.pack(side='left')

app.mainloop()