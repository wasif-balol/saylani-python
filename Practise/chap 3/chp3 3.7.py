invitation=["Minhal","Amaan","Sadat"]
print("You are invited on dinner : ",invitation[0])
print("You are invited on dinner : ",invitation[1])
print("You are invited on dinner : ",invitation[2])
print(invitation[0],"will not come on dinner")
invitation[0] = "aleem"
print(invitation)
print("You are invited on dinner : ",invitation[0])
print("You are invited on dinner : ",invitation[1])
print("You are invited on dinner : ",invitation[2])
print("I have more space available on my dinner table")
invitation.insert(0,"salman")
invitation.insert(3,"aqib")
invitation.insert(5,"abuu")
print(invitation)
print("You are invited on dinner : ",invitation[0])
print("You are invited on dinner : ",invitation[1])
print("You are invited on dinner : ",invitation[2])
print("You are invited on dinner : ",invitation[3])
print("You are invited on dinner : ",invitation[4])
print("You are invited on dinner : ",invitation[5])
print("sorry i have place for only teo people")
popped1=invitation.pop(5)
print("sorry you are not invited",popped1)
popped1=invitation.pop(4)
print("sorry you are not invited",popped1)
popped1=invitation.pop(3)
print("sorry you are not invited",popped1)
popped1=invitation.pop(2)
print("sorry you are not invited",popped1)
invitation.remove("aleem")
invitation.remove("salman")
print(invitation)