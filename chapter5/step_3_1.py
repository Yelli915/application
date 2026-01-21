import deepl

DEEPL_KEY = "09eb50be-913d-4b9e-a8c4-04263a0fc182:fx"
tran = deepl.Translator(DEEPL_KEY)
resp = tran.translate_text("Hello World",source_lang="EN",target_lang="KO")
print(resp.text)