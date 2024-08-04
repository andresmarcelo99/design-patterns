from autofactory import AutoFactory

factory = AutoFactory()

for carname in 'Chevy', 'Ford', 'Jeep', 'Tesla':
    car = factory.create_instance(carname)
    car.start()
    car.stop()