from autos.abs_auto import AbsAuto

class Chevy(AbsAuto):
    def start(self):
        print("Chevvy running")

    def stop(self):
        print('Chevvy shutting down')