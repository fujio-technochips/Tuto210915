#上記の%%writefile sub1.pyｈ
print("function_2.pyをロードしました")
import os
def ExchangeExtension(fname,newext):
    print(f"付け替え {fname} -> {newext}")
    path, ext = os.path.splitext(fname)
    path += newext;
    return path
