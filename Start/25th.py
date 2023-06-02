# ----------------------------------------- Writing a file by python ------------------------------------------------


file = open("15th.txt","x")                     # for opening, open("txt_file","readable or writable files mode")
# -> for read operation, "r"
# -> for write operation, "w"                   -> will overwrite any existing content
# -> for read & write operation, "r+"
# -> for append operation, "a"                  -> will append to the end of the file
# -> to create new file, "x"                    -> will create a file, returns an error if the file exist

# If the file is located in a different location, you will have to specify the file path, like this:
# -> open("D:\\myfiles\file_name.txt", "operation_mode")

# print(file.readable())                         # check if it is readable
# print(file.writable())                         # check if it is writable

# add content in file
file.write("\nThank me later")

# reading from a txt file
text = file.read()
print(text)

file.close()
