from random import choice


class RandomWalk:
    """Класс для генерации случайных блужданий"""

    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания."""
        # Шаги генерируются до достижения нужной длинны.
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений x и y.
            next_x = self.x_values[-1] + int(x_step)
            next_y = self.y_values[-1] + int(y_step)

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        # Определение направления и длинны перемещения.
        xy_direction = choice([1, -1])
        xy_distance = choice([0, 1, 2, 3, 4])
        xy_step = xy_direction * xy_distance
        return xy_step
