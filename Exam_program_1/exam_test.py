#https://github.com/SFJBS-FSD-1/challenges_12sept-lellabhaskar

# go to terminal
# git init
# git status
# git add .\exam_test.py
# git commit -m "added file exam_test.py challenges"

# git remote add origin https://github.com/SFJBS-FSD-1/challenges_12sept-lellabhaskar
# git push -u origin master

# Challenges:
#print('test')

#1:  Write a function that takes a natural number as input and outputs the number of digit in it.
     #Conversion of number to string is not allowed

# natural_number=int(input("please enter a natural number"))
# digit_count=0
# convert_list=str(natural_number)
# for number in convert_list:
#     digit_count=digit_count+1
# print(f"The user enter number of digits are {digit_count}")

#2: Write a function that takes a natural number as input and outputs the reverse of that number.

# natural_number=int(input("please enter a natural number"))
# count=0
# convert_strlist=str(natural_number)
# reverse_number=convert_strlist[::-1]
# print(reverse_number)

#3:Write a function where user will enter a natural number as input and output returns the number of zeroes in the end of the factorial of that number.
   #Conversion of number to string is not allowed

usernum = int(input("please enter a natural number"))
fact_number = 1
while usernum >= 1:
    fact_number = fact_number * usernum
    usernum = usernum - 1
print(f'fact_number of the number is {fact_number}')

count=0
while fact_number:
    give_num=fact_number//10
    reminder = give_num % 10
    fact_number=give_num
    count = count + 1
    if reminder!=0:
        break

#print(count)


print(f'number of zeros after factorial are {count}')

# Challenge 4

# list1 = ["India" , "England", "Spain"]
#
# list2 = ["Delhi","London","Madrid"]
#
# mydict = {}
# for i in range(len(list1)):
#     mydict[list1[i]]=list2[i]
# print(mydict)

#Challenge 5
#city = {"Mumbai": {“Latitude”: “19.07'53.2” , “Longitude”: “72.54'51.0”},
             #“Delhi” : {“Latitude”: “28.33'34.1” , “Longitude”: “77.06'16.6”} }

# places = {("19.07'53.2", "72.54'51.0"): "Mumbai",("28.33'34.1","77.06'16.6"): "Delhi"}
# #print(places)
# dict={}
# listvalues=[]
# temdict={}
# for keys,values in places.items():
#     listvaues=list(keys)
#     temdict['Latitude']=listvaues[0]
#     temdict['Longitude'] = listvaues[1]
#     dict[values]=temdict
# print(dict)

#Challenge 6

# mylist  =  [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
# #x = lambda a: a%2
# #print(x(3))
# evenlist=[]
# for number in mylist:
#     if number%2==0:
#         evenlist.append(number)
# #print(evenlist)
# sum=0
# for even in evenlist:
#     sum=sum+even
#     #print(sum)
# print("total of even numbers are ",sum)


