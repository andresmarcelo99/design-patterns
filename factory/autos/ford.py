from autos.abs_auto import AbsAuto

class Ford(AbsAuto):
    def start(self):
        print("Ford running")

    def stop(self):
        print('Ford shutting down')