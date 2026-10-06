num = 3.14159
print(f"{num:.2f}")

price = 125.5
print(f"Price: Rs. {price:.2f}")

num = 123
print(f"{num:10}")

num = 123
print(f"{num:->10}")    # -------123
print(f"{num:-<10}")    # 123-------
print(f"{num:#^10}")    # ###123####

print(f"{'Item':<12}{'Price':>5}")
print("-" * 17)
print(f"{'Apple':<12}{3:>5}")
print(f"{'Banana':<12}{10:>5}")
print(f"{'Orange':<12}{200:>5}")
