site_a = int(input())
site_b = int(input())

area = site_a * site_b
perimeter = (site_a + site_b) * 2

if area == perimeter:
    print("The sides form a square!")

print(f"The area is: {area}, \nThe perimeter is: {perimeter}")