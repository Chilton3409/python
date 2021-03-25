#!/usr/bin/env python3
def create_python_script(filename):
    comments = "#!/usr/bin/env python3"
    
    with open(filename, "w") as file:
        filesize = file.write(comments)
        
        return(filesize)

print(create_python_script("program.py"))
