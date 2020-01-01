def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a - b  

def multiply(a,b):
    print(f"Multiplying {a} * {b}")
    return a * b  

def divide(a,b):
    print(f"Adding {a} / {b}")
    return a / b     

print("Lets do some math with these functions!")  

age  = add(30,5) 
height  = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"ADD: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

#a puzzle fir the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print(f"Result: {what}")
