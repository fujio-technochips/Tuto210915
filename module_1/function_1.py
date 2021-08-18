#上記の%%writefile sub1.pyｈ
print("function_1.pyをロードしました")
import tkinter
import tkinter.filedialog
import tkinter.messagebox
def get_filename():
    root=tkinter.Tk()    # 一番外に必要
    root.withdraw()    # 一番外に必要
    fTyp=[('pynote','*.ipynb'),('All','*.*')]
    f =  tkinter.filedialog.askopenfilename(filetypes=fTyp)
    #print(f)
    return f
