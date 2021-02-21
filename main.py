class Electric_lamp:
    count = 0

    @classmethod
    def number(cls):
        print(f"Amount of objects {cls.count}")

    def __init__(self, firm_producer="Ukraine", lighting_power=12, working_duration=3, country_producer="Ukraine",
                 price=100, material="glass"):
        self.firm_producer = firm_producer
        self.lighting_power = lighting_power
        self.working_duration = working_duration
        self.country_producer = country_producer
        self.price = price
        self.material = material
        Electric_lamp.count += 1

    def __str__(self):
        return f"The firm which produce it is - {self.firm_producer}, \n" \
               f"The lighting power is - {self.lighting_power}, watts, \n" \
               f"The duration of work is - {self.working_duration}, days, \n" \
               f"The country which produce it is - {self.country_producer}, \n" \
               f"The price is - {self.price}, \n" \
               f"The material is - {self.material}, \n" \


    def __del__(self):
        del self
        print("method __del__")


first_lamp = Electric_lamp("Samsung", 30, 120, "Korea", 150, "plastic")
print(first_lamp.__str__())
second_lamp = Electric_lamp()
print(second_lamp.__str__())
third_lamp = Electric_lamp("Philips", 40, 240)
print(third_lamp.__str__())
Electric_lamp.number()
