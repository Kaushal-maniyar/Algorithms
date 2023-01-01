denomination = []

num = int(input("How many denominations you want : "))
for i in range(num):
  a = int(input(f"Enter denomination {i+1} : "))
  denomination.append(a)

denomination.sort(reverse=True)
part = -1
amount = int(input("Enter amount : "))
for i in denomination:
  if i == amount:
    part = denomination.index(i)
    break

change = {}
for i in denomination[part+1:]:
  if amount >= i:
    feq = int(amount/i)
    amount = amount - feq*i
    change[i] = feq

print("Change : ")
for key, value in change.items():
  if value > 1:
    print(f"{value} coins of {key}")
  else:
    print(f"{value} coin of {key}")
