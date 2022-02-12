#!/usr/bin/env python3
def create_python_script(filename):
    shebang = "#!/usr/bin/env python3"
    
    with open(filename, "w") as file:
        filesize = file.write(shebang)
        file.write("\n#new file created")
        
        return(filesize)

print(create_python_script("program.py"))
