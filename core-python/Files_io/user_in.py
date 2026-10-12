def us_in():
    fl = open("./Files_txt/user_in", "w")
    ms = input('Enter your message:')
    while (ms!= 'quit'):
        fl.write(ms)
        fl.write(" ")
        ms=input(" ")
    fl.close()


us_in()
