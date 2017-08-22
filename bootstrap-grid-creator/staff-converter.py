import csv


def writeFileStart(writeFile):
    writeFile.write("<div>\n")
    writeFile.write("<div>\n")
    writeFile.write("<h2>CONTACT US</h2>\n")
    writeFile.write("<p>If you have questions or feedback on AUSA membership, contact us at: Member Services Center 1-855-246-6269 or Membersupport@ausa.org</p>\n")
    writeFile.write("<div class=\"container-fluid\">\n")

def writeDepartment(writeFile,department):
    writeFile.write("<div class=\"row\" style=\"overflow: hidden; border-top:5px solid; border-top-color:#df5400;\">\n")
    writeFile.write("<div class=\"col-xs-12 col-sm-12\" style=\"margin-bottom: -99999px; padding-bottom: 99999px;\">\n")
    writeFile.write("<h2>" + department + "</h2>\n")
    writeFile.write("</div>\n")
    writeFile.write("</div>\n")

def writeRow(writeFile):
    writeFile.write("<div class=\"row\" style=\"overflow: hidden;\">\n")

def writeStaff(writeFile, staffMember):

    writeFile.write("<div class=\"col-xs-5 col-sm-3\" style=\"margin-bottom: -99999px; padding-bottom: 99999px;\">\n")
    writeFile.write("<p>\n")
    if(staffMember[5] != ''):
        writeFile.write("<img class=\"img-responsive\" src=\"" + staffMember[5]+ "\" />\n")
    else:
        writeFile.write("<img class=\"img-responsive\" src=\"https://www.ausa.org/sites/default/files/ausa-transparent-logo.png\"/>\n")
    writeFile.write("</p>\n")
    writeFile.write("</div>\n")
    writeFile.write("<div class=\"col-xs-7 col-sm-3\" style=\"margin-bottom: -99999px; padding-bottom: 99999px;\">\n")
    writeFile.write("<h3 style=\"padding-top: 0px; margin-top: 0px;\">" + staffMember[1] + "</h3>\n")
    writeFile.write("<h5>" + staffMember[2] + "</h5>\n")
    writeFile.write("<p>" + staffMember[3] + "<br />" + staffMember[4] + "</p>\n")

    if(staffMember[6] != ''):
        writeFile.write("<p>\n")
        writeFile.write("<a href=\"" + staffMember[6] + "\">Bio</a>\n")
        writeFile.write("</p>\n")

    writeFile.write("</div>\n")

def writeDivEnd(writeFile):
    writeFile.write("</div>\n")

def writeFileEnd(writeFile):
    writeFile.write("</div>\n")
    writeFile.write("</div>\n")
    writeFile.write("</div>\n")



staffFile = open('staff-page.html', 'w')

writeFileStart(staffFile)

departmentMember = 1
currentDepartment = ''
startOfFile = True

with open('staff-list.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:

        if(startOfFile == False):
            print(row)
            if(currentDepartment != row[0]):
                if(departmentMember % 2 == 0):
                    writeDivEnd(staffFile)
                writeDepartment(staffFile, row[0])
                currentDepartment = row[0]
                departmentMember = 1
            if(departmentMember % 2 > 0):
                writeRow(staffFile)
                writeStaff(staffFile, row)
                departmentMember += 1
            else:
                writeStaff(staffFile, row)
                writeDivEnd(staffFile)
                departmentMember += 1

        else:
            startOfFile = False

    writeFileEnd(staffFile)

f.close()
staffFile.close()