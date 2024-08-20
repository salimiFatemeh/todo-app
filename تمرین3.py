with open("file1.txt","w") as file:
    file.write("Hello You")

with open("file1.txt",'r') as file:
    content=file.read()
    print(content)
    print(len(content))