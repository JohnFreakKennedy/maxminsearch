x = input("Please, put your digit: ")
try:
    x = int(x)
except:
    print("wrong value")
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

print("Finish")
