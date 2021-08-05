"""
File handling:
--------------
To store the data permanently and if our data is very small.

Very small amount of information is there like 100 students mobile numbers
then it can be handled by the Files concept.

If I want to store huge data like the icici customer transactions info then
we can handle it with the database concept

If very very huge data like videos, fb posts, tweets, etc. then we'll us the
big data or hadoop concept.

Dictionary is a type of temporary data storing concept. Dictionary is mutable.


What is the need of file concept?
- To store the data permanently.

How many types of files are there?
- Normal text files : To store character data eg: abc.txt
- Binary files : To store binary data eg images, videos, audio files, zip files, etc.

> If you want to perform any operation on a file then first step is to open the file.
> Then after the operation on the file, you need to close the file.
> To open the file there is an inbuilt function, f=open(filename, mode) eg. f = open('abc.txt','r')
  if the file is present at any other location then specify the location of the file
> Mode defines the operations like read, write, etc.
> like 'r' for read and 'w' for write
> The allowed values for mode are:-
  r, w, a, r+, w+, a+, x
  These are the allowed operations.
  r - read, w - write, a - append,
  r+ - read and write
  w+ - write and read
  a+ - append and read
  x - exclusive mode

READ OPERATION ('r'):-
- Open an existing file for read operation.
  f = open('abc.txt') # This will read only if we do not specify the mode
                      # So, read is the default mode

  If the specified file is not found - Then FileNotFoundError will occur

WRITE OPERATION ('w'):-
- open an existing file for  write operation
  f = open('abc.txt','w')
  if file available but contains some data.....then the already existing data
  will be overwrite....or the data will be gone.
  If the file is not available...then the required file will be created automatically
  no error will occur.

APPEND OPERATION ('a'):-
- f=open('abc.txt', 'a')
- If the specify file contains the data previously.. then no overwrite of the data
  if the specify file is not available then the file will be created automatically.
  So, no loss of data in append mode.



"""