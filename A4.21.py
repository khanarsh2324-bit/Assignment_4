print("A4.21")
s = input("Enter a string: ")  #for inour string from user
vowels = "aeiouAEIOU"
count = 0                   #starting value is 0
for char in s:    
    if char in vowels:        
        count = count + 1   #it takes current value of counting and 1 in it if vowel found
print("Number of Vowels :", count)
