# Chris Blanco 1900307

def Cost(a):
 if a == "Oil change":
  return 35
 if a == "Tire rotation":
  return 19
 if a == "Car wash":
  return 7
 if a == "Car wax":
  return 12

print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

fir = input("Select first service:\n")
sec = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")

one = Cost(fir)
two = 0
print("Service 1: %s, $%s" % (fir, one))

if sec == "-":
  print("Service 2: No service")
else:
  two = Cost(sec)
  print("Service 2: %s, $%d" % (sec, two))

  print("\nTotal: $%d" % (one + two))

  








