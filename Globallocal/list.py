#basically lists cannot be made global
li=["one","two"]
def list():
    global li
    li =["three","four"]

list()
print(li)
