# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet

class SpaceInput:

    def read_space_objects_data_from_file(input_filename):
        """Cчитывает данные о космических объектах из файла, создаёт сами объекты
        и вызывает создание их графических образов

        Параметры:


        **input_filename** — имя входного файла
        """
        objects = []
        with open(input_filename) as input_file:
            for line in input_file:
                if len(line.strip()) == 0 or line[0] == '#':
                    continue  # пустые строки и строки-комментарии пропускаем
                object_type = line.split()[0].lower()
                if object_type == "star":  # FIXME: do the same for planet
                    star = Star(0, '', 0, 0, 0, 0, 0,0)
                    SpaceInput.parse_star_parameters(line, star)
                    objects.append(star)
                elif object_type == "planet":
                    planet = Planet(0, '', 0, 0, 0, 0, 0,0)
                    SpaceInput.parse_planet_parameters(line, planet)
                    objects.append(planet)
                else:
                    print("Unknown space object")

        return objects


    def parse_star_parameters(line, star):
        """Считывает данные о звезде из строки.
        Входная строка должна иметь слеюущий формат:
        Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

        Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
        Пример строки:
        Star 10 red 1000 1 2 3 4

        Параметры:

        **line** — строка с описание звезды.
        **star** — объект звезды.
        """
        data = line.split()[1:]
        star.R = int(data[0])
        star.color = data[1]
        star.m =float(data[2])
        star.x = float(data[3])
        star.y = float(data[4])
        star.Vx = float(data[5])
        star.Vy = float(data[6])
        star.orbit_number = 0
        # FIXME: not done yet

    def parse_planet_parameters(line, planet):
        """Считывает данные о планете из строки.
        Предполагается такая строка:
        Входная строка должна иметь слеюущий формат:
        Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

        Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
        Пример строки:
        Planet 10 red 1000 1 2 3 4

        Параметры:

        **line** — строка с описание планеты.
        **planet** — объект планеты.
        """
        data = line.split()[1:]
        planet.R = int(data[0])
        planet.color = data[1]
        planet.m =float(data[2])
        planet.x = float(data[3])
        planet.y = float(data[4])
        planet.Vx = float(data[5])
        planet.Vy = float(data[6])
        planet.orbit_number = int(data[7])  
        # FIXME: not done yet...


    def write_space_objects_data_to_file(output_filename, space_objects):
        """Сохраняет данные о космических объектах в файл.
        Строки должны иметь следующий формат:
        Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
        Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

        Параметры:

        **output_filename** — имя входного файла
        **space_objects** — список объектов планет и звёзд
        """
        with open(output_filename, 'w') as out_file:
            for obj in space_objects:
                print(f"Тип-{obj.type} Радиус-{obj.R} Цвет-{obj.color} Масса-{obj.m} ",
                    f"Кордината х-{obj.x} Кордината y- {obj.y} Скорость по х-{obj.Vx} Скорость по y-{obj.Vy}"
                    , file=out_file, end="\n\n")
                # FIXME: should store real values

    # FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...
    

if __name__ == "__main__":
    print("This module is not for direct call!")
