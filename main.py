# def       funtion keyword
#addition    funtion name
#print        Task



def addition(num1, num2):
        if type(num1) != int or type(num2) != int:
            print ("allowed only integers")
        else:
            print (num1 + num2)
addition(100,500)

#---------------------------------------------------------

myTuple = ("Html", "CSS", "JS")
mySkills = {
    "Go": "40%",
    "Python": "50%",
    "MySQL": "80%"
    } 

def show_skills(name, *skills, **skillwithprogress):
    print (f"My name is {name}:")
    for skill in skills:
        print(f"- {skill}")
    for skill_key, skill_value in skillwithprogress.items():
        print (f"-{skill_key} => {skill_value}")
show_skills ("Dina", *myTuple, **mySkills)
