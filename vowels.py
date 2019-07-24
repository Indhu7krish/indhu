a=input()
a=a.lower()
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print("Vowel")
elif(97<=ord(a)<=122):
    print("Consonant")
else:
    print("Invalid Input")
