"""
 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
"""
import json
import xlwt


def read_text_as_json(file):
    return json.load(open(file, encoding='utf-8'))


workbook = xlwt.Workbook()
sheet = workbook.add_sheet('city')

if __name__ == '__main__':
    result = read_text_as_json('../text/city.txt')
    i = 0
    for key in sorted(result.keys()):
        sheet.write(i, 0, key)
        sheet.write(i, 1, result[key])
        i += 1
    workbook.save('../text/city.xls')