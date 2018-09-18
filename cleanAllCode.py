from __future__ import print_function, unicode_literals

from unidiff import PatchSet

repos = open("C:/Users/happyuser/Desktop/GitHub_Scraper/1000000/scraper/1000000_Packages_SearchHits_Ruby.txt", "r")
for name in repos:
    name = name.replace('/', '-')
    name = name.replace('\n', '')


    try:
        patches = PatchSet.from_filename('K:/cloned_searchFiles_rb/' + name + '_patches.diff', encoding='utf-8')

        with open('C:/Users/happyuser/Desktop/GitHub_Scraper/1000000/codeCSV_rb/' + name + '.csv',
                  'w',
                  newline='') as file:
            file.write("projectName, commitID, author, date, fileName, modifications, codechangetype")
            file.write("\n")
        print(name)

        for patch in patches:
            stringPath = str(patch.path)
            arr = str(patch).splitlines()
            codeModified = []

            for line in arr:
                if(line.__len__() > 1):
                    if (line[0] == "+" or line[0] == "-") and line[1] != "+" and line[1] != "-":
                        if (line[0] == "+"):
                            codeModified.append('"' + line.replace("+", "").replace("-", "").replace(",", "").replace('"', "").replace("'", "") + '"' + ', "A"')
                        elif (line[0] == "-"):
                            codeModified.append('"' + line.replace("+", "").replace("-", "").replace(",", "").replace('"', "").replace("'", "") + '"' + ', "D"')
                    elif line.__contains__("Author: "):
                        author = (line.replace("Author: ", ""))
                    elif line.__contains__("Date: "):
                        date = (line.replace("Date:  ", ""))
                    elif line.__contains__(("commit ")):
                        commitID = (line.replace("commit ", ""))


            if len(codeModified) > 0:
                with open(
                        'C:/Users/happyuser/Desktop/GitHub_Scraper/1000000/codeCSV_rb/' + name + '.csv',
                        'a',
                        newline='') as file:
                    weGood = True

                    for line in codeModified:
                        try:
                            file.write(
                                name + ", " + commitID + ", " + author + ", " + date + ", " + stringPath + ", " + line)
                            file.write("\n")
                        except:
                            pass
    except:
        pass