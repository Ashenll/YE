# coding: utf-8
# license: GPLv3

from solar_objects import *
class SpaceVis:

    """Модуль визуализации.
    Нигде, кроме этого модуля, не используются экранные координаты объектов.
    Функции, создающие гaрафические объекты и перемещающие их на экране, принимают физические координаты
    """

    header_font = "Arial-16"
    """Шрифт в заголовке"""

    window_width = 800
    """Ширина окна"""

    window_height = 800
    """Высота окна"""

    scale_factor = None
    """Масштабирование экранных координат по отношению к физическим.
    Тип: float
    Мера: количество пикселей на один метр."""


    def calculate_scale_factor(max_distance):
        """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
        SpaceVis.scale_factor = 0.4*min(SpaceVis.window_height, SpaceVis.window_width)/max_distance
        print('Scale factor:', SpaceVis.scale_factor)

    def scale_x(x):
        """Возвращает экранную **x** координату по **x** координате модели.
        Принимает вещественное число, возвращает целое число.
        В случае выхода **x** координаты за пределы экрана возвращает
        координату, лежащую за пределами холста.

        Параметры:

        **x** — x-координата модели.
        """

        return int(x*SpaceVis.scale_factor) + SpaceVis.window_width//2


    def scale_y(y, orbit_number):
        """Возвращает экранную **y** координату по **y** координате модели.
        Принимает вещественное число, возвращает целое число.
        В случае выхода **y** координаты за пределы экрана возвращает
        координату, лежащую за пределами холста.
        Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

        Параметры:

        **y** — y-координата модели.
        **orbit_number** - номер орбиты объекта
        """
        orbit_number = orbit_number
        if orbit_number %2 == 0:
            return SpaceVis.window_height // 2 - int(y *SpaceVis.scale_factor)
        else:
            return int(y*SpaceVis.scale_factor) + SpaceVis.window_height//2


    def create_star_image(space, star):
        """Создаёт отображаемый объект звезды.

        Параметры:

        **space** — холст для рисования.
        **star** — объект звезды.
        """

        x = SpaceVis.scale_x(star.x)
        y = SpaceVis.scale_y(star.y,orbit_number=star.orbit_number)
        r = star.R
        star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


    def create_planet_image(space, planet):
        """Создаёт отображаемый объект планеты.

        Параметры:

        **space** — холст для рисования.
        **planet** — объект планеты.
        """
        x = SpaceVis.scale_x(planet.x)
        y = SpaceVis.scale_y(planet.y,orbit_number=planet.orbit_number)
        r = planet.R
        planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


    def update_system_name(space, system_name):
        """Создаёт на холсте текст с названием системы небесных тел.
        Если текст уже был, обновляет его содержание.

        Параметры:

        **space** — холст для рисования.
        **system_name** — название системы тел.
        """
        space.create_text(30, 80, tag="header", text=system_name, font=SpaceVis.header_font)


    def update_object_position(space, body):
        """Перемещает отображаемый объект на холсте.

        Параметры:

        **space** — холст для рисования.
        **body** — тело, которое нужно переместить.
        """
        x = SpaceVis.scale_x(body.x)
        y = SpaceVis.scale_y(body.y, orbit_number=body.orbit_number)
        r = body.R
        if x + r < 0 or x - r > SpaceVis.window_width or y + r < 0 or y - r > SpaceVis.window_height:
            space.coords(body.image, SpaceVis.window_width + r, SpaceVis.window_height + r,
                        SpaceVis.window_width + 2*r, SpaceVis.window_height + 2*r)  # положить за пределы окна
        space.coords(body.image, x - r, y - r, x + r, y + r)



if __name__ == "__main__":
    print("This module is not for direct call!")

    print("This module is not for direct call!")

