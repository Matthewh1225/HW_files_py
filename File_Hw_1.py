file_0 = "file0.txt" # original names
file_1 = "file1.txt" # reversed names
file_2 = "file2.txt" # restored names

def read_file_byChar(file_name = None):
    #reads 1 char at a time and prints to console
    if file_name is None:
        File_to_Read = input("Enter the name of the file to read text from:   ")
        with open(File_to_Read,"r") as file:
            while True:
                    c = file.read(1)
                    print(c,end="")   
                    if not c:
                        break    
        file.close()
    # returns list of chars from file
    if file_name is not None:
        chars = []
        with open(file_name,"r") as file:
                for name in file:
                    for char in name:
                        chars.append(char)
        file.close()  
        return chars   

#gets names from user input,adds name to list & prints each name reversed
def get_names():
    names_list = []
    getting = True
    while (getting):  
        name = input("\nType names or click e to exit!").strip()
        if name.lower() == "e":
            getting = False
        else:
            print("".join(reversed(name)))
            names_list.append(name)       
    return names_list

#uses stack/ppop to reverse names
def reverse_names(file_name):
    char_list = read_file_byChar(file_name)
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

def Assignment(): 
    read_file_byChar()#read file char by char & print to console

    #write normal names to file_0
    Original_names=get_names()
    with open(file_0,"w") as file0:
        for name in Original_names:
                file0.write(name + "\n")
    print("\n Names written to", file_0, "\n")  
    file0.close()

    #read from File 0 & write reverse names into file_1
    rev_names = reverse_names(file_0)   
    with open(file_1, "w") as file1:
        for name in rev_names:
            file1.write(name + "\n")
    file1.close()    
    print(" Reversed names written to", file_1,"\n")

    #read from File 1 & write restored names into file_2
    restore_names = reverse_names(file_1)
    with open(file_2, "w") as file2:
        for name in restore_names:
            file2.write(name + "\n")
    file2.close()      
    print(" Restored names written to", file_2,"\n")

    #read from file_2, reverse, sort & print names
    names = reverse_names(file_2)
    names.sort()
    print("\n---reversed & Sorted--- ")
    for name in names:
        print("   ",name)
