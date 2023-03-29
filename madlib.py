name_1 = input("Please give a name: ")
name_2 = input("Please give a second name: ")
verb_1 = input("Please give a verb: ")
verb_2 = input("Please give a second verb: ")
verb_3 = input("Please give a third verb: ")
noun_1 = input("Please give a noun: ")
noun_2 = input("Please give a second noun: ")
noun_3 = input("Please give a third noun: ")
adjective_1 = input("Please give a adjective: ")
adjective_2 = input("Please give a second adjective: ")

mad_lib = f"""\n{adjective_1} {noun_1} {name_1} was a teenager when she discovered something that changed her life forever: she was a descendant of {name_2}, a woman {verb_1} for witchcraft during the Salem Witch Trials of 1692. 
At 24, after scouring archives, reading {adjective_2} texts, and {verb_2} hundreds of pages of {noun_2} on witch hunts, {name_1} is ready to share her findings in a {noun_3}. 
But before finishing the story, she has some last strings to {verb_3}, which leads her to revisit the last days of {name_2} in Salem and to reckon with the fact that for millions around the world, Salem is not over. \n"""


print(mad_lib)