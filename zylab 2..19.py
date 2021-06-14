# Chris Blanco 1900307
# this is the first part


lemon = float(input('Enter amount of lemon juice (in cups): '))
water = float(input('Enter amount of water (in cups): '))
agave = float(input('Enter amount of agave nectar (in cups): '))
servings = float(input('Enter amount of agave servings does this make? '))

print("")
print('\nLemonade ingredients - yields {:.2f} servings'.format(servings))
print(str('{:.2f}'.format(lemon))+' cup(s) lemon juice')
print(str('{:.2f}'.format(water))+' cup(s) water')
print(str('{:.2f}'.format(agave))+' cup(s) agave')


#the 2nd part begins here

diff_servings = float(input('How many servings would you like to make?'))
abc = diff_servings / servings
new_lemon = lemon * abc
new_water = water * abc
new_agave = agave * abc

print("")
print('\nLemonade ingredients - yields {:.2f} servings'.format(diff_servings))
print(str('{:.2f}'.format(new_lemon))+' cup(s) lemon juice')
print(str('{:.2f}'.format(new_water))+' cup(s) water')
print(str('{:.2f}'.format(new_agave))+' cup(s) agave')

# part 3

print('Lemonade ingredients - yields {:.2f} servings' .format(diff_servings))
print(str('{:.2f}'.format(new_lemon/16))+' cup(s) lemon juice')
print(str('{:.2f}'.format(new_water/16))+' cup(s) water')
print(str('{:.2f}'.format(new_agave/16))+' cup(s) agave')






