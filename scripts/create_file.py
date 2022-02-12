#!/usr/bin/env python3
#this script will take a filename as a system argument and create a python script for you.
#It will then write the shebang line, shortening your time to get started on a new idea.
import os
import sys
filename=sys.argv[1]
shebang = "#!/usr/bin/env python3"
if not os.path.exists(filename):
    with open(filename, "w")as f:
        f.write(shebang)
        f.write("\n#New file created\n") 
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)