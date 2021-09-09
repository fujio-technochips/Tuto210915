#上記の%%writefile sub1.pyｈ
print("function_1.pyをロードしました")
import tkinter
import tkinter.filedialog
import tkinter.messagebox
def get_filename():
    root=tkinter.Tk()    # 一番外に必要
    root.withdraw()    # 一番外に必要
<<<<<<< HEAD
    root.attributes("-topmost", True)       #<-最前面さらにマスターに追加さらにマスターに追加
=======
    root.attributes("-topmost", True)       #<-最前面
    #競合するように変更した
>>>>>>> a26b11ca1d15183276bcbdeac081d19f33a6e5d9
    fTyp=[('pynote','*.ipynb'),('python','*.py'),('全て','*.*')]
    f =  tkinter.filedialog.askopenfilename(filetypes=fTyp)
    #print(f)
    return f
