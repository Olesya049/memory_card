from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QPushButton, QButtonGroup
)
from random import *

class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('Memory Card')
push_button = QPushButton('Ответить')
question = QLabel('Какой национальности не существует?')

# Создание результатов
RadioGroupBoxRes = QGroupBox('Результат теста')
res_text = QLabel('Правильно/Неправильно')
answer_text = QLabel('Правильный ответ')
ans_line = QVBoxLayout()
ans_line.addWidget(res_text, alignment=Qt.AlignLeft)
ans_line.addWidget(answer_text, alignment=Qt.AlignCenter)
RadioGroupBoxRes.setLayout(ans_line)

# Создание вариантов  
RadioGroupBox = QGroupBox('Варианты ответов')
answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Чулымцы')
answer3 = QRadioButton('Смурфы')
answer4 = QRadioButton('Алеуты')
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line2.addWidget(answer1)
line2.addWidget(answer2)
line3.addWidget(answer3)
line3.addWidget(answer4)
line1.addLayout(line2)
line1.addLayout(line3)

# Объединение вариантов ответов в группу
RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)
RadioGroupBoxRes.hide()
RadioGroupBox.setLayout(line1)

# Размещение виджетов в главном окне
main_line = QVBoxLayout()
main_line.addWidget(question, alignment = (Qt.AlignCenter))
main_line.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
main_line.addWidget(RadioGroupBoxRes)
main_line.addWidget(push_button, alignment = Qt.AlignCenter)
my_win.setLayout(main_line)

# Классы объектов
def show_question():
    RadioGroupBox.show()
    RadioGroupBoxRes.hide()
    push_button.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    RadioGroupBoxRes.show()
    push_button.setText('Следующий вопрос')

answers = [answer1, answer2, answer3, answer4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)

def show_correct(res, correct_ans):
    res_text.setText(res)
    answer_text.setText(correct_ans)    

def test():
    if answers[0].isChecked():
        show_correct('Верно!', answers[0].text())
        show_result()
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно', answers[0].text())
        show_result()
    

push_button.clicked.connect(test)

q = Question('Как переводится слово "Literally"', 'буквально', 'литературный', 'литература', 'образно')
ask(q)

my_win.show()
app.exec_()
