# Домашнє завдання: Оцінка інтегралів методом Монте-Карло та методом `quad`

## Опис завдання

У цьому завданні ми оцінили значення визначеного інтегралу функції \( f(x) = x^2 \) на інтервалі \([a, b]\) за допомогою двох методів:

1. Метод Монте-Карло
2. Метод числової інтеграції `quad` із бібліотеки SciPy

Інтервал, на якому обчислюється інтеграл, заданий як \([a, b] = [0, 2]\).

## Метод Монте-Карло

Метод Монте-Карло використовується для оцінки інтегралів за допомогою випадкових чисел. У нашому випадку для оцінки інтегралу функції \( f(x) = x^2 \) ми генеруємо випадкові точки у прямокутному обмеженні \([a, b]\) по осі \( x \) і \([0, f(b)]\) по осі \( y \). Потім підраховуємо, яка частина цих точок знаходиться під кривою функції, що дозволяє наближено оцінити площу під графіком функції.

## Метод `quad`

Метод `quad` із бібліотеки SciPy є стандартним методом для числового обчислення інтегралів. Він надає точне значення інтегралу разом з оцінкою похибки.

## Результати

Після виконання розрахунків отримали такі результати:

- **Метод Монте-Карло**: 2.66674
- **Метод `quad`**: 2.666666666666667 (з помилкою 2.96e-11)

### Порівняння результатів

1. **Результат методу Монте-Карло**: Оцінка інтегралу методом Монте-Карло наближається до значення інтегралу, отриманого методом `quad`, з невеликою похибкою. Оскільки метод Монте-Карло заснований на випадкових числах, його точність залежить від кількості випадкових точок, що генеруються (у нашому випадку \( N = 100000 \)).
2. **Результат методу `quad`**: Метод `quad` дає точний результат інтеграції функції на зазначеному інтервалі. Похибка, яка була оцінена, є дуже малою і не впливає на результат.

## Висновки

1. **Метод Монте-Карло** є наближеним методом, і його точність залежить від кількості випадкових точок. Збільшення кількості точок може покращити точність, але вимагає більше часу на обчислення.
2. **Метод `quad`** дає дуже точний результат, оскільки є спеціалізованим методом числової інтеграції.

3. Порівнюючи результати, можна зробити висновок, що метод Монте-Карло дає достатньо точні результати для практичних завдань, якщо кількість випадкових точок велика. Однак для більш точних обчислень краще використовувати методи, подібні до `quad`.

## Візуалізація

Графік, на якому показано функцію \( f(x) = x^2 \), а також розподіл випадкових точок під та над кривою, дозволяє наочно побачити, як метод Монте-Карло оцінює площу під графіком.

- Блакитні точки знаходяться під кривою функції.
- Червоні точки знаходяться над кривою.

Ця візуалізація допомагає зрозуміти, як працює метод Монте-Карло.
