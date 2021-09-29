#上記の%%writefile sub1.pyｈ
print("function_1.pyをロードしました")
import tkinter
import tkinter.filedialog
import tkinter.messagebox
def get_filename():
    root=tkinter.Tk()    # 一番外に必要
    root.withdraw()    # 一番外に必要
    root.attributes("-topmost", True)       #<-最前面さらにマスターに追加さらにマスターに追加さらにマスターに追加　PUSHテストmutoh
    fTyp=[('pynote','*.ipynb'),('python','*.py'),('全て','*.*')]
    f =  tkinter.filedialog.askopenfilename(filetypes=fTyp)
    #print(f)
    return f
