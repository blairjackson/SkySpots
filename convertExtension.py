import os

def convert():
    path = input('Provide file path:')

    if path:
        originalPath = os.getcwd()
        #strip extension and change to .csv
        #change working directory to edit file name
        sPath = path.split('/')
        newPath ='/'.join(sPath[:-1])
        file = sPath[-1]
        newfile = file[:-4]
        filename = newfile + '.csv'
        os.chdir(newPath)
        os.renames(file, filename)
        os.chdir(originalPath)
        return newPath + '/' + filename