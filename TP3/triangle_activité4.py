print("donner les cotés du triangle ")
a= int(input("donner la coté a: "))
b= int(input("donner la coté b: "))
c= int(input("donner la coté c: "))

if (a*a + b*b== c*c): 
    print("ABC est un triangle rectongle en a")
elif (b*b + c*c == a*a):
    print("ABC est un triangle rectongle en b")
elif (c*c + a*a == b*b):
    print("ABC est un triangle rectongle en c")
else:
    print("ABC n'est pas rect ")
