import csv
# تبدیل به لیست در پایتون
with open("weather.csv","r") as file:
    data=list(csv.reader(file))
# print(data)

city=input("Enter city name: ")
for row in data:
    if row[0]==city:
        print(row[1])