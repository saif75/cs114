
print("please enter the ammount of change to convert less than 100")
change = int(input())
num_quarters = change // 25
print(num_quarters)
run_total = change - (num_quarters * 25)
print(run_total)
num_dimes = run_total // 10
print(num_dimes)
run_total = run_total - (num_pennies * 100)
print(run_total)
num_pennies = run_total // 100
print(num_pennies)
run_total = run_total - (num_pennies * 100)
print(run_total)
