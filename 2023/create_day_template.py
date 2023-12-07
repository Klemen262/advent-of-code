#!/bin/python
import sys
import os
import urllib.request
import datetime

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        day = str(datetime.date.today().day)
    else:
        day = args[0]
    if len(day) == 1:
        day = "0" + day
    day_one_digit = day.lstrip("0")

    if os.path.exists(f"html/day{day}.html"):
        file = open(f"html/day{day}.html")
        content = file.read()
    else:
        content = urllib.request.urlopen(f"https://adventofcode.com/2023/day/{day_one_digit}").read().decode('utf-8')
    
    test_input = get_test_input(content)
    answer, question = get_test_answer_and_question(content[:content.find("--- Part Two ---")])
    print(question)
    create_template(day, content, test_input, answer)

# reads last two <em> elements
def get_test_answer_and_question(content):
    start_txt = "<em>"
    end_txt = "</em>"
    start = content.find(start_txt) + len(start_txt)
    forward = 0
    ems = []
    while forward != -1:
        end = start + content[start:].find(end_txt)
        if start > 0 and end > start:
            ems.append(content[start:end])
        forward = content[end:].find(start_txt)
        start = end + forward + len(start_txt)
    return ems[-2:]

# reads first code block
def get_test_input(content):
    start_code_block = "<pre><code>"
    end_code_block = "</code></pre>"
    start = content.find(start_code_block) + len(start_code_block)
    end = content.find(end_code_block)
    if start > 0 and end > start:
        code_block = content[start:end]
    return code_block

def create_template(day, content, test_input, answer):
    template = open("day??_template.py", "r")
    content = template.read()
    template.close()
    content = content.replace('test_input_1 = """"""', 'test_input_1 = """' + test_input + '"""')
    content = content.replace('test_result_1 = -1', 'test_result_1 = ' + str(answer))
    content = content.replace("??", day)
    day_file = open(f"day{day}.py", "w")
    day_file.write(content)

if __name__ == "__main__":
    main()