st= input("Enter the Message: \n")
words = st.split(" ")
coding = int(input("Enter the 1 for coding and 2 for decoding"))
if(coding == 1):
    nwords = []
    for word in words:
        if(len(word) >= 3 ):
            r1 = "asd"
            r2 = "fef"
            stnew = r2 + word[1:] + word[0] + r1 
            print(word)
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

elif(coding == 2):
    nwords = []
    for word in words:
        if(len(word) >= 3 ):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    print("Invalid input")