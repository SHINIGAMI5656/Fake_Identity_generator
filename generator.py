#python
import math
import random
from datetime import date,timedelta
from PIL import Image

#Date-Of-Birth
test_date1, test_date2 = date(1995, 1, 1), date(2005, 12, 31)
res_dates = [test_date1]
  
while test_date1 != test_date2:
    test_date1 += timedelta(days=1)
    res_dates.append(test_date1)
  
res = random.choice(res_dates)
print("Date of Birth is : " + str(res))

#Age
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age

print("Age=",calculateAge(res), "years")


#Gender
list1=['Male','Female']
b=random.choice(list1)
print('Gender=', b)


#Name
male_name=['Abhishek', 'Anij', 'Charan', 'Diep', 'Hiral', 'Jatin', 'Kanha', 'Mohan', 'Yash']
female_name=['Beena', 'Denali', 'Gauri', 'Sriza', 'Poonam', 'Jyoti', 'Aasha', 'Anisha', 'Pooja']
if(b=='Male'):
	mn=random.choice(male_name)
	print('Name=',mn)
else:
	fn=random.choice(female_name)
	print('Name=',fn)

#Last Name
last_name=['Anand', 'Reddy', 'Patel', 'Singh', 'Kumar', 'Gore', 'Bendre', 'Punekar', 'Jadhav', 'Pandey', 'Shetty']
ln=random.choice(last_name)
print('Last Name=',ln)

#email
if(b=='Male'):
	ri=random.randint(10,100)
	print(mn,end="")
	print(ri,end="")
	print('@gmail.com')
else:
	ri=random.randint(10,100)
	print(fn,end="")
	print(ri,end="")
	print('@gmail.com')

#blood_group
bg=['a-','a+','b-','b+','ab-','ab+','o-','o+']
print('Your blood group is', random.choice(bg))

#phone number
print('Phone number is',end=" ")
print(9,end="")
for i in range(9):
	print(random.randint(0,9),end="")

#print photo
if(b=='Male'):
	r=random.randint(1,7)
	jn='m'+str(r)
	img = Image.open(jn+".jpg")
	img.show()
else:
	r=random.randint(1,7)
	jn='f'+str(r)
	img = Image.open(jn+".jpg")
	img.show()
