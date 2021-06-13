class GymManager:
    regimen={}
    customer = dict()
    def __init__(self,s_id,s_name):
        self.s_id = s_id
        self.s_name = s_name
        
    @classmethod
    def addCustomer(cls,customer):
        GymManager.customer[customer.getPhoneNo()] = customer
obj = GymManager('s_1','YFC')

class Customer:

    def __init__ (self,name='',age='',gender='',phoneNo='',email='',bmi='',duration=''):
        self.__name = name
        self.__phoneNo = phoneNo
        self.__age = age
        self.__gender = gender
        self.__email = email
        self.__bmi = bmi
        self.__duration = duration

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setPhoneNo(self, phoneNo):
        self.__phoneNo = phoneNo

    def getPhoneNo(self):
        return self.__phoneNo

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setBMI(self,bmi):
        self.__bmi = bmi

    def getBMI(self):
        return self.__bmi

    def setDuration(self,duration):
        self.__duration = duration

    def getDuration(self):
        return self.__duration

    def __str__(self):
        return self.getName()+" "+self.getPhoneNo()+" "+self.getDuration()+" "+self.getAge()+" "+self.getGender()


print("****GYM MANAGER PORTAL****")
print("Welcome SuperUser, Please select a choice from the menu")

def menu():
    print("\nEnter Your Choice: ")
    print("1. Create Member")
    print("2. View Member")
    print("3. Delete Member")
    print("4. Update Member")
    print("5. Create Regimen")
    print("6. View Regimen")
    print("7. Delete Regimen")
    print("8. Update Regimen")
    print("0. Exit")


menu()

while(True):
    option = int(input())
    if option == 1:
        name = str(input("Enter Member Name:- "))
        age = str(input("Enter Member age:- "))
        gender = str(input("Enter Member gender:-"))
        phoneNo = str(input("Enter Member phoneNo:- "))
        email = str(input("Enter Member Email:- "))
        bmi = str(input("Enter Member BMI:- "))

        if bmi<'18.5':
            r = {'Mon':'Chest','Tue':'Biceps','Wed':'Rest','Thu':'Back','Fri':'Triceps','Sat':'Rest','Sun':'Rest'}

        elif bmi<'25':
            r = {'Mon':'Chest','Tue':'Biceps','Wed':'Cardio/Abs','Thu':'Back','Fri':'Triceps','Sat':'Legs','Sun':'Rest'}

        elif bmi<'30':
            r = {'Mon':'Chest','Tue':'Biceps','Wed':'Abs/Cardio','Thu':'Back','Fri':'Triceps','Sat':'Legs','Sun':'Rest'}

        elif bmi>='30':
            r = {'Mon':'Chest','Tue':'Biceps','Wed':'Cardio','Thu':'Back','Fri':'Triceps','Sat':'Cardio','Sun':'Cardio'}

        duration = str(input("Enter Member Duration(in months):- "))
        customer = Customer(name,age,gender,phoneNo,email,bmi,duration)
        GymManager.regimen[phoneNo] = r
        GymManager.addCustomer(customer)
        print("Your Membership is created")
        menu()



    elif option == 2:
        check_phn = input('Enter phone number of member:-')
        print("Name\tAge\tGender\tphone\tEmail\tBMI\tDuration")
        for cusid in GymManager.customer.keys():
            if cusid == check_phn:
                customer = GymManager.customer[cusid]
                name = customer.getName()
                age = customer.getAge()
                gender = customer.getGender()
                phoneNo = customer.getPhoneNo()
                email = customer.getEmail()
                bmi = customer.getBMI()
                duration = customer.getDuration()
                print(name + "\t" +age+ "\t" +gender+ "\t" + phoneNo + "\t" + email + "\t" + bmi + "\t" + duration)
        print("\n")
        menu()


    elif option == 3:
        check_phn = input('Enter phone number of member you want to delete:- ')
        try:
            for cusid in GymManager.customer.keys():
                if cusid == check_phn:
                    print("Member Deleted")
            GymManager.customer.pop(check_phn)

        except:
            print("Number doesn't exist\n")
        menu()


    elif option == 4:
        check = input("Enter phone no:- ")
        exr = input("Enter if you want to extend or revoke:-")
        if exr == 'extend':
            for cusid in GymManager.customer.keys():
                customer = GymManager.customer[cusid]
                if cusid == check:
                    dur = customer.getDuration()
                    s = int(dur)+int(input("Enter how many months you want it to be extented for:-"))
                    res = str(s)
                    customer.setDuration(res)
        elif exr == 'revoke':
            for cusid in GymManager.customer.keys():
                customer = GymManager.customer[cusid]
                if cusid == check:
                    customer.setDuration('0')
                    print("MemberShip Revoked")
        menu()



    elif option == 5:
            phn = input("Enter the phone number you want to create regimen:- ")
            for i in GymManager.regimen:
                if i == phn:
                    for j in GymManager.regimen[i]:
                        GymManager.regimen[i][j]=input(j+":")
            menu()

    elif option == 6:
            check_phn = input('Enter phone number of memeber:-')
            for i in GymManager.regimen:
                if i == check_phn:
                    for key,val in GymManager.regimen[i].items():
                        print(key,":",val)
            print("\n")
            menu()

    elif option == 7:
            check_phn = input('Enter phone number of member:-')
            for i in GymManager.regimen:
                if i == check_phn:
                    print("Workout regimen deleted")
            GymManager.regimen.pop(check_phn)
            print("\n")
            menu()

    elif option == 8:
            check_phn = input('''Enter the phone number of member who's regimen you want to update:- ''')
            for i in GymManager.regimen:
                if i == check_phn:
                    d = input("Enter the day which you want to update:- ")
                    for j in GymManager.regimen[i]:
                        if j==d:
                            GymManager.regimen[i][j] = input("Enter the workout:- ")
                            print("Updated sucessfully!!!!!")
            print("\n")
            menu()


    elif option == 0:
            break

    else:
        print("Please enter a valid number ")

menu()

def menu():
    print("\nWelcome To Member Portal\n")
    print("\nEnter your Choice:- ")
    print("1. My Regimen")
    print("2. My Profile")
    print("3. Exit")


menu()
while(True):
    option = int(input())
    if option == 1:
        p = input("Enter your phone number:- ")
        print("--Your Regimen based on your BMI--")
        for i in GymManager.regimen:
            if i==p:
                for key,val in GymManager.regimen[i].items():
                    print(key,":",val)
        print("\n")

    elif option == 2:
        p = input("Enter your Phone Number:- ")
        try:
            for cusid in GymManager.customer.keys():
                if cusid == p:
                    customer = GymManager.customer[cusid]
                    name = customer.getName()
                    age = customer.getAge()
                    gender = customer.getGender()
                    phoneNo = customer.getPhoneNo()
                    email = customer.getEmail()
                    bmi = customer.getBMI()
                    duration = customer.getDuration()
                    print("Your Profile")
                    print("Name:",name,"\nAge:",age,"\nGender:",gender,"\nPhoneNo:",phoneNo,"\nEmail:",email,"\nBMI:",bmi,"\nDuration:",duration)
        except:
            print("No user with this number exist")
    elif option == 3:
        break

    else:
        print("Please Enter the valid number ")
    menu()






