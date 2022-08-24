import os

def help_(cmd,cmd_list):
    if len(cmd) == 2 & cmd[1] in cmd_list:
            if cmd[1] == "quit":
                print("Syntax: quit")
                print("Description: exits the directory, quits if it is vocab")
            elif cmd[1] == "ls":
                print("Syntax: ls")
                print("Description: lists files and folders in current directory")

def ls_(directory):
    print("")
    files = open("/home/emilyblack/john_misc/" + directory + "/files.txt","r").read()
    if len(files) > 0:
        print(files)
    else:
        print("There are no files here :(")

def quit_(directory, quit,file_primed):
    if file_primed:
        file_primed = False
    elif directory == "vocab":
        quit = True
    else:
        directory = directory.split("/")
        directory.pop()
        directory = "/".join(directory)
    return(directory,quit,file_primed)

def open_(cmd,directory,file,file_primed):
    files = open("/home/emilyblack/john_misc/" + directory + "/files.txt").read().split("\n")
    if cmd[1] in files:
        if not cmd[1].endswith(".vcb"):
            directory += "/" + cmd[1]
        else:
            file = cmd[1]
            file_primed = True
    return(directory,file,file_primed)

def make_new_(cmd,directory):
    print("")
    if cmd[1] == "f":
        os.mkdir("/home/emilyblack/john_misc/" + directory + "/" + cmd[2])
        open("/home/emilyblack/john_misc/" + directory + "/" + cmd[2] + "/files.txt","w")
        file = open("/home/emilyblack/john_misc/" + directory + "/files.txt","a")
        file.write("\n" + cmd[2])
        file.close()
        print("Made new folder " + cmd[2])
    elif cmd[1] == "v":
        open("/home/emilyblack/john_misc/" + directory + "/" + cmd[2] + ".vcb","w")
        file = open("/home/emilyblack/john_misc/" + directory + "/files.txt","a")
        file_r = open("/home/emilyblack/john_misc/" + directory + "/files.txt","r").read()
        if file_r == "":
            file.write(cmd[2] + ".vcb")
        else:
            file.write("\n" + cmd[2] + ".vcb")
        file.close()
        print("Made new vocab file")
    else:
        print("Error: can only use f and v file types")

def add(directory,file,cmd):
    f = open("/home/emilyblack/john_misc/" + directory + "/" + file,"a")
    f.write(" ".join(cmd[1:]))
    f.close()

def find_cmd(cmd,directory,quit,file,file_primed):
    if not file_primed:
        cmd_list = sorted(["quit","ls","open","help","new"])
        if cmd[0] in cmd_list or cmd[0] == "":
            if cmd[0] == "help":
                if len(cmd) == 1:
                    print("")
                    print("\n".join(cmd_list))
                else:
                    help_(cmd,cmd_list)
            elif cmd[0] == "open":
                directory,file,file_primed = open_(cmd,directory,file,file_primed)
            elif cmd[0] == "ls":
                ls_(directory)
            elif cmd[0] == "new":
                make_new_(cmd,directory)
            elif cmd[0] == "quit":
                directory,quit,file_primed = quit_(directory, quit,file_primed)
        else:
            print("\nError: " + cmd[0] + " unknown command.\nUse help to find a list of commands\n")
    else:
        cmd_list = sorted(["quit","edit","help","translate","add","delete","ls"])
        if cmd in cmd_list or cmd[0] == "":
            if cmd[0] == "quit":
                directory,quit,file_primed = quit_(directory, quit,file_primed)
            elif cmd[0] == "help":
                if len(cmd) == 1:
                    print("")
                    print("\n".join(cmd_list))
            elif cmd[0] == "edit":
                edit(directory,file,cmd)
            elif cmd[0] == "translate":
                translate(directory,file,cmd)
            elif cmd[0] == "add":
                add(directory,file,cmd)
            elif cmd[0] == "delete":
                delete(directory,file,cmd)
            elif cmd[0] == "ls":
                file_ls(directory,file,cmd)
    return(file,directory,quit,file_primed)

quit = False
directory = "vocab"
file_primed = False
file = ""
while not quit:
    if file_primed:
        cmd = raw_input(directory + "/" + file + " >>> ").split(" ")
    else:
        cmd = raw_input(directory + " >>> ").split(" ")

    file,directory,quit,file_primed = find_cmd(cmd, directory, quit,file, file_primed)
    print("")