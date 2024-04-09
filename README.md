# Task #3. Website analytics (EN)
## Installation Guide
1. Install Python 3.11.4: https://www.python.org/downloads/release/python-3114/.
2. Open the console in the main project directory.
3. Run the program: Windows - python main.py, Linux - python3 main.py.

## Description
The program takes 2 CSV files as input (day 1 and day 2). It outputs the IDs of users who visited the page on both days or only on the second day. The program uses Python's set() data type to avoid repeating elements.

The overall complexity of the algorithm will be O(m * n), where m is the number of records for day 1, and n is the number of records for day 2. If m and n are of the same size, the complexity will be O(n^2), so the algorithm is optimal for small data sets.

Execution time: 3 hours 27 minutes.

# Task #3. Website analytics (UA)
## Інструкція з інсталяції
1. Встановити Python 3.11.4: https://www.python.org/downloads/release/python-3114/.
2. Відкрити консоль в головній директорії проєкту.
3. Запуск програми: Windows - python main.py, Linux - python3 main.py.

## Опис роботи
Програма приймає на вхід 2 файли CSV (1 і 2 день). На вихід виводить ID користувачів, які відвідали сторінку в обидва дні або тільки другого дня. Програма використовує тип даних set() мови Python, щоб уникнути повторення елементів.

Загальна складність алгоритму буде O(m * n), де m – кількість записів за 1 день, а n – кількість записів за 2 день. Якщо m і n однакового розміру, складність буде O(n^2), тому алгоритм оптимальний для невеликих наборів даних.

Час виконання роботи: 3 год. 27 хв.