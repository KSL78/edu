from tkinter import *
###팅커의 모든 모듈 연결###
win = Tk()
win.title("GUItest")
Label(win,text = 'guitest').grid(column=0,row=0)#레이아웃 매니저grid
win.resizable('false','false')
win.mainloop()