file =open("data.txt","r")
content = file.read()
print(content)
file.close()

newfile =open("output.txt","w")
newfile.write("Hello Python\n")
newfile.write("File handling is useful")
newfile.close()


