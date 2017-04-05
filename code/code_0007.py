"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""
import os


def is_line_blank(line):
    if not line:
        return True
    if not line.strip():
        return True
    return False


def count_lines(dir):
    blank = 0
    code = 0
    comment = 0
    for dir_path, dir_names, file_names in os.walk(dir):
        for file in (os.path.join(dir_path, filename) for filename in file_names if filename.strip().endswith(".java")):
            with open(file, encoding='utf-8') as f:
                comment_flag = False
                for line in f:
                    if is_line_blank(line):
                        blank += 1
                    else:
                        line = line.strip()
                        if line.startswith("//"):
                            comment += 1
                        elif line.startswith("/*"):
                            comment_flag = True
                            comment += 1
                        elif line.endswith("*/"):
                            comment += 1
                            comment_flag = False
                        elif not comment_flag:
                            code += 1
                        else:
                            comment += 1
    return code, blank, comment


if __name__ == '__main__':
    print("代码 : %s \n空行 : %s \n注释 : %s" % count_lines("../"))
