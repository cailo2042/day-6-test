# opening and editing files in python
role_file= open("roles.txt","r")
print(role_file.readline())
#close file.
role_file.close()

file= open("./roles.txt","r")
words=file.read()
print(words)

