def fahrenheit_convert(C):
    fahrenheit = int(C) * 9/5 + 32
    return str(fahrenheit) + 'F'
print(fahrenheit_convert(30))

def trapezoid_area(base_up, base_down, height):
    return 1/2 * (base_down + base_up) * height
print(trapezoid_area(1,2,3))
print(trapezoid_area(height=3,base_up=1,base_down=2))
