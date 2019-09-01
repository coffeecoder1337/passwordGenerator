import random


class PasswordGenerator:
    def createDictionary(self, lower = True, upper = False, digital = False):
        """Возвращает словарь для генерации пароля.

            :param lower: включает строчные символы
            :param upper: включает заглавные символы
            :param digital: включает цифры
        """
        dictionary = []
        if upper:
            dictionary += [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        if lower:
            dictionary += [chr(i) for i in range(ord('a'), ord('z') + 1)]
        if digital:
            dictionary += [chr(i) for i in range(ord('0'), ord('9') + 1)]
        return dictionary


    def createPassword(self, length, dictionary):
        """Возвращает сгенерированный пароль.
        
            :param length: длина пароля
            :param dictionary: словарь для генерации пароля
        """
        password = ""
        for l in length:
            password += random.choice(dictionary)
        return password
    

    def getPassword(self, start, stop, step, passwordText):
        password = passwordText[start:stop:step] 
        return password
        