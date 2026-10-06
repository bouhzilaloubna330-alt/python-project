
students =[]

import json
while True:
    print("/n------ student systeme-------")  
    print("1.add student")  
    print("3.search setudent")
    print("4.delete setudent")
    print("5.exit") 


    choise = input("choose")
    if choise == "1":
      
        name = input("name")
        age = input("age")
        student= {"name":name,"age":age }
        students.append(student)
        with open("students.json","w") as file:
            json.dump(students,file)
        print ("students added")
        print(students)  
                  
    elif choise == "3" :
        
        name = input( "serch name")
        for student in students:
            if  student["name"] == name:
                print("found",student)
                break 
        else:
            print("not found")
    elif choise == "4":
       
        name = input("delet name")
        for student in students :
            if student["name"] == name :
                students.remove(student)
                print ("succefully delet")
                
            with open("students.json","w") as file:
              json.dump(students,file)   
            print("succefully delet",student)
            break
    elif choise == "5":
        break
    else:
        for student in students:
           
         print(student)
    
     

            
