#Guess Password

tries = 4
mainpass = "dina@1234"
inputpass = input("writ password: ")
while mainpass != inputpass:
    tries-=1
    print(f"wrong password, {'last' if tries ==0 else tries} chance left")

    inputpass = input("writ password: ")
    
    if tries==0:
        print ("All tries is finished")
        break
else:
    print("correct password")