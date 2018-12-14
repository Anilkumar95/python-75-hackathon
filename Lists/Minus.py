def Diff(li1, li2):
    return (list(set(li1) - set(li2)))
li1=['one','Yuvan']
li2=['two','frog','one']
li3=Diff(li2,li1)
print(li3)
