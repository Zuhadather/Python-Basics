# IF
MyValue = int(input("Please Enter the Number"))

if MyValue < 0: print("X is Zero")
if MyValue == 1: print("X is One")
if MyValue == 2:
    print("X is Two")
else:
    print("X is Above Condition")

# FOR LOOP


words = ['Juhi', "Ather", 'Aamina And Zsquare']

for w in words[:]:
    print(w, len(w))
#Range

for i in range (5):
    print("Range " + str(i))

    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])
