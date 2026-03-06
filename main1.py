a = int(input("enter value 1: "))
b = int(input("enter value 2: "))
c = int(input("enter value 3: "))

avg = (a + b + c) / 3
print("Average =", avg)

if avg > a and avg > b:
    print("%f is higher than %d, %d" % (avg, a, b))
elif avg > a and avg > c:
    print("%f is higher than %d, %d" % (avg, a, c))
elif avg > b and avg > c:
    print("%f is higher than %d, %d" % (avg, b, c))
elif avg > a:
    print("%f is just higher than %d" % (avg, a))
elif avg > b:
    print("%f is just higher than %d" % (avg, b))
elif avg > c:
    print("%f is just higher than %d" % (avg, c))
else:
    print("invalid input")