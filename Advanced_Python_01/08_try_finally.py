def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey I am inside of finally it will always execute whether it is in a function or not")

    print("hey this will only works in a simple program not in a function")

main()