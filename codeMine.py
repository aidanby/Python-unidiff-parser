from __future__ import print_function, unicode_literals
import argparse
import codecs
import sys
import unidiff
import re
import string
import csv
from unidiff import PatchSet, DEFAULT_ENCODING

lines = open("C:/Users/happyuser/Desktop/GitHub_Scraper/1000000/1000000_Packages_SearchHits.txt", "r")
userNames = []

for line in lines:
    userNames.append(line)

    for name in userNames:
        name = name.replace('/', '-')
        name = name.replace('\n', '')


    try:
        patches = PatchSet.from_filename('K:/cloned_searchFiles/' + name + '_patches.diff', encoding='utf-8')
        hasFeatureIDs = []
        i = 0
        while (i < len(patches) - 1):
            stringPath = str(patches[i].path)
            pathList = stringPath.split(".")
            lastIndex = pathList.__len__() - 1
            if pathList[lastIndex] == "feature":
                #print(stringPath)
                arr = str(patches[i]).splitlines()
                hasCommit = False
                for line in arr:
                    if line.__contains__("commit "):
                        commitID = (line.replace("commit ", ""))
                        hasFeatureIDs.append(commitID)
                        hasCommit = True
                if hasCommit == False:
                    j = i - 1
                    while hasCommit == False:
                        stringPath = str(patches[j].path)
                        arr = str(patches[j]).splitlines()
                        for line in arr:
                            if line.__contains__("commit "):
                                commitID = (line.replace("commit ", ""))
                                hasFeatureIDs.append(commitID)
                                #print(commitID)
                                hasCommit = True
                        j = j - 1
            i = i+1

        if len(hasFeatureIDs) > 0:
            with open('C:/Users/happyuser/Desktop/GitHub_Scraper/1000000/codeCSV_allFiles_test/' + name + '.csv',
                      'w',
                      newline='') as file:
                file.write("projectName, commitID, author, date, isBdd, fileName, modifications")
                file.write("\n")
            print(name)
            #with open('C:/Users/happyuser/Desktop/GitHub_Scraper/1000000/code-toR-allFiles.txt',
                      #'a',
                      #newline='') as file:
                #file.write(name + "\n")

        i = 0
        while(i < len(patches) - 1):
            hasBDD = False
            stringPath = str(patches[i].path)
            arr = str(patches[i]).splitlines()
            codeModified = []
            for line in arr:
                if line.__contains__("commit "):
                    commitID = (line.replace("commit ", ""))
                    if hasFeatureIDs.__contains__(commitID):
                        #print("Starting with file: " + stringPath)
                        hasBDD = True
            if hasBDD == False:
                i = i+1
                continue

            if hasBDD == True:
                for line in arr:
                    if len(line) > 1:
                        if (line[0] == "+" or line[0] == "-") and line[1] != "+" and line[1] != "-":
                            codeModified.append(line.replace("+", "").replace("-", ""))

                        elif line.__contains__("Author: "):
                            author = (line.replace("Author: ", ""))
                        elif line.__contains__("Date: "):
                            date = (line.replace("Date:  ", ""))


                hasCommit = False
                if len(codeModified) > 0:
                    with open(
                        'C:/Users/happyuser/Desktop/GitHub_Scraper/1000000/codeCSV_allFiles_test/' + name + '.csv',
                        'a',
                    newline='') as file:
                        #file.write("\n")
                        for line in codeModified:
                            file.write(
                                name + ", " + commitID + ", " + author + ", " + date + ", " + stringPath + ", " + '"' + line.replace('"', "").replace("'", "") + '"')
                            file.write("\n")
                j = i + 1
                while hasCommit == False:
                    stringPath = str(patches[j].path)
                    arr = str(patches[j]).splitlines()
                    codeModified = []
                    for line in arr:
                        if len(line) > 1:
                            if line.__contains__("commit "):
                                hasCommit = True
                                break
                            elif (line[0] == "+" and line[1] != "+") or (line[0] == "-" and line[1] != "-"):
                                codeModified.append(line.replace("+", "").replace("-", ""))
                            elif line.__contains__("Author: "):
                                author = (line.replace("Author: ", ""))
                            elif line.__contains__("Date: "):
                                date = (line.replace("Date:  ", ""))
                    if len(codeModified) > 0:
                        with open(
                                'C:/Users/happyuser/Desktop/GitHub_Scraper/1000000/codeCSV_allFiles_test/' + name + '.csv',
                                'a',
                                newline='') as file:
                            #file.write("\n")
                            for line in codeModified:
                                file.write(
                                    name + ", " + commitID + ", " + author + ", " + date + ", " + stringPath + ", " + '"' + line.replace('"', "").replace("'", "") + '"')
                                file.write("\n")
                    j = j+1
            i = i+1
    except:
        pass

