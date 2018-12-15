try:
    error= open("dummy.txt","r")
    print(error.read())# perform file operations
finally:
   error.close()
