from time import sleep
import json
import random
from page_3 import *

nl = '\n>> '
genderDict = {'0': '<Male>', '1': '<Female>'}

def switch(i):
    if i==0:
        return 1
    else:
        return 0
    
def ms(i):
    sleep(i/1000.0)

def test_marriage(me, i):
    if me.gender == i.gender :
        return False
    else:
        return True

myName = input(':: your name?'+nl)
myAge = int(input(':: age?'+nl))
myGender = int(input(':: male=0 | female=1'+nl))
myRelationship = int(input(':: are you single or not? (single=0 | married=1)'+nl))

# first question
answer = input(':: do you want to change your gender? (y \ n)'+nl)
if answer != 'n':
    for i in range(50):
        ms(10)
        print('|', end='')
    print('100%')
    myGender = switch(myGender)
    ms(500)
    print(':: your gender is changed successfully!')
    print()
    ms(1000)
    print(':: now you are a ' + genderDict[str(myGender)])
    ms(500)
    myName = input(':: pick your new name!'+nl)


myHeight = int(input(':: input your Height (cm) >> '))
# girls room!
if myGender == 1:    
    mySize = {'bust':int(input(':: input Bust size (cm) >> ')),
              'waist':int(input(':: input Waist size (cm) >> ')),
              'hips':int(input(':: input Hips size (cm) >> '))}
# boys room!
elif myGender == 0:
    mySize = {'chest':int(input(':: input chest size (cm) >> '))}

myWeight = int(input(':: input your Weight (kg) >> '))
# make a Human Class!
me = Human(myName, myGender, myAge, myHeight, mySize, myWeight, myRelationship, True)

if me.gender == 0:
    point0 = 'she'
    point1 = 'her'
elif me.gender == 1:
    point0 = 'he'
    point1 = 'his'
# making society! # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
society = []
for i in range(10):
    gender = random.randint(0,1)
    age = random.randint(14,50)
    height = random.randint(150,190)
    if gender == 0:
        size = {'chest': random.randint(60,120)}
    elif gender == 1:
        size = {'bust': random.randint(60,100),
                'waist': random.randint(45,90),
                'hips': random.randint(80,100)}
    weight = random.randint(35,80)
    relationship = 0
    society.append( Human('p'+ str(i), gender, age , height , size , weight , relationship , None ))

# MARRIAGE # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if me.relationship == 0:
    partner = None
    marriage_candidates = []
    for i in society:
        if test_marriage(me,i):
            marriage_candidates.append(i)
    if input(':: there are ' + str(len(marriage_candidates)) +' people who you can marry. do you have any marriage plan? (y / n)\n>> ') != 'n':
        print(':: i will tell you their names...')
        ms(500)
        for i in range(len(marriage_candidates)):
            print(str(i) + ': ' + str(marriage_candidates[i].__dict__))
            ms(500)
    
    candidate_index = input(':: is there any1 that you are intrested in? tell me ' + point1 + ' number.\n>> ')
    if candidate_index != '':
        candidate_index = int(candidate_index)
        partner = marriage_candidates[candidate_index]
        print(':: wow... so you are into ' + partner.name + '. now ' + point0 + ' is yours!')
        me.relationship = 1
        # other codes
    else:
        print(':: seems they are not good enough for you.')


# having sex # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if me.relationship == 1:
    print('<now you can have sex with your partner!>')

# SAVE Log!
print()
input('Enter to exit')
#with open('data.txt', 'w') as outfile:
    #json.dump(me.bio, outfile)
    #outfile.close() 