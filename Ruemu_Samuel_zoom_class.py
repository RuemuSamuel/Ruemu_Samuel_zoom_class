Results = {"brock":"80", "nuna":"93", "bryan":"99", "ugo":"89", "nicole":"85"}
Results.update({"sam":"78", "marrie":"92", "ria":"88"})
print(Results)

#makes dictionary values integers
Results_values= list(map(int, (Results.values()) ))
print(Results_values)

#gets the sum of the integers
sum=0
for i in Results_values:
    sum+=i

#calculates the average
Results_avg = (sum/(len(Results)))
print(Results_avg)

#calculates the number of students that got above average of 85
above_avg = 0
for i in Results_values:
    if i > 85:
        above_avg+=1
print("the number of students who got above average is" ,above_avg)


#to find the top mark and student in the class
top_mark = max(Results_values)
top_student = max(Results, key=lambda k: Results[k])
print("the top student is " ,top_student, "and he scored" ,top_mark)


#update the score of sam to a 95
Results["sam"]= "95"
print(Results)
