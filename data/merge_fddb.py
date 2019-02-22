import glob
import os

fddbPath = os.path.expanduser("~/datasets/fddb/FDDB-folds/")
lff = glob.glob(os.path.join(fddbPath, "*ellipseList.txt"))
lff = sorted(lff)
print lff

with open(os.path.join("FDDB", 'img_list_ellipseList.txt'), 'w') as fileWriter:
    for f in lff:
        with open(f, "r") as fileReader:
            fileWriter.write(fileReader.read())