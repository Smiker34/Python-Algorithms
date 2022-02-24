print('Ведите две буквы латинского алфавита:')
char1 = input('char1 = ').lower()
char2 = input('char2 = ').lower()

print(f'Буква "{char1}" {ord(char1) - 96}-я в алфавите\n'
      f'Буква "{char2}" {ord(char2) - 96}-я в алфавите\n'
      f'Между буквами {abs((ord(char1) - 64) - (ord(char2) - 64)) - 1} букв')