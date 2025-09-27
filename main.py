import json
def write_json(info):
    try:
      with open('contacts.json', 'w') as f:
           json.dump(info, f)
    except FileNotFoundError:
        print('File not found')
        with open('contacts.json','w') as f:
            json.dump(info, f)
            print('new contact created')

def read_json():
        try:
            with open('contacts.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print('File not found')
            with open('contacts.json', 'w') as f:
                json.dump({}, f)
                print('File created!')

dct={}
while True:
    print("enter your choice:")
    print("1.add your number")
    print("2.show numbers")
    print("3.search")
    print("4.exit the program")

    choice=input("your choice:")
    if choice=="1":
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        number = int(input("Enter your number: "))
        fullname =f"{fname} {lname}"
        dct[fullname] = number
        info = write_json(dct)
        print("your number successfully added!")
    # print(dct)

    elif choice=="2":
        dct=read_json()
        if dct:
            print("contacts:")
            for name, num in dct.items():
                print(f"{name}: {num}")
        else:
            print("No contacts found!")

    elif choice=="3":
        dct=read_json()
        search=input("enter name: ")
        results = [f"{name}: {num}" for name, num in dct.items() if search.lower() in name.lower()]
        if results:
            print("\n".join(results))
        else:
            print("not found!")
        # if search in dct:
        #     print("number:",dct[search])


    elif choice=="4":
        print("Exiting program...")
        break
    else:
        print("invalid input")


