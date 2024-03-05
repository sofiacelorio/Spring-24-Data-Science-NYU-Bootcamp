# Spring 24' Data Science Bootcamp
# Sofía Celorio Vicente
# Exercise 1

word = str(input("Enter a word: "))
vowels = "aeiouAEIOU"
count_vowels = 0

for x in word:
        if x in vowels:
            count_vowels += 1
            
print("Number of vowels in ",word, ": ",count_vowels,sep='')
