#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employee:
    '''
        Employee is the base class for Ballerina.
    '''

    num_employee = 0

    def __init__(self, f_name = None, l_name = None, rank = 0, pay = 1000):
        self.f_name = f_name
        self.l_name = l_name
        self.rank = rank
        self.pay = pay
        self.email = f'{f_name}.{l_name}@something.com'
        self.inc_empl_count()

    def is_even_day(self, day):
        return day%2 == 0

    def promote(self):
        self.rank += 1

    def raise_salary(self, pay = 0):
        self.pay += pay

    @classmethod
    def count_employees(cls):
        return cls.num_employee

    @classmethod    
    def inc_empl_count(cls):
        cls.num_employee += 1

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def __repr__(self):
        return f'Employee name: {self.f_name} {self.l_name}\nCurrent rank and salary: {self.rank} {self.pay}\nE-Mail: {self.email}'

class Ballerina(Employee):
    '''
        Ballerina is the child class of Employee.
    '''
    def __init__(self, f_name = None, l_name = None, rank = 0, pay = 1000, dances = 0):
        self.dances = dances
        super(Ballerina, self).__init__(f_name, l_name, rank, pay)
    
    def __repr__(self):
        return super(Ballerina, self).__repr__() + f'\nNumber of dances: {self.dances}'


def main():
    '''
        Instantiates a Ballerina which is a child clase of base class employee.
        Outputs an example run of these objects being instantiated.
    '''
    b = Ballerina()

    print(b.count_employees())
    print(Employee.count_employees())
    print(b)


    class A(object):
        '''
            This is a docstring. Accessible via "A.__doc__"
        '''
        def __init__(self, test = 1):
            print(f'Class {self.__class__} initialized.')
            self.test = test

    a = A()

    for i in a.__dict__.keys():
        print(a.__dict__[i])
    
    print(Employee.__doc__)
    print(A.__doc__)


if __name__ == "__main__":
    main()


# In[ ]:




