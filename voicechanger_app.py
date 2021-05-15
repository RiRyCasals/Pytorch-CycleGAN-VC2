import os
import os.path
import pyaudio
import tkinter as tk
from tkinter import ttk,messagebox
from test import CycleGANTest


option_list =['model1','model2','model3']
model_checkpoint = ['./model/model_checkpoint/_CycleGAN_CheckPoint.pth','aaa','bbb']

logf0s_normalization = './model/logf0s_normalization.npz'
mcep_normalization = './model/mcep_normalization.npz'
#model_checkpoint = './model/model_checkpoint/_CycleGAN_CheckPoint.pth'
validation_A_dir = './soundsorce'
output_A_dir = './output'

def button1_click():
    messagebox.showinfo("実行中")
    v = str(combo.get())
    #model_chackpoint = model_checkpoint[option_list.index(v)]
    #stream = Pyaudio.open(format=pyaudio.paInt16, channels=1, rate=44100, frames_per_buffer=8820, input=True, output=False)
    cycleGAN = CycleGANTest(logf0s_normalization=logf0s_normalization,mcep_normalization=mcep_normalization,model_checkpoint=model_checkpoint[option_list.index(v)],validation_A_dir=validation_A_dir,output_A_dir=output_A_dir)
    cycleGAN.validation_for_A_dir()
    messagebox.showinfo("終了")
def button2_click():
    '''
    pyaudio stream実験用
    if stream:
        stream.stop_stream()
        stream.close()
    if Pyaudio:#最初に中止ボタンが押されたときのため
        pyaudio.terminate()
        Pyaudio = stream = None
    '''
    pass
        
def select(value):
    pass
   


#Pyaudio = pyaudio.PyAudio()

if not(os.path.exists(output_A_dir)):
    os.mkdir(output_A_dir)

main_win = tk.Tk()
main_win.title("VoiceChanger")
main_win.geometry("300x120")

main_frame = ttk.Frame(main_win)
main_frame.grid(column = 0,row = 0,padx = 5,pady = 10)

model_label = ttk.Label(main_frame, text = '音声モデル選択')
model_label.grid(column = 0,row = 0)
'''
variable = tk.StringVar(main_win)
variable.set(option_list[0])
option = tk.OptionMenu(main_win,variable,*option_list,command = select)
option.grid(column = 0,row = 1)
'''
frame = ttk.Frame(main_win,padding=10)
frame.grid()
var = tk.StringVar()
combo = ttk.Combobox(frame,textvariable = var,value = option_list,width=10)
combo.set(option_list[0])
combo.bind("<<ComboboxSelected>>",select)
combo.grid(column=0,row=1)


button1 = tk.Button(main_win,text = '実行',command = button1_click)
button1.grid(column = 1,row = 1)

button2 = tk.Button(main_win,text = '中止',command = button2_click)
button2.grid(column = 2,row = 1)

main_win.mainloop()

