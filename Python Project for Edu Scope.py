import sys  # Import sys to exit the program

# User authentication
email = input("ENTER THE USER NAME: ")
passw = input("ENTER THE PASS CODE: ")

if email == "@" and passw == "123":
    print("YOU HAVE SUCCESSFULLY LOGGED IN...\n")
else:
    print("ENTER THE CORRECT MAIL ID AND PASSWORD...")
    sys.exit()  # Stop further execution



print(" Welcome to our Python Notes...\n All the notes are taken by Chandru Annan...")
def check():
    check_op = int(input("ENTER THE VALUES TO CHECK THE NOTES RESPECTIVELY : \n 1,BASIC NOTES...\n 2,ADVANCE NOTES...\n 3,CLASS AND OBJECTS...\n ENTER HEAR : "))
    if check_op == 1:
        print("THANK YOU FOR ENTERING IN TO BASIC NOTES : ")
        bas = int(input("IN BASICS OF PYTHON THERE ARE MAINLY : \n 1,Standared Data types in Python \n 2,Sequence"
                        "\n 3,Boolean \n 4,Mapping \n 5,Set \n  6,BASIC OF ADDITION \n 7, Type Casting \n 8,User Input()  \n 9,Operators ENTER THE SERIAL NO HEAR TO VIEW THE NOTES : "))
        if bas == 1:
            print("THERE ARE THREE STANDARD DATA TYPE IN PYTHON WHICH ARE GIVEN BELOW : ")
            print(
                "1. NUMERIC  : In Python, a numeric data type is used to store numerical values. There are three main types of numeric data in Python:"
                "\n for ex :a=10 b=20 these are in Integer values ")
            print(
                "2. FLOAT : In Python, the float data type is used to represent real numbers (numbers that contain a decimal point). It supports both positive and negative numbers and can also be written in scientific notation."
                "\n for ex : a=10.3 b=5.6 These are in Float values")
            print(
                "3. COMPLEX : In Python, the complex data type is used to represent complex numbers, which consist of a real part and an imaginary part. The imaginary part is represented using j (instead of i, as used in mathematics)"
                "\n for ex : z = 3 + 4j hear  3 is the real part, 4j is the imaginary part")
        if bas == 2:
            print("IN SEQUENCE THERE ARE 3 TYPE OF DATA TYPE WHICH ARE GIVEN BELOW : ")
            print(
                "1. LIST[] : A list in Python is a mutable, ordered collection that allows storing multiple items in a single variable. Lists can hold different data types, including integers, floats, strings, and even other lists."
                "\n For ex : list = [1, hello, 3.14, True]")
            print(
                "2. TUPLE() : A tuple in Python is an ordered, immutable collection used to store multiple items in a single variable. Unlike lists, tuples cannot be modified after creation."
                "\n for ex : mixed_tuple = (1,hello, 3.14, True")
            print(
                "3.Dictionary{} : A dictionary in Python is an unordered, mutable collection used to store key-value pairs. Each key in a dictionary is unique, and values can be of any data type."
                "\n for ex : dict={name : kaif,age : 20,college: The new college}")
        if bas == 3:
            print("1. BOOLEAN : There are two typpe of Boolen Condition given below : \n True \n False")
        if bas == 4:
            print(
                "1. MAPPING : In Python, mapping refers to a data structure that stores key-value pairs, where each key maps to a specific value. The most common mapping type in Python is the dictionary (dict)."
                "\n for ex : dict={name : kaif,age : 20,college: The new college}")
        if bas == 5:
            print(
                "1.SE{} :  set in Python is an unordered, mutable collection of unique elements. Sets do not allow duplicate values and are commonly used for membership testing and removing duplicates from a list."
                "\n for ex : my_set = {1, 2, 3, 4, 5} ")
        if bas == 6:
            print("a=10\nb=20\nc=a+b\n Output : 30")

            def add():
                a = 10
                b = 20
                c = a + b

            add()
        if bas == 7:
            print("THIS IS TYPE CASTING SESION : \n Type Casing is the ethod which use to Convert one DataType in to "
                  "Other DataType is Known as TypeCasting...")
            print("a=10\nb=char(a)\nprint(type(b))")

            def type_cast():
                a = 10
                b = chr(a)
                print(type(b))

            type_cast()
        if bas == 8:
            print("YOU ARE IN THE USER INPUT SESSION : ")
            print("a=input(Enter The Value Hear : )\n b=input(Enter the b value Hear : )")

            def inp():
                a = input("ENTER YOUR NAME : ")
                b = int(input("ENTER YOUR AGE : "))
                print(f"YOUR NAE IS : {a}")
                print(f"YOUR AGE IS : {b}")

            inp()
        if bas == 9:
            print("NOW WE ARE MOVING UPON TO THE OPERATORS : ")
            print("There are mainly 7 Types of operator which are given below : ")
            op = int(input("1.ARITHMETIC OPERATOR\n2.ASSIGNMENT OPERATOR\n3.COMPARISON OPERATOR\n4.LOGICAL OPERATOR"
                           "\n5.IDENTIFY OPERATOR\n6.MEMBERSHIP OPERATOR\n7.BITWISE OPERATOR\nENTER THE SERIAL NO HEAR : "))


            if op == 1:
                print("YEAH YOU HAD ENTERED TO THE ARITHMETIC OPERATOR : ")
                print(
                    "Arithmetic operators are used to perform mathematical operations in Python. Here are the six main arithmetic operators with examples:")
                print("Addtion==>a+b=c==>10+20==30\n Subraction==>a-b=c==>30-20=10\n Multiplication==>a*b=c==>2*5=10"
                      "\n Division==>a/b=c==>10/2=5.0\n Module==>a//b==>10//2=5\n Exponential==>a**b=c==>2**2=4 ")
            if op == 2:
                print("YEAH YOU HAD ENTERED TO THE ASSIGNMENT OPERATOR : ")
                print(
                    "An assignment operator is used to assign values to variables.\n a=10 , b=hello hai good morning ")
            if op == 3:
                print("YEAH YOU HAD ENTERED IN TO THE COMPARISON OPERATOR : ")
                print(
                    "Comparison operators are used to compare two values. They return True or False based on the condition.")
                print("if a=10 and b=20 \n a==b->False\na!=b->True\na>b->False\na<b->True\na>=b->False\na<=b->True")
            if op == 4:
                print("YEAH YOU HAD ENTERED IN TO THE LOGICAL OPERATOR : ")
                print(
                    "Logical operators are used to combine multiple conditions and return True or False based on the logic.")
                print("AND==>a and b\n OR==>a or b\nNOT==>a not b")
            if op == 5:
                print("YEAH YOU HAD ENTERED IN TO THE IDENTIFY OPERATOR : ")
                print("Identity operators are used to compare the memory location of two objects.")
                print("is==> a is b\n isnot==> a is not b")
            if op == 6:
                print("YEAH YOU HAD ENTERED IN TO THE MEMBERSHIP OPERATOR : ")
                print(
                    "Membership operators are used to check if a value is present in a sequence (like a list, tuple, string, or dictionary).")
                print("in==>a in b\n not in ==> a not in b")


    elif check_op == 2:
        print("THANK YOU FOR ENTERING IN TO ADVANCE NOTES : ")
    adv = int(input("IN ADVANCE OF PYTHON THERE ARE MAINLY : 1,STRING OPERATIONS...\n2,INDEXING...\n3,STRING METHODS.\n4,FORMATE\n5,CONTROL FLOW.\n6.LIST IN PYTHON"
                    "\n7.TUPLE\n8.DICTIONARY\n ENTER THE S.NO TO CHECK THE NOTES : "))
    if adv == 1:
        print("OK YOU HAD ENTERED ON THE STRING OPERATIONS  IN PYTHON : ")
        print("It is a sequencof character which is enclosed with single or double quotes \n it is immutable because it is un changeable...")
        print("There are some Functions in String Operation : \n*print(a.capitalize())\n*print(a.upper())"
              "\n*print(a.lower())\n*print(a.case fold)\n*print(a.swapcase())")
        text = str(input("ENTER YOUR NAME TO CHECK THE STRING OPERATIONS :"))
        print(text.upper())  # Output: HELLO WORLD
        print(text.lower())  # Output: hello world
        print(text.capitalize())  # Output: Hello world
        print(text.title())  # Output: Hello World
    if adv==2:
        print("YOU HAD ENTERED TO THE INDEXING METHOD IN STRING OPERATION...")
        print("It is a Process of  accessing the specfic element in the sequence...\n Here The Negative index start with(-1)==>From the right side\n"
              "and in the positive Index start with(0)==>It start from the left side")
        print("a=Hello World\n print(a[1]==>The output will be e\nprint(a[-4])==>The output will be e")
        print("a=hello\nprint(a.index[0])==>The output will be==>4")
    if adv==3:
        print("YOU HAD ENTERED TO THE STRING METHODS...")
        print("There are some Methods in String Operation : \n*print(a.title())\n*print(a.find())"
              "\n*print(a.count())\n*print(a.startswith())\n*print(a.endswith())")
        text = str(input("ENTER THE TEXT TO CHECK THE STRING METHODS : "))
        print("Title Case:", text.title())
        print("Find 'World':", text.find("World"))
        print("Count of 'l':", text.count("l"))
        print("Starts with 'Hello':", text.startswith("Hello"))
        print("Ends with 'World':", text.endswith("World"))
    if adv==4:
        print("YOU HAD ENTERED TO FORMATE FUNCTION : ")
        print("It is the process of inserting the pre define text")
        print("WATCH THE SYNTAX : \nname=Kaif\nage=20\nprint(My Name is {} and my Age is {}.formate(a,b)")
        name="Kaif"
        age=20
        print("MY NAME IS {} AND MY AGE IS {}".format(name, age))
    if adv==5:
        print("YOU HAD ENTERED TO THE CONTROL FLOW ...")

        op = int(input("IN THE CONTROL FLOW IT CONTAIN MAINLY TWO TYPE OF STATEMENT IN IT :\n1,CONTROL STATEMENT\n2,ITERATIVE STATEMENT"
                       "\n ENTER THE SERIAL NUMBER TO CHECK THE UPGIVEN STAEMENTS : "))

        if op == 1:
            print("""YOU HAVE ENTERED THE CONTROL STATEMENT SECTION:

            In the control statement, there are:
            * if Statement
            * if-else Statement
            * if-elif-else Statement
            * Nested if Statement

            -------------------------------------------------------------------------------

            The if statement in Python is used for conditional execution of code. 
            Here's the basic syntax:

            if condition:
                # Code will be executed here...

            -------------------------------------------------------------------------------

            The if-else statement in Python allows you to execute different blocks of code 
            depending on whether a condition is True or False.

            if condition:
                # Code will be executed here...
            else:
                # Code will be executed here...

            -------------------------------------------------------------------------------

            The if-elif-else statement allows multiple conditions to be checked in sequence.

            if condition:
                # Code will be executed here...
            elif condition:
                # Code will be executed here...
            elif condition:
                # Code will be executed here...
            else:
                # Code will be executed here...

            -------------------------------------------------------------------------------

            A nested if statement is an if statement inside another if statement. 
            It allows multiple levels of condition checking.

            if condition:
                # Code will be executed here...
                if condition:
                    # Code will be executed here...
                    if condition:
                        # Code will be executed here...
                        if condition:
                            # Code will be executed here...
            else:
                # Code will be executed here...

            -------------------------------------------------------------------------------
            """)
        if op==2:
            print("YOU HAD ENTERED TO THE ITERATIVE STATEMENT : ")
            print("""YOU HAVE ENTERED THE ITERATIVE STATEMENT (LOOPING) SECTION:

            In Python, there are two types of loops:
            * for Loop
            * while Loop

            -------------------------------------------------------------------------------

            The for loop in Python is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). 
            It has the following syntax:

            for variable in sequence:
                # Code will be executed for each item in the sequence

            Example:

            for i in range(5):
                print(i)  # Prints numbers from 0 to 4

            -------------------------------------------------------------------------------

            The while loop in Python runs a block of code as long as a condition is True.
            It has the following syntax:

            while condition:
                # Code will be executed while the condition is True

            Example:

            count = 0
            while count < 5:
                print(count)
                count += 1  # Increments count to avoid infinite loop

            -------------------------------------------------------------------------------

            Nested loops are loops inside another loop. They allow complex iterations.

            Example:

            for i in range(3):
                for j in range(2):
                    print(f"i={i}, j={j}")  # Prints combination of i and j values

            -------------------------------------------------------------------------------

            Loop Control Statements:
            Python provides special statements to control loops:
            * break - Exits the loop completely
            * continue - Skips the current iteration and moves to the next
            * pass - Does nothing, used as a placeholder

            Examples:

            # Using break
            for i in range(5):
                if i == 3:
                    break
                print(i)  # Stops at 2

            # Using continue
            for i in range(5):
                if i == 3:
                    continue
                print(i)  # Skips 3 but continues the loop

            -------------------------------------------------------------------------------
            """)
    if adv==6:
        print("YOU HAD ENTER TO THE LIST IN PYTHON : ")
        print("""
        LIST IN PYTHON:
        ----------------------------
        - A list in Python is a mutable, ordered collection that allows storing multiple items in a single variable.
        - Lists can hold different data types, including integers, floats, strings, and even other lists.

        CREATING A LIST:
        ----------------------------
        my_list = [1, 2, 3, 4, 5]
        print(my_list)  # Output: [1, 2, 3, 4, 5]

        ACCESSING ELEMENTS:
        ----------------------------
        - You can access elements using their index.
        - Indexing starts from 0.

        Example:
        numbers = [10, 20, 30, 40]
        print(numbers[0])  # Output: 10
        print(numbers[-1])  # Output: 40 (last element)

        LIST METHODS:
        ----------------------------
        - append(): Adds an item to the end of the list.
        - insert(): Inserts an item at a specified position.
        - remove(): Removes a specific element.
        - pop(): Removes the last element or a specific index.
        - sort(): Sorts the list in ascending order.
        - reverse(): Reverses the list.

        Example:
        fruits = ["apple", "banana", "cherry"]
        fruits.append("orange")
        print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

        ITERATING THROUGH A LIST:
        ----------------------------
        - You can loop through a list using a for loop.

        Example:
        for fruit in fruits:
            print(fruit)

        LIST COMPREHENSION:
        ----------------------------
        - A short way to create lists.

        Example:
        squares = [x**2 for x in range(1, 6)]
        print(squares)  # Output: [1, 4, 9, 16, 25]

        NESTED LISTS:
        ----------------------------
        - A list inside another list.

        Example:
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(matrix[1][2])  # Output: 6 (Second row, third column)

        """)
    if adv==7:
        print("YOU HAD ENTERED IN TO TUPLE : ")
        print("""
        TUPLE IN PYTHON:
        ----------------------------
        - A tuple is an **ordered**, **immutable** collection used to store multiple items in a single variable.
        - Unlike lists, tuples **cannot be modified** after creation.
        - Tuples can contain different data types, including integers, strings, and even other tuples.

        CREATING A TUPLE:
        ----------------------------
        my_tuple = (1, 2, 3, 4, 5)
        print(my_tuple)  # Output: (1, 2, 3, 4, 5)

        SINGLE ELEMENT TUPLE:
        ----------------------------
        - A single-element tuple must have a **comma** at the end.

        Example:
        single_tuple = (10,)  
        print(type(single_tuple))  # Output: <class 'tuple'>

        ACCESSING ELEMENTS:
        ----------------------------
        - You can access elements using **indexing**.
        - Indexing starts from **0**.

        Example:
        numbers = (10, 20, 30, 40)
        print(numbers[0])  # Output: 10
        print(numbers[-1])  # Output: 40 (last element)

        TUPLE UNPACKING:
        ----------------------------
        - Tuple unpacking allows assigning multiple values at once.

        Example:
        person = ("John", 25, "Engineer")
        name, age, job = person
        print(name)  # Output: John
        print(age)   # Output: 25
        print(job)   # Output: Engineer

        IMMUTABILITY:
        ----------------------------
        - Tuples **cannot** be changed after creation.
        - The following code will cause an error:

        Example:
        my_tuple = (1, 2, 3)
        # my_tuple[0] = 10  ❌ ERROR: TypeError: 'tuple' object does not support item assignment

        TUPLE METHODS:
        ----------------------------
        - count(): Returns the number of times a value appears.
        - index(): Returns the first index of a value.

        Example:
        numbers = (1, 2, 3, 2, 2, 4)
        print(numbers.count(2))  # Output: 3
        print(numbers.index(3))  # Output: 2

        NESTED TUPLES:
        ----------------------------
        - Tuples can contain other tuples.

        Example:
        nested_tuple = ((1, 2, 3), (4, 5, 6))
        print(nested_tuple[1][2])  # Output: 6 (Second tuple, third element)

        CONVERTING LIST TO TUPLE:
        ----------------------------
        - You can convert a list into a tuple using **tuple()**.

        Example:
        my_list = [10, 20, 30]
        my_tuple = tuple(my_list)
        print(my_tuple)  # Output: (10, 20, 30)

        WHEN TO USE TUPLES?
        ----------------------------
        ✔ When data should **not be modified** (e.g., coordinates, database records).
        ✔ Tuples are **faster** than lists in terms of access speed.
        ✔ They use **less memory** compared to lists.

        """)
    if adv==8:
        print("""
        DICTIONARY IN PYTHON:
        ----------------------------
        - A **dictionary** is an **unordered**, **mutable** collection used to store data in **key-value pairs**.
        - Each key in a dictionary is **unique**, and values can be of any data type.
        - Dictionaries are created using **curly braces { }**.

        CREATING A DICTIONARY:
        ----------------------------
        my_dict = {
            "name": "Alice",
            "age": 25,
            "city": "New York"
        }
        print(my_dict)  
        # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

        ACCESSING VALUES:
        ----------------------------
        - You can access values using their **keys**.

        Example:
        print(my_dict["name"])  # Output: Alice
        print(my_dict["age"])   # Output: 25

        - Using **get()** method (prevents errors if the key is missing).

        Example:
        print(my_dict.get("city"))  # Output: New York
        print(my_dict.get("country", "Not Found"))  # Output: Not Found

        ADDING & UPDATING VALUES:
        ----------------------------
        - You can **add** or **update** dictionary values.

        Example:
        my_dict["job"] = "Engineer"  # Adding a new key-value pair
        my_dict["age"] = 26  # Updating an existing value
        print(my_dict)  
        # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}

        REMOVING ELEMENTS:
        ----------------------------
        - **pop()**: Removes a specific key.
        - **popitem()**: Removes the last added item.
        - **del**: Deletes a key or the entire dictionary.
        - **clear()**: Removes all items.

        Example:
        my_dict.pop("city")  # Removes 'city' key
        print(my_dict)  
        # Output: {'name': 'Alice', 'age': 26, 'job': 'Engineer'}

        DICTIONARY METHODS:
        ----------------------------
        - **keys()**: Returns all keys.
        - **values()**: Returns all values.
        - **items()**: Returns key-value pairs.

        Example:
        print(my_dict.keys())    # Output: dict_keys(['name', 'age', 'job'])
        print(my_dict.values())  # Output: dict_values(['Alice', 26, 'Engineer'])
        print(my_dict.items())   # Output: dict_items([('name', 'Alice'), ('age', 26), ('job', 'Engineer')])

        LOOPING THROUGH A DICTIONARY:
        ----------------------------
        - You can loop through keys, values, or key-value pairs.

        Example:
        for key in my_dict:
            print(key, ":", my_dict[key])
        # Output:
        # name : Alice
        # age : 26
        # job : Engineer

        NESTED DICTIONARIES:
        ----------------------------
        - A dictionary can contain another dictionary.

        Example:
        students = {
            "student1": {"name": "John", "age": 22, "course": "Math"},
            "student2": {"name": "Emma", "age": 24, "course": "Science"}
        }
        print(students["student1"]["name"])  # Output: John

        CONVERTING LIST TO DICTIONARY:
        ----------------------------
        - Use **dict()** function.

        Example:
        keys = ["name", "age", "city"]
        values = ["Alice", 25, "New York"]
        new_dict = dict(zip(keys, values))
        print(new_dict)
        # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

        WHEN TO USE DICTIONARIES?
        ----------------------------
        ✔ When you need **fast lookups** based on unique keys.  
        ✔ When storing **structured data** (e.g., JSON objects).  
        ✔ When working with **configurations, databases, or API responses**.  
        """)


check()


kai=input("IF ALL OF YOUR WORK DONE PYESS(y) TO EXIT OR PRESS (n) TO BE IN THIS PAGE : ")
if kai=="y":
    check()
else:
    print("NOW WE ARE MOVING TO THE ")





























