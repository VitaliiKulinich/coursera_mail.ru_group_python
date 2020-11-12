import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.carrying = float(carrying)
        self.brand = brand
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_length, self.body_width, self.body_height = body_whl.split("x")

            self.body_length = float(self.body_length)
            self.body_width = float(self.body_width)
            self.body_height = float(self.body_height)

        except (AttributeError, ValueError):
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0
        self.car_type = 'truck'

    def get_body_volume(self):
        return float(self.body_width) * float(self.body_height) * float(self.body_length)


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename, "r") as file:
            data = csv.reader(file, delimiter=';')

            for vehicle in data:
                #try:
                if os.path.splitext(vehicle[3])[1] == '' or os.path.splitext(vehicle[3])[1] not in ('.jpeg', '.jpg', ".png", ".gif"):
                    continue
                if vehicle[0] == 'car' and vehicle[1]!='' and vehicle[5]!='' and vehicle[2] != '':
                    car_list.append(Car(vehicle[1], vehicle[3], vehicle[5], vehicle[2]))
                if vehicle[0] == 'truck'and vehicle[1]!='' and vehicle[5]!='':
                    car_list.append(Truck(vehicle[1], vehicle[3], vehicle[5], vehicle[4]))
                if vehicle[0] == "spec_machine"and vehicle[1]!='' and vehicle[5]!='' and vehicle[6] != '':
                    car_list.append(SpecMachine(vehicle[1], vehicle[3], vehicle[5], vehicle[6]))
                #except IndexError:
                  #  continue
    except ValueError:
        pass
    return car_list


if __name__ == '__main__':
    for i in get_car_list("coursera_week3_cars.csv"):
        print(i)
