import shutil
def makeZip(outputName, directoryName):
    shutil.make_archive(outputName, 'zip', directoryName)

makeZip("cates", "cates")
