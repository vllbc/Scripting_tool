import os

def copyFiles(sourceDir,targetDir):
    if sourceDir.find("exceptionfolder")>0:
        return
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,file)
        targetFile = os.path.join(targetDir,file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) !=
 os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
                print(targetFile+ " copy succeeded")
        if os.path.isdir(sourceFile):
            copyFiles(sourceFile, targetFile)