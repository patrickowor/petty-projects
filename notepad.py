'''
  A minimalist Notepad built with the PySimpleGUI TKinter framework
  Author:     Israel Dryer
  Email:      israel.dryer@gmail.com
  Modified:   2019-10-13
'''
from  os import replace
import tkinter 
import PySimpleGUI as sg 
sg.ChangeLookAndFeel('BrownBlue') # change style

WIN_W: int = 90
WIN_H: int = 25
filename:str = None

# string variables to shorten loop and menu code
file_new: str = 'New............(CTRL+N)'
file_open: str = 'Open..........(CTRL+O)'
file_save: str = 'Save............(CTRL+S)'

menu_layout: list = [['File', [file_new, file_open, file_save, 'Save As', '---', 'Exit']],
                     ['      '],
                     ['Tools', ['Word Count', 'replace']],
                     ['      '],
                     ['Help', ['About']]]

layout: list = [[sg.Menu(menu_layout,font=("Helvetica", 10 ,"bold"))],
                [sg.Text('> New file <', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
                [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]]

window: object = sg.Window('Notepad', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
window.read(timeout=1)
window.maximize()
window['_BODY_'].expand(expand_x=True, expand_y=True)

def new_file() -> str:
    ''' Reset body and info bar, and clear filename variable '''
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> New File <')
    filename = None
    return filename

def open_file() -> str:
    ''' Open file and update the infobar '''
    try:
        filename: str = sg.popup_get_file('Open File', no_window=True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'r') as f:
            window['_BODY_'].update(value=f.read())
        window['_INFO_'].update(value=filename)
    return filename

def save_file(filename: str):
    ''' Save file instantly if already open; otherwise use `save-as` popup '''
    if filename not in (None, ''):
        with open(filename,'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    else:
        save_file_as()

def save_file_as() -> str:
    ''' Save new file or save existing file with another name '''
    try:
        filename: str = sg.popup_get_file('Save File', save_as=True, no_window=True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename,'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    return filename

def word_count():
    ''' Display estimated word count '''
    words: list = [w for w in values['_BODY_'].split(' ') if w!='\n']
    word_count: int = len(words)
    sg.PopupQuick('Word Count: {:,d}'.format(word_count), auto_close=False)

def about_me():
    sg.PopupQuick('"All great things have small beginnings" - Peter Senge', auto_close=False)
    
    

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break
    if event in (file_new, 'n:78'):
        filename = new_file()
    if event in (file_open, 'o:79'):
        filename = open_file()
    if event in (file_save, 's:83'):
        save_file(filename)
    if event in ('Save As',):
        filename = save_file_as()   
    if event in ('Word Count',):
        word_count()
    if event in ('replace',):
         old = sg.popup_get_text('enter value to change')
         new = sg.popup_get_text('enter new value')
         try:
             filereplaced = str(values['_BODY_'])
             filereplace = filereplaced.replace(old, new)
             window['_BODY_'].update(value=str(filereplace))
         except:
             pass       
    
   