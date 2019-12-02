# passwordGenerator

import pg

pg = main.PasswordGenerator()
main.writeTextToFile('password.txt', pg.createPassword(5000, pg.createDictionary(upper=True, digital=True)))

# запоминаете стартовую и конечную позицию вашего пароля и шаг. Например, 0 10 1

print(pg.getPassword(0, 10, 1, main.readTextFromFile('password.txt')))
