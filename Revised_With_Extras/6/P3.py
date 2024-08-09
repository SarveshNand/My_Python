s1 = "Make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

message = input("Enter your comment: ")

if(s1 in message or s2 in message or s3 in message or s4 in message):
    print("This is a SCAM!!!")
else:
    print("Proceeding Message")