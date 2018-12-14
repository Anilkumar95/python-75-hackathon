t = 99

def glob():
    global t
    t = 45
#the function could only access to the global varables
glob()
print(t)
