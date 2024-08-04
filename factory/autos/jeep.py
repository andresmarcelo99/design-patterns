from autos.abs_auto import AbsAuto

class Jeep(AbsAuto):
    def start(self):
        print("Jeep running")

    def stop(self):
        print('Jeep shutting down')