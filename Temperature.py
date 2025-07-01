Temperatures = [23,30,41,56,32,18,22,26,29,25]

allowed_temp = [temp for temp in Temperatures if temp < 30 and temp >19]
print(f"During day time, the following temperatures were optimal for maximum motor operation\n {allowed_temp}")
cost = 35000
print(f"This will cost us about\n {cost*len(allowed_temp)} in euros")
if cost*len(allowed_temp) >= 10000:
  print("This is too much for us")
  print("Lets stabilize temperature during a day")
else:
  print("This is tolerable")
  
