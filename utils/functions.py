import re


def classifica_rating(rating):
    vietati_18 = [
        'R', 'NC-17', 'VM18', '18', '18A', 'R18', 'R-18', '18PL', 'C18', 'M/18',
        'MA15+', 'R18+', 'R15+', '18SG', '18TC', 'III', 'IM-18', '18X', 'A-18',
        'R21', 'R-15', 'R15', 'R-15+', 'MA+', 'IM18', 'SAM18', '18PA', '18SX',
        'M21', 'M-18', 'PG18', 'NC18', 'NC-16', 'NC-15', 'NC16', 'R16', 'R-16',
        'R13+', 'R-13', 'PG-17', 'PG-16', 'PG15', 'PG-15', 'PG-14', 'PG13',
        'PG-13', '15', '16', '17', '14A', '15A', '16E', '16LS', '16LV', '16SL',
        '16LPV', 'VM14', 'M/14', 'M14', 'M16', 'M/16', 'M/16Q', 'IM16'
    ]

    per_tutti = [
        'G', 'ATP', 'U', 'ALL', 'TV-G', 'FSK0', 'FSK-0', 'TV-Y7', 'TV-Y', 'SU',
        '0', 'AL', 'AG', 'GA', 'KT/EA', 'EA', 'K+', 'K', 'K7', 'K-7', 'K-6-4'
    ]

    if rating in vietati_18:
        return 'Minori di 18'
    elif rating in per_tutti:
        return 'Per tutti'
    else:
        return 'Altro'

def classifica_durata(row):
    if row['minute'] < 50:
        return 'Cortometraggio'
    elif row['minute'] <= 240:
        return 'Film'
    else:
        return 'Serie'

def status_oscars(row):
    if row.get('winner', False) is True:
        return 'Vincitore'
    elif row.get('nominated', False) is True:
        return 'Nominato'
    else:
        return 'Non nominato'

letter_score = {
    'A+':10, 'A':9.5, 'A-':9.0, 'B+':8.7, 'B':8.5, 'B-':8.0, 'C+':7.7,
    'C':7.5, 'C-':7.2, 'D+':7.0, 'D':6.5, 'D-':6.0, 'F':4,
}

def normalize_review(value):
    value = str(value).strip().upper()

    # for fractions
    if re.match(r'^\d+(\.\d+)?/\d+(\.\d+)?$', value):
        try:
            num, den = map(float, value.split('/'))
            score = (num/den) * 10
            return round(score, 1)
        except:
            return None

    # for float or integer number
    if re.match(r'^\d+(\.\d+)?$', value):
        val = float(value)
        if val<=10:
            return round(val, 1)
        elif val<=100:
            return round((val/100) * 10, 1)
        else:
            return None

    # for the letters
    if value in letter_score:
        return letter_score[value]

    # Nan
    return None