# this menu is a three level university system. From different college to master program to program courses.

university = {
    "Business": {
        "Business Management": {
            "Management": 123,
            "Database Analysis": 124,
            "Business Process": 146
        },
        "Business Analytics": {
            "Multivariate Analysis": 234,
            "Network Analysis": 265,
            "Experiement Design": 278
        },
        "MBA": {
            "Optimization Process":345,
            "Financial Analysis": 376,
            "Case Study": 389
        }
    },
    "Engineer": {
        "Chemical Engineer": {
            "Fundamental Chemistry": 456,
            "Chemical Analysis": 435,
            "Experiement Design":498
        },
        "Physical Engineer": {
            "Fundamental Physics": 564,
            "Mechanics": 532,
            "Modern Physics": 587
        },
        "Civil Engineering": {
            "Introduction to Geosciences": 678,
            "Engineering Design": 645,
            "Modeling and Simulation": 625
        }
    },
    "Science": {
        "Computer Science": {
            "Discrete Structures": 789,
            "Data Structure": 736,
            "Algorithms": 745
        },
        "Data Science": {
            "Dissertation Research": 876,
            "Machine Learning": 836,
            "Python": 834
        },
        "Mathematics": {
            "Integral Calculus": 987,
            "Discrete Mathematics": 967,
            "Differential Equations": 973
        }
    },
    "Humanities": {
        "History": {
            "History of Science": 1038,
            "Images of American Life": 1056,
            "Modern Art History and Theory": 1039
        },
        "Art": {
            "Drawing": 1132,
            "Creative Programming": 1156,
            "Introduction To Photography": 1167
        },
        "Music": {
            "Music History": 1276,
            "Piano Class": 1239,
            "Sound Recording": 1263
        }

    }

}

# print all colleges, which are the keys of university
college_list = list(university.keys())
college_list.extend(["Quit"])
print("colleges: ", college_list)

# First layer
flag = True
while flag:
    choice1 = input("Please input your college from the above list: ")
    # chose quit, stop the whole while loop
    if choice1 == "Quit":
        break
    # chose right college, generate corresponding new dictionary (here is majors)
    elif choice1 in university.keys():
        # print all majors in the new dictionary
        majors = university[choice1]
        major_list = list(majors.keys())
        major_list.extend(["Quit", "Go Back"])
        print("Majors: ", major_list)

        # second layer
        flag2 = True
        while flag2:
            choice2 = input("Please input your major from the above list: ")
            # chose quit, stop the whole program
            if choice2 == "Quit":
                flag = False
                break
            # chose go back, then to back to the last layer (here is colleges)
            elif choice2 == "Go Back":
                flag2 = False
            # chose right major, generate corresponding new dictionary (here is courses)
            elif choice2 in majors.keys():
                # print all courses in the new dictionary
                courses = majors[choice2]
                course_list = list(courses.keys())
                course_list.extend(["Quit", "Go Back"])
                print("Courses: ", course_list)

                # third layer
                flag3 = True
                while flag3:
                    choice3 = input("Please input your course from the above list: ")
                    if choice3 == "Quit":
                        flag = False
                        break
                    elif choice3 == "Go Back":
                        flag3 = False
                    # get the value of selected course
                    elif choice3 in courses.keys():
                        print("Course Number: ", courses[choice3])
                        flag2 = False
                        flag = False
                        break
                    # repeat the same question when the answer is not in the list
                    else:
                        flag3 = True
            else:
                flag2 = True
    else:
        flag = True
