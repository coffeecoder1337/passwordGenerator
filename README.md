# passwordGenerator

import pg

pgen = pg.PasswordGenerator()
pg.writeTextToFile('password.txt', pgen.createPassword(5000, pgen.createDictionary(upper=True, digital=True)))

// bsF806u2rGXJHth7T56TRgOfDeEmJioUOnstFFYkOzS5c17RPktJc8LAXviinJ

# запоминаете стартовую и конечную позицию вашего пароля и шаг. Например, 0 10 1

print(pgen.getPassword(0, 10, 1, pg.readTextFromFile('password.txt')))

// bsF806u2rG
