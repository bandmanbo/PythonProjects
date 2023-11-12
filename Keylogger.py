#Goals: reading key strokes that write to a txt file.
#File handling - how to read, write and append to a file.   

#first parameter in open is to (create the) name the file we are writing to
#seceond parameter in open is 'mode' which determines how the code will interact with the file
#r - reading 
#w - writing 
#a - appending

f = open("log.txt", "a")
#filedata = f.read()
#print(filedata)
f.write("\n We be gettin that wizard bread fasho \n")
f.close


#first we create a variable named 'f' for our open function. set the parameters. 
#then we tell our variable 'f' to to either read or write 'log.txt'
#\n to append text to a new line.