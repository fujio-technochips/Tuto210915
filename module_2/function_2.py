#上記の%%writefile sub1.pyｈ
print("function_2.pyをロードしましたよ～xx-----")
import os
def ExchangeExtension(fname,newext):
	# よくわからんけどコメント追加
    print(f"付け換え {fname} -> {newext}")
    path, ext = os.path.splitext(fname)
    path += newext;
    return path
