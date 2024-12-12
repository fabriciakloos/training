    # python

'''
    Timmy & Sarah think they are in love, but around where
they live, they will only know once they pick a flower each.
If one of the flowers has an even number of petals and the
other has an odd number of petals it means they are in love.
    Write a function that will take the number of petals of
each flower and return true if they are in love and false if
they aren't
'''


def petals(a,b):
    if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
        return True
    else:
        return False
    
a = int(input("Enter the number of petals of the Timmy's flower: "))
b = int(input("Enter the number of petals of the Sarah's flower: "))

print(petals(a,b))  # Output: True or False