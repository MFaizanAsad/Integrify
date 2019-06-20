#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def function(n):

    if val_input(n):

        if n > 7:
            print("Course Passed.")

        elif n < 5:
            print('The current value of n is: {}\n'.format(n))
            n += 1
            return function(n)

        else:
            print('The current value of n is: {}\n'.format(n))
            n += 1
            return function(n)
    else:
        return function(bad_num(n))


def val_input(n):
    return isinstance(n, int) and n in range(11)


def bad_num(n):

    while n not in range(11) or not isinstance(n, int):

        n = int(input("Please only enter whole numbers between 0 and 10: "))

    return n


def run_program():

    call_func = input("Would you like to run the program? Y/N  ").lower()
    print(call_func)

    while not (call_func[0] == 'y' or call_func[0] == 'n'):
        call_func = input("Please select whether you would like to continue. Enter \"Y\" or \"N\"  ").lower()

    if call_func[0] == 'y':

        n = int(input("Enter a whole number between 0 and 10: "))
        function(n)
        run_program()

    else:
        return 0


run_program()


# In[ ]:




