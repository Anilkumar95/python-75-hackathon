#appending lines to the given file
append= open("file.txt", "a")
append.write("How are u man?")
read =open("file.txt","r")
print(read.read())
