def file_info():
    fo = open("./Files_txt/1_read", "r")
    print("fo Name", fo.name)
    print("fo Path", fo.mode)
    print("fo is closed", fo.closed)
    fo.close()
    print("is file closed now", fo.closed)


file_info()
