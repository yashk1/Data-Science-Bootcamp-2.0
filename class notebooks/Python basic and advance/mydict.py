class dict_parser():
    def __init__(self, dic) -> None:
        self.dic = dic

    def get_keys(self):
        if self.input_type():
            return self.dic.keys()

    def get_values(self):
        return self.dic.values()

    def input_type(self):
        if type(self.dic) != dict:
            raise Exception(self.a, "Not a dictionary")

    def take_input(self):
        a = input('enter a key')
        b = input('enter a value')

        self.dic[a] = b
        return self.dic

    def insert_new_pair(self, key, value):
        self.dic[key] = value
        return self.dic

