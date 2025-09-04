file_name="names_input.txt" 
file_name_1 = "file1.txt"
file_name_2="file2.txt"

def get_name_input():
    names_list = []
    getting = True
    while (getting):  
        names = input("please enter numbers or enter d to exit!").strip()
        if names.lower() == "d":
            getting = False
        else: 
            names_list.append(names)
    return names_list
 
def Write_names():
    names=get_name_input()
    if names:
        with open(file_name,"w") as file:
            for name in names:
                file.write(name + "\n")
        for name in names:
            print(name)
        print("Names written to", file_name)  
    else:
        print("Error, no names")

def readChar(file_name):
    chars = []
    with open(file_name,"r") as file:
            for name in file:
                for char in name:
                    chars.append(char)
    return chars

def reverse_names(file_name):
    char_list = readChar(file_name)
    names = []
    name = ""
    for char in char_list:
        if char == '\n':
            if name:
                stack = list(name)
                reverse = ""
                while stack:
                    reverse += stack.pop()
                names.append(reverse)
                name = "" 
        else:
            name += char
    return names

def write_reverse_names():
    names = reverse_names(file_name)   
    with open(file_name_1, "w") as file:
        for name in names:
            print(name)
            file.write(name + "\n")
    print("Reversed names printed & written to", file_name_1)

def re_reverse():
    names = reverse_names(file_name_1)
    with open(file_name_2, "w") as file:
        for name in names:
            file.write(name + "\n")
    print("Re-reversed names written to", file_name_2)

def reverse_sort():
    names = reverse_names(file_name_2)
    names.sort()
    print("\n -reversed_Sorted Names- ")
    for name in names:
        print(name)

def Read_all_files():
    print("\n -Original- ")
    with open(file_name, "r") as file:
        print(file.read())

    print("\n -Reversed- ")
    with open(file_name_1, "r") as file:
        print(file.read()) 

    print("\n -Re-Reversed- ")
    with open(file_name_2, "r") as file:
        print(file.read())   

Write_names()
write_reverse_names()
re_reverse()
Read_all_files()
reverse_sort()
