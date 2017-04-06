"""
 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
"""
import json
import xlwt


class Student:
    def __init__(self, _id, name, *score):
        self.id = _id
        self.name = name
        self.score = score


def read_text_as_json():
    j = json.load(open('../text/student.txt', encoding='utf-8'))
    return j


workbook = xlwt.Workbook(encoding='utf-8')
table = workbook.add_sheet('Sheet1')

if __name__ == '__main__':
    print(read_text_as_json())
    result = read_text_as_json()
    i = 0
    for each in sorted(result):
        student = Student(each, result[each].pop(0), result[each])
        table.write(i, 0, student.id)
        table.write(i, 1, student.name)
        for j in range(len(student.score[0])):
            table.write(i, 2 + j, student.score[0][j])
        i += 1
    workbook.save('../text/student.xls')
