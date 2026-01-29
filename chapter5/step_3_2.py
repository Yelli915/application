import deepl
from pathlib import Path
from step_1 import IN_DIR
from step_2_2 import read_text

def read_text_translated(path:Path, target_lang:str="EN") -> list :
    text_list = read_text(path)
    DEEPL_KEY = "09eb50be-913d-4b9e-a8c4-04263a0fc182:fx"
    tran = deepl.Translator(DEEPL_KEY)
    result = []
    for coords,text,prob in text_list :
        resp = tran.translate_text(text,target_lang="KO")
        result.append((coords,resp.text,prob))
    return result

if __name__ == "__main__" :
    path = IN_DIR/"ocr.jpg"
    print(read_text_translated(path))