import sys
import os
import shutil

def getFiles(param, value):

    files = []
    path = os.listdir()
    if param == '-t':
        for f in path:
            if f.endswith(value):
                files.append(f)
    elif param == '-n':
        for f in path:
            if value in f.lower():
                files.append(f)
    else:
        print ('/!\ "' + param +'" : Unknown command. Type "help" for the list of all commands.')
        sys.exit()

    return files

def rename(files, oldText, newText):

    if newText == 'null': newText = ''
    i = 0
    print('Renaming files, don\'t close.')
    for f in files:
        newName = f.replace(oldText, newText)
        os.rename(os.getcwd()+'/'+f.lower(), os.getcwd()+'/'+newName)
        i = i+1
    print('Successfuly renamed ', i ,' files : "'+oldText+'/'+newText+'".')

    return

def move(files, moveFrom, moveTo):

    i = 0
    if os.path.isdir(moveTo):
        print('Moving files, don\'t close.')
        for f in files:
            #os.rename(moveFrom+"/"+f, moveTo+"/"+f)
            #os.replace(moveFrom+"/"+f, moveTo+"/"+f)
            shutil.move(moveFrom+"/"+f, moveTo+"/"+f)
            i = i+1
        print('Successfuly moved ', i ,' files to : "'+moveTo+'".')
    else:
        print('/!\ Destination path must be a folder.')
        sys.exit()

    return

def help():

    print(' # MOVE FILES\n'+
    '\t move -t|-n fileTypes|Names destination\n'+
    '\t(types: .txt|.pdf|.mp3 ...etc\n\n'+
    ' # RENAME FILES\n'+
    '\t rename -n oldText newText\n'+
    '\t(to delete the text instead: newText = null ')

    return

def prompt(cmd):

    if cmd == [] :
        command = input('> ')
        command = command.lower().split(' ')
    else: command = cmd

    print(command)

    c0 = command[0]
    if c0 == 'help':
        help()
        return
    elif c0 != 'move' and c0 != 'rename':
        print('/!\ "' + c0 +'" : Unknown command. Type "help" for the list of all commands.')
        sys.exit()

    files = getFiles(command[1],command[2])
    if files == []:
        print('/!\ No such files found in current directory.')
        sys.exit()

    if c0 == 'move':
        move(files, os.getcwd(), command[3])
    elif c0 == 'rename':
        if(command[1] != '-n'):
            print('/!\ Renaming files requires the name of the files. Type "help" for the list of all commands.')
        rename(files, command[2], command[3]) 

    return


#command syntax:    > move/rename/help  type/name  arg1  arg2
#                            c0            c1       c2    c3

if __name__ == "__main__":
    if(sys.argv[1:] != []):
        command = sys.argv[1:]
    else: command = []
    prompt(command)
    
    while(True):
        command = []
        prompt(command)
    
    os.system("pause")
