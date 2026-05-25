result = lambda x, y: (x + y, x * y)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_result, product_result = result(a, b)

print("Sum:", sum_result)
print("Product:", product_result)