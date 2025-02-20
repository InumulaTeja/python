class Converter:
    conversion_factors = {
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34,
        'kilometers': 1000,
        'meters': 1,
        'centimeters': 0.01,
        'millimeters': 0.001
    }
    def __init__(self,length,unit):
        if unit not in self.conversion_factors:
            print("invalid units")
            unit='meters'
        self.length_in_meters = length * self.conversion_factors[unit]
    def inches(self):
        return self.length_in_meters / self.conversion_factors['inches']
    def feet(self):
        return self.length_in_meters / self.conversion_factors['feet']
    def yards(self):
        return self.length_in_meters / self.conversion_factors['yards']
    def miles(self):
        return self.length_in_meters / self.conversion_factors['miles']
    def kilometers(self):
        return self.length_in_meters / self.conversion_factors['kilometers']
    def meters(self):
        return self.length_in_meters / self.conversion_factors['meters']
    def centimeters(self):
        return self.length_in_meters / self.conversion_factors['centimeters']
    def millimeters(self):
        return self.length_in_meters / self.conversion_factors['millimeters']
c=Converter(9,'inches')
print(c.feet())
