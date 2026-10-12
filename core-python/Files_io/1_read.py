def readline():
    fl=open("./Files_txt/1_read", "r")
    text=fl.read()
    print(text)
    fl.close()
readline()