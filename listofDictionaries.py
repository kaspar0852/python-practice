#smallest age from list of dictionaires

people = [
     { "name": "Tom", "age": 10 },
     { "name": "Mark", "age": 5 },
     { "name": "Pam", "age": 7 },
     { "name": "Dick", "age": 12 }
 ]

def searchsmallestage():
    s_age = people[0]['age']
    for sm_age in people:
        if sm_age['age'] < s_age:
            s_age = sm_age['age']    
            
    print(s_age)
    
searchsmallestage()
        
