def writeline():
    fl=open("./Files_txt/2_write", "w")
    fl.write("Hi\n")
    fl.write("How are you?")
    fl.close()

writeline()