import webbrowser
import sys
import shelve
import shelveGrouping

def opengroup(shelveFileName, groupname):
    shelfFile = shelve.open(shelveFileName)
    if groupname not in shelfFile:
        print('Group Not Found')
        return
    for page in shelfFile[groupname]:
        webbrowser.open(page)
    print(str(len(shelfFile[groupname])) + ' pages opened ')


def showhelp():
    print('''-groupname                     Opens WebGroup
    -a -groupname [webpage 1, webpage 2,..] Adds webpages to group
    -rm -groupname [webpage 1, webpage 2,..] Removes webpages to group
    -ls Lists all groups
    -lsa Lists all groups and pages within
    -help shows commands''')


shelveFileName='webPageGroups'
if len(sys.argv) <= 1:
    print('Not enough arguments passed')

elif len(sys.argv) == 2:
    arg1 = sys.argv[1]
    if arg1 == '-ls':
        shelveGrouping.listgroups(shelveFileName)
    elif arg1 == '-lsa':
        shelveGrouping.listgroups(shelveFileName,True)
    elif arg1 == '-help':
        showhelp()
    else:
        opengroup(shelveFileName,arg1[1:])

else:
    if sys.argv[1] == '-a':
        shelveGrouping.addToGroup(shelveFileName,sys.argv[2][1:], sys.argv[3:])
    elif sys.argv[1] == '-rm':
        shelveGrouping.removeFromGroup(shelveFileName,sys.argv[2][1:], sys.argv[3:])
    else:
        print('Command Not found')

