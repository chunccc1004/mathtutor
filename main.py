import random

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle


def make_problem():
    problem_list = []
    answer_list = []

    # type
    MUL_ONE = 1
    MUL_TEN = 2
    MUL_HUND = 3

    def make_problem_multiplication(type):
        first_num = random.randint(100, 999)  # 100보다 큼
        second_num = 0
        if type == MUL_ONE:
            second_num = random.randint(2, 9)
        elif type == MUL_TEN:
            second_num = random.randint(11, 99)
        else:
            second_num = random.randint(101, 999)

        return "%d × %d = " % (first_num, second_num), first_num * second_num

    def make_problem_division(type):
        first_num = random.randint(100, 999)  # 100보다 큼
        second_num = 0
        if type == MUL_ONE:
            second_num = random.randint(2, 9)
        elif type == MUL_TEN:
            second_num = random.randint(11, 99)

        return "%d ÷ %d = " % (first_num, second_num), "%d ... %d" % (first_num // second_num, first_num % second_num)

    # # 곱해지는 인자의 자릿수 : 1
    # for _ in range(2):
    #     problem, answer = make_problem(MUL_ONE)
    #     problem_list.append(problem)
    #     answer_list.append(answer)
    #
    # # 곱해지는 인자의 자릿수 : 2
    # for _ in range(3):
    #     problem, answer = make_problem(MUL_TEN)
    #     problem_list.append(problem)
    #     answer_list.append(answer)

    # 곱해지는 인자의 자릿수 : 3
    for _ in range(5):
        problem, answer = make_problem_multiplication(MUL_HUND)
        problem_list.append(problem)
        answer_list.append(answer)
    # 나눠지는 인자의 자릿수 : 1
    for _ in range(2):
        problem, answer = make_problem_division(MUL_ONE)
        problem_list.append(problem)
        answer_list.append(answer)
    # 나눠지는 인자의 자릿수 : 2
    for _ in range(3):
        problem, answer = make_problem_division(MUL_TEN)
        problem_list.append(problem)
        answer_list.append(answer)

    return problem_list, answer_list


def make_test_paper(c: canvas.Canvas, data: list, page_num: int):
    # 표 생성
    table = Table(data, colWidths=50, rowHeights=70)
    table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 30),
    ]))

    # 표 그리기
    table.wrapOn(c, 1000, 1000)
    table.drawOn(c, 100, 100)

    c.drawCentredString(A4[0] / 2, 30, str(page_num))

    c.showPage()


if __name__ == '__main__':
    # PDF 생성
    c_p = canvas.Canvas("problem.pdf", pagesize=A4)
    c_a = canvas.Canvas("answer.pdf", pagesize=A4)

    for page_num in range(30):
        problem_list, answer_list = make_problem()

        # 표 데이터
        for i in range(len(problem_list)):
            problem_list[i] = str(i + 1) + ". " + problem_list[i]
        data_problem = list(map(lambda x: [x], ["Problem"] + problem_list))

        for i in range(len(answer_list)):
            answer_list[i] = str(i + 1) + ". " + str(answer_list[i])
        data_answer = list(map(lambda x: [x], ["Answer"] + answer_list))

        print(data_problem)
        make_test_paper(c_p, data_problem, page_num + 1)
        make_test_paper(c_a, data_answer, page_num + 1)
        # print(answer_list)

    # PDF 저장
    c_p.save()
    c_a.save()
