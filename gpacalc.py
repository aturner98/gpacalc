def calcGPA(student,aDict): 
    grades1 = 0
    hours = 0
    if student in aDict:
        for x in aDict[student]:
            if aDict[student] == []:
                return 0.0
            if x[1] >= 90:
                grade = 4
            elif x[1] >= 80:
                grade = 3
            elif x[1] >= 70:
                grade = 2
            elif x[1] >= 60:
                grade = 1
            elif x[1] < 60:
                grade = 0
            grades1 = grades1 + grade * x[2]
            hours = hours + x[2]

        gpa = grades1 / hours
        return round(gpa,2) 
    else:
        return 0.0
