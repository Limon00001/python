# ----------------------------------------- Reading a file by python ------------------------------------------------


file = open("14th.txt","r+")                    # for opening, open("txt_file","readable or writable files mode")
# -> for read operation, "r"
# -> for write operation, "w"                   -> will overwrite any existing content
# -> for read & write operation, "r+"
# -> for append operation, "a"                  -> will append to the end of the file
# -> to create new file, "x"                    -> will create a file, returns an error if the file exist

# If the file is located in a different location, you will have to specify the file path, like this:
# -> open("D:\\myfiles\file_name.txt", "operation_mode")

# print(file.readable())                         # check if it is readable
# print(file.writable())                         # check if it is writable

# reading from a txt file
text = file.read()
print(text)

# checking the length
length = len(text)
print(length)

# to show files as list
files = file.readlines()
print(files)

# using readlines, '\n' appears. To remove '\n' use -> strip()
# Strip removes the leading and trailing characters like:
strip_file = ",,,,,rrttgg.....That's fine now....rrr"
garbage_ch = strip_file.strip(",.grt")                                   # Syntax -> "string.strip(characters)"
                                                                         # Here, which characters want to be removed.
print(garbage_ch)

# Strip removes spaces at the beginning and at the end of the string
txt = "     Hello.     "
r = txt.strip()

print(r, "Nice to meet you.")

# using loop, can see the whole file
for x in file:
    print(x)

# close the file
file.close()
