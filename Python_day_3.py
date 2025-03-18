Students = ["Amrish", "aachal", "Ashutosh", "Shital", "Ravina", "arav","bag"]

#Create separate list for students whose name starts with a
def startwith_a(Students):
    stuent_with_a = []
    for i in Students:
        if i.startswith("A"):
            stuent_with_a.append(i)
        elif i.startswith("a") :
            stuent_with_a.append(i)   
    return stuent_with_a
        
newList = startwith_a(Students)    
print(newList)    

# create list where all the string have at least 2 vowels
def at_least_two_vowels(Students):
    student_with_two_vowels = []
    for i in Students:
        vowels = ["a", "e", "o", "i", "u"]
        count = 0
        for j in i:
            if j.lower() in vowels:
                count += 1
                if count >= 2:
                    student_with_two_vowels.append(i)
    return student_with_two_vowels

two_vowels = at_least_two_vowels(Students)
print(two_vowels)

#Find Consonent and if found double it and add 'o' after it

def double_consonent(Students):
    student_with_double_consonent = []
    for i in Students:
        for j in i:
            lowercase = j.lower()
            print(lowercase)
            vowels = ["a", "e", "o", "i", "u"]
            if lowercase not in vowels:
                student_with_double_consonent.append(j*2 + 'o')
            
    return student_with_double_consonent
        
double = double_consonent(Students)
print(double)        

#String More than n length
def more_length(Students):
    student_more_length = []
    for i in Students:
        if len(i) > 4:
            student_more_length.append(i)
    return student_more_length

more_length_result = more_length(Students)
print(more_length_result)
        