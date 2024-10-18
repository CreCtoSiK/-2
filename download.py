
def swap_tens_and_units(number):
  hundreds = number // 100
  tens = (number % 100) // 10
  units = number % 10
  return hundreds * 100 + units * 10 + tens

try:
  number = int(input("Введите трехзначное число: "))

  if 100 <= number <= 999:
    new_number = swap_tens_and_units(number)
    print(f"Число с переставленными цифрами десятков и единиц: {new_number}")
  else:
    print("Некорректный ввод. Введите трехзначное число.")

except ValueError:
  print("Некорректный ввод. Введите целое число.")

