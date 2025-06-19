groc = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        break
    else:
        if item in groc:
            groc[item] += 1
        else:
            groc[item] = 1

sorted_keys = sorted(groc.keys()) # sort keys to use them to sort dict

new_groc = {} # new dict which is sorted

for i in sorted_keys:
    new_groc[i] = groc[i] # assign the sorted dict

for i in new_groc:
    print(new_groc[i], i) # print the value then the key
