print("The Bank of Khan")
pin = int(input("Enter your PIN: "))
while pin != 1234:
  pin = int(input("Incorrect pin. Enter your pin again: "))
  if pin==1234:
    print("Pin Accepted")