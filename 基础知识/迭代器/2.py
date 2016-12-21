s = "fish"
it = iter(s)
var = 1

while var == 1:
    try:
        ea = it.next()
    except StopIteration:
        break
    print ea
