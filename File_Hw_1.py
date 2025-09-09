file_0 = "file0.txt" # original names
file_1 = "file1.txt" # reversed names
file_2 = "file2.txt" # re-reversed names

#read files 1 char at a time and print
def read_file_byChar():
    File_to_find = input("Enter the name of the file to read text from:   ")
    with open(File_to_find,"r") as file:
        while True:
                c = file.read(1)
                print(c,end="")   
                if not c:
                    break     
    file.close()  

#gets names from user input,adds to list & prints each  name reversed
def get_names():
    names_list = []
    getting = True
    while (getting):  
        name = input("Type names or click e to exit!").strip()
        if name.lower() == "e":
            getting = False
        else:
            print("".join(reversed(name)))
            names_list.append(name)       
    return names_list
#write normal names from user input into file 0
def Write_names():
    names=get_names()
    with open(file_0,"w") as file:
        for name in names:
                file.write(name + "\n")
    print("\n Names written to", file_0, "\n")  
    file.close()


def readChar(file_name):
    chars = []
    with open(file_name,"r") as file:
            for name in file:
                for char in name:
                    chars.append(char)
    file.close()  
    return chars

#uses stack/ppop to reverse names
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

#reverse names & write into file 1
def write_reverse_names():
    names = reverse_names(file_0)   
    with open(file_1, "w") as file1:
        for name in names:
            file1.write(name + "\n")
    file1.close()    
    print(" Reversed names written to", file_1,"\n")

#reverse from file1 and write into file2
def write_re_reverse():
    names = reverse_names(file_1)
    with open(file_2, "w") as file2:
        for name in names:
            file2.write(name + "\n")
    file2.close()      
    print(" Re-reversed names written to", file_2,"\n")

#read file 2 and print sorted ordeer of names
def reverse_sort():
    names = reverse_names(file_2)
    names.sort()
    print("\n---reversed & Sorted--- ")
    for name in names:
        print("   ",name)

# read_file_byChar()
# Write_names()
write_reverse_names()
write_re_reverse()
reverse_sort()




#question 3 = 21??
# 25000*256 = 6,400,000
# 512*50*12 = 307,200
# 6,400,000/307,200=20.8->21