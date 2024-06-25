from validation_function import is_numeric
while True:
    q = input("Add contact(a) Search Contact(s) Quit(q) : ");
    if ( q == 'a'):
        with open("Contact.txt", 'a') as f:
            name = input("Please Enter name: ")
            phone = input("Please Enter Phone no. : ")
            if len(phone) != 10:
                print('Please enter the correct phone no...')
            elif is_numeric(phone) is False:
                 print('Please enter the correct phone no...')
            else:
                f.writelines(((name.title()), ' : ', phone,'\n'))
    elif ( q == 's' ):
            with open("Contact.txt", 'r') as z:
                find = input("Search : ")
                print("")
                for i in z:
                    if find in i:
                        print(i)
    elif ( q == 'q' ):
            print("Thank You !!")
            break
    else:
            print("Please Enter Valid Input....")