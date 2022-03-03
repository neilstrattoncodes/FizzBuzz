
# Fizz Buzz program
# Neil Stratton March, 3, 2022
# Sprint Week


while True:

    for fizzbuzz in range(101):
        if fizzbuzz % 5 == 0 and fizzbuzz % 8 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 5 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 8 == 0:
            print("buzz")
            continue
        print(fizzbuzz)

    enter_new_info = input("Would you like to enter a info Y for Yes: ").upper()
    print("")

    if enter_new_info == "Y":
        continue
    else:
        break