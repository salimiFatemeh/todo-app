temperatures = [10, 12, 14]

file = open("file.txt", 'w')

for temperature in temperatures:
    file.writelines(str(temperature)+"\n")

file.close()