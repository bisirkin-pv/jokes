class PropertyReader:
    """ Class read ini file and create dict """

    def __init__(self, filename):
        self.filename = filename
        self.property = dict()
        self.__read()

    def __read(self):
        try:
            with open(self.filename) as f:
                for line in f:
                    (key, val) = line.split('=')
                    self.property[key] = val
        except IOError:
            print("Error create file")

    def get(self, key):
        return self.property.get(key)
