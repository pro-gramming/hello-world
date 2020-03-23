hw="hello world "
n=int(input("Enter a No. to print the hello world that times"))
    
if n <= 3:
    print(hw*n)
else:
    print("runProgAgain", end=" ")

def good():
    print("good")

def name():
    return("dinesh")

st = input("Enter good or name to see String inside it")

if st == "good" :
    good()
elif st == "name":
    print(name())
else:
    print("Enter only any of above two to proceed")
    
