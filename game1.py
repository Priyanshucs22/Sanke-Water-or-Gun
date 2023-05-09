# snake , water and gun or stone , paper and secisor
# import random
# def gamewin(comp,you):
#     if comp==you:
#         return None
#     if you=='stone':
#         if comp=='secisor':
#             return 'true'
#         elif comp=='paper':
#             return 'false'
#     if you=='paper':
#         if comp=='stone':
#             return 'true'
#         elif comp=='secisor':
#             return 'false'
#     if you=='secisor':
#         if comp=='stone':
#             return 'false'
#         elif comp=='paper':
#             return 'true'
        
# print("Comp turn : stone , paper and secisor?")

# randNo=random.randint(1,3)
# if randNo==1:
#     comp='stone'
# elif randNo==2:
#     comp='paper'
# elif randNo==3:
#     comp='secisor'

# you=input("Your turn : stone , paper and secisor?")

# a=gamewin(comp,you)

# print(f"computer choose {comp} ")     
# print(f"you choose {you} ")

# if a==None:
#     print("The game is a tie")
# elif a:
#     print("you win")
# else :
#     print("you loose")        