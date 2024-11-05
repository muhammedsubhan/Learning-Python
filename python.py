# print("what is your name ? " , end=" ")
# name = input()
# print("what is your age ? "  , end=" ")
# age = input()
# print("what do you do ? " , end=" ")
# job = input()


# print(f"system do you like {name}")
# likes = input(">")


# print(f"system do you like {name}'s Job")
# likes_job = input(">")



# print(f"""
# so system you said {likes} to me 
# and i asked you about my job  that you like it or not you said {likes_job}

# """)

# File Handling 

# import os
# doc_path =  os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(doc_path, "doc.txt")

# with open(file_path, "r") as file:
#     content = file.read()
#     print("Reading file content:")
#     print(content)
 



# with open(file_path, 'w') as file:
#     file.write("hello this is now a new file ")


# with open(file_path, 'a') as file:
#     file.write("\nhello this an appended text you are seeing.")
#     file.close()




# Functions


# def print_user_details(*details):
    
#     name , work, age =  details 
#     print(f"Hello {name} Oh so your a {work} and your age is {age}")





# print_user_details("Muhammad Subhan", "Software Engineer", 23)

# name = ""
# age=""
# work=""


# def get_user_details():
#     global name, age,work
 

#     name = input("Enter your name " )
#     age = input("Enter your age ")
#     work = input("Enter your work " )
    
    


# def print_values():
#     print(f"your name is {name} and your age is {age} and you are a {work}")
    
    
    
    
# get_user_details()
# print_values()




# import os

# dir_name = os.path.dirname(os.path.abspath(__file__))
# persistent_path = os.path.join(dir_name, "doc.txt")

# print(persistent_path)

# def read_file():
    
#     with open(persistent_path, "r") as file:
#        content  = file.read()
       
#        print(content)
       
       
# def write_file():
#     with open(persistent_path, "a") as file:
#         file.write("New line of code with functions")   
       
       
       
       
    
       
       
# read_file()
# write_file()


# Functions can return something 



# def sum_of_nums(a , b):
    
#     print(f"Adding {a} + {b}")
    
#     return a + b




# sum_is = sum_of_nums(20, 10)

# print(sum_is)



# def break_words():
    
#     words = "hello guys how are you ?".split(" ")
#     return words


# words_break = break_words()


# print(words_break)


# words = "hello guys how are you ? are you fine ?"

# def sort_words():
#     return sorted(words)



# words_sorted = sort_words()

# print(words_sorted)