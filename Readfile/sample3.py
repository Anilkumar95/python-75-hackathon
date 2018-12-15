#printing the file size in bytes
def file_size(fname):
        import os
        get = os.stat(fname)
        return get.st_size

print("The size of the file is : ",file_size("dummy.txt"))
