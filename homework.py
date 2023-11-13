def sub(name, age, gender, balance):
    withdraw = input("You can take some money from your balance, (yes / no): ").lower()
    if withdraw == "yes":
        money = int(input("Write down how much you want to withdraw: "))
        print("Personal Details")
        print("Name: ", name)
        print("Age: ", age)
        print("Gender: ", gender)
        print("Insufficient Funds | Balance Available: ", balance - money, "$")


def bank(name, age, gender, balance):
    print("Personal Details")
    print("Name: ", name)
    print("Age: ", age)
    print("Gender: ", gender)
    print("Account has been updated: ", balance, "$")


def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    balance = int(input("Enter balance: "))
    bank(name, age, gender, balance)
    sub(name, age, gender, balance)


if __name__ == "__main__":
    main()
