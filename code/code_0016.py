"""
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
"""

from code import code_0015
import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("numbers")
if __name__ == '__main__':
    result = code_0015.read_text_as_json('../text/numbers.txt')
    for i in range(len(result)):
        for j in range(len(result[i])):
            sheet.write(i, j, result[i][j])
    workbook.save('../text/numbers.xls')
