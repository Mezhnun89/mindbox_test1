# Геометрический калькулятор

Это простая библиотека на Python для вычисления площади круга и треугольника, а также проверки на прямоугольность треугольника.

## Файлы

- `geometry.py`: Файл с исходным кодом библиотеки.
- `test_geometry.py`: Файл с юнит-тестами для библиотеки.

## Использование

Чтобы использовать библиотеку, просто импортируйте класс `GeometryCalculator` из файла `geometry.py` и вызывайте соответствующие методы:

```python
from geometry import GeometryCalculator

# Вычисление площади круга
radius = 5
area = GeometryCalculator.circle_area(radius)
print("Площадь круга:", area)

# Вычисление площади треугольника
side1, side2, side3 = 3, 4, 5
area = GeometryCalculator.triangle_area(side1, side2, side3)
print("Площадь треугольника:", area)

# Проверка на прямоугольность треугольника
is_right_triangle = GeometryCalculator.is_right_triangle(side1, side2, side3)
print("Это прямоугольный треугольник?", is_right_triangle)
```

## Запуск тестов

Чтобы запустить юнит-тесты, используйте команду:

```
python test_geometry.py
```


