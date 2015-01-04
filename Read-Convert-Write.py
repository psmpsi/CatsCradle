#added: code to write the string, exactly as read, to a different file (remember mode = a for append):
#added: a loop to iterate the readline command until end of file
    #for line in infile:  uses file iterators to step through lines in a file
#end of first project - complete 20141230.
#next projects:
    #adding: code to replace the comma delimiters with another delimiter, then write the modified string to a different file.
    #add: call to import the CSV module, -or- modules for string manipulation.
    #add: ask user for the input file and output file paths (or read them from a config file)
    #add: code to search for the data header line in the real data file, which has dozens of lines of info before the data starts, and not start readline until the header is found.
    #add: code to search for the first data line in the real data file (next line after data header).
    #add: logic to parse the header line and repeating data lines to "understand" it - read data elements into variables - to re-order or otherwise mainpulate the strings.
        #approach: use dict, which establishes data tables?
        #then write the re-ordered data line to a different file.
outfile = open('C:\MyDocs\GitHub\CatsCradle\Out.txt', 'a')

with open('C:\MyDocs\GitHub\CatsCradle\in.txt', 'r') as infile:
    for line in infile:
        myline = line
        myline.replace(",", "><")   # the replace method is not working
        print(myline)               # this command only executes once; the loop is not looping
        outfile.write(myline)       # this command only executes once; the loop is not looping