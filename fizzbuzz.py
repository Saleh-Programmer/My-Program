listSample = range(100)
listFizzBuzz = []
for list in listSample:

    if list % 3 == 0 and list % 5 == 0:
        listFizzBuzz.append(f"{list}-->fizzbuzz")
    elif list % 3 == 0:
        listFizzBuzz.append(f"{list}-->fizz")
    elif list % 5 == 0:
        listFizzBuzz.append(f"{list}-->buzz")
    else:
        continue
help(listFizzBuzz.append)
print(listFizzBuzz)
