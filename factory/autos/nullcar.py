from autos.abs_auto import AbsAuto


class NullCar(AbsAuto):
    def __init__(self, carname) -> None:
        self._carname = carname

    def start(self):
        print(f'Unknown car {self._carname}')

    def stop(self):
        pass