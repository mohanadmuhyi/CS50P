due = 50
while due > 0:
    print(f"Amount Due: {due}")
    insert = int(input("Insert Coin: "))
    if insert in [5, 10, 25]:
        due = due - insert

print(f"Change Owed: {abs(due)}")
