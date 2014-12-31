#add: call to import the CSV module, -or- modules for string manipulation.
#enhance the above: code to replace the comma delimiters with another delimiter, then write the modified string to a different file.
#added: code to write the string, exactly as read, to a different file (remember mode = a for append):
	# outfile = open('C:\MyDocs\GitHub\CatsCradle\HoboWxSta-PSItest-Output.txt', 'a')
#added: a loop to iterate the readline command until end of file
	#for line in infile:  uses file iterators to step through lines in a file
#end of first project.
#next project: 
	#enhance: ask user for the input file and output file paths (or read them from a config file)
	#add: code to search for the data header line in the real data file, which has dozens of lines of info before the data starts, and not start readline until the header is found.
	#add: code to search for the first data line in the real data file (next line after data header).
	#add: logic to parse theheader line and repeating data lines to "understand" it - read data elements into variables - to re-order or otherwise mainpulate the strings.
		#approach: use dict, which establishes data tables?
		#then write the re-ordered data line to a different file.
outfile = open('C:\MyDocs\GitHub\CatsCradle\HoboWxSta-PSItest-Output.txt', 'a')
with open('C:\MyDocs\GitHub\CatsCradle\HoboWxSta-PSItest-Input.txt', 'r') as infile:
		# ,r is read; , w is rite; w+ or a for append
		#absolute file path is preferred. same folder OK, but relative is dangerous.
		#with creates a new block, which normally has a colon at the end of the starting line. to end the block.
		# new block requires both colon and indentation.
	for line in infile.readline():
		infile_line = infile.readline()
		#Don't have to declare variables ahead of time; in fact, in Python you never have to.
		#this is "duck-typing" - usually works well, sometimes fails.
		#Python is a run-time language, not compiled.
		#Windows uses CRLF, and Unix uses just LF. Python knows which platform it's on and uses "\n" to add the appropriate line end. 
		print(infile_line)
		#in terminal, type python filename
		#Python has a CSV utility which will be my friend. example:
		outfile.write(infile_line)
#after end of file read / write iterations, close the input and output files
outfile.close()
infile.close()
