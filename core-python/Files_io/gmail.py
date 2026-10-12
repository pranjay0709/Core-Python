import re
import os
def gmail():
    inp=open('./Files_txt/gmail',"r")
    out=open('./Files_txt/cr_gmail',"w")
    for line in inp:
        if(re.search("@gmail.com",line)):
            out.write(line)
    inp.close()
    out.close()

gmail()