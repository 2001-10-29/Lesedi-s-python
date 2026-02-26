file =open("data.txt","r")
content = file.read()
print(content)
file.close()

newfile =open("output.txt","w")
newfile.write("Hello Python\n")
newfile.write("File handling is useful")
newfile.close()

file =open("output.txt","a")
file.write("\nAppending new line to the file.")
file.close()

name =input("Enter student name: Lesedi ")

file =open("students.txt","a")
file.write(name +"\n")
file.close()

file =open("output.txt","w")
file.write("Hello Python\n")
file.write("File handling is useful")
file.close()


