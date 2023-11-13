#listeners - Listens to keystrokes
#The 'with' keyword releases memory/resources automatically

with open("log.txt", "a") as f:
    f.write("\n We be gettin that wizard bread fasho")


#the 'with' keyword is used to replace these three lines of code from the previous commit
#'with' automatically closes out the resoources right after processing them.
#'as' keyword is used to create an alias for the 'with' statement
