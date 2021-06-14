#Chris Blanco 1900307
# Part-1

lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings_cups = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_cups))
print('{:.2f} cup(s) lemon juice'.format(lemon))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(nectar))

# Part-2
servings_required = float(input('\nHow many servings would you like to make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_required))
print('{:.2f} cup(s) lemon juice'.format(lemon * servings_required / servings_cups))
print('{:.2f} cup(s) water'.format(water * servings_required / servings_cups))
print('{:.2f} cup(s) agave nectar'.format(nectar * servings_required / servings_cups))

# Part-3
print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_required))
print('{:.2f} gallon(s) lemon juice'.format(lemon * servings_required / servings_cups / 16))
print('{:.2f} gallon(s) water'.format(water * servings_required / servings_cups / 16))
print('{:.2f} gallon(s) agave nectar'.format(nectar * servings_required / servings_cups / 16))


