# Horoscopo
from datetime import datetime

HOROSCOPO = {1: 'Capricornio', 2: 'Acuario', 3: 'Picsis', 4: 'Aries', 5: 'Tauro', 6: 'Géminis', 7: 'Cáncer', 8: 'Leo', 9: 'Virgo', 10: 'Libra', 11: 'Escorpión', 12: 'Sagitario'}

def get_sign_name (n):
    return HOROSCOPO.get(n)

def ask_date_birth ():
    date_birth = input('Fecha de nacimiento (dd/mm/YYYY): ')
    return date_birth

def convert_date (d):
    return datetime.strptime(d, '%d/%m/%Y')

def which_is_your_sign (d):
    d = convert_date(d)
    if d.day >= 23:
        return get_sign_name(d.month + 1)
    else:
        return get_sign_name(d.month)
    
def predict_horoscopo():
    d = ask_date_birth()
    s = which_is_your_sign(d)
    print(f'Su fecha de nacimiento es {d}, por tanto su signo del zodiaco es {s}.')
    
predict_horoscopo()