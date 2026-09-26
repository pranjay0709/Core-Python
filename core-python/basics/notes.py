amount= 2526
notes=[500,200,100,50,20,10,5,2,1]
for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note

        #print(note, "note(s) :", count)

num = 200
l=len(notes)
for i in range(l):
    if notes[i]==num:
        print("present at i",i)
