import csv, random

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding = "utf-8") as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)
# [0][9]
while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
       ch =  int(input("Type here dein number "))
       print (apartments[ch-2])
    elif choice == '2':
        def sortede(apartment):
            return int(apartment[-1])
        neu = sorted(apartments, key =sortede, reverse = True) 
        for i in range(10):
            print(neu[i])
    elif choice == '3':
        def sortede(apartment):
            return int(apartment[-1])
        neu = sorted(apartments, key =sortede) 
        for i in range(10):
            print(neu[i])
    elif choice == '4':
        prices = int(input("Type dein price"))
        def firstsorted(apartments):
            return int(apartments[-1])
        sorted_apartments = sorted(apartments, key =firstsorted)
        
        filtered_apartments = []
        for apartment in sorted_apartments:
            if prices > int(apartment[-1]):
                filtered_apartments.append(apartment)

        print(filtered_apartments[:20])
    elif choice == '5':
        prices = int(input("Type dein price"))
        def firstsorted(apartments):
            return int(apartments[-1])
        sorted_apartments = sorted(apartments, key =firstsorted)
        
        filtered_apartments = []
        for apartment in sorted_apartments:
            if prices < int(apartment[-1]):
                filtered_apartments.append(apartment)

        print(filtered_apartments[:20])

    elif choice == '6':
        print (choice(apartments))
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")
