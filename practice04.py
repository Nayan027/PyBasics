fruits = ["app", "pear", "grapes", "guava"]

for i in fruits:
    print(i)

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


people = []
mail_id = []
job_role = []

for i in range(3):

    name = input("enter ur name: ")
    email = input("enter mail id: ")
    role = input("enter designation: ")

    people.append(name)
    mail_id.append(email)
    job_role.append(role)

print(people, mail_id, job_role)