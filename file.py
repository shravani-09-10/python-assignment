try:
    file= open('my_file.txt','r')
    lines=file.readlines()
    print("Reading file contents:")
    print("line 1:", lines[0])
    print("line 2:",lines[1])
    file.close()
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found")