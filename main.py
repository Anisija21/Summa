def countNumbers(teksts):
  summa = 0
  for simbols in teksts:
    summa = summa + int(simbols)
  return summa
a = input("Ievadiet skaitļus: ")
aaa = countNumbers(a)
print("Summa ir:", aaa)
