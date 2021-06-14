# Chris Blanco 1900307
from datetime import date


def calculateAge(currentDate, birthDate):
    today = currentDate
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


# the main code
a = 1981
b = 9
c = 21
print("Birthday Calculator")
print('Current Day')
m = int(input('Month: '))
d = int(input('Day: '))
y = int(input('Year: '))
print('Birthday')
xm = int(input('Month: '))
xd = int(input('Day: '))
xy = int(input('Year: '))
print("You are ", calculateAge(date(y, m, d), date(xy, xm, xd)), "years old.")
if d == xd:
    print("Happy Birthday!")
    

