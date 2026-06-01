print("ANAGRAM TESTING")

str1=input("Enter first string: ").replace(" ", "").lower()
str2=input("Enter second string: ").replace(" ", "").lower()

if len(str1)!=len(str2):
    print("Not anagrams")
else:
    count={}

    for char in str1:
        count[char]=count.get(char,0)+1

    for char in str2:
        count[char]=count.get(char,0)-1

    if all(value==0 for value in count.values()):
        print("Anagrams")
    else:
        print("Not Anagrams")