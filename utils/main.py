from fun import *
import datetime


class Check:

    def __init__(self, date, num_card, num_account):
        self.date = date
        self.num_card = num_card
        self.num_account = num_account

    def count_now(self, from_to):

        from_to_slip = from_to.split(' ')
        if from_to_slip[0] == 'Счет':
            self.num_account = from_to_slip[-1]
            return ' '.join(from_to_slip[:-1]) + ' ' + check_new.mask_account()
        else:
            self.num_card = from_to_slip[-1]
            return ' '.join(from_to_slip[:-1]) + ' ' + check_new.mask_card()

    def mask_account(self):
        return '*' * len(self.num_account[:-4]) + self.num_account[-4:]

    def mask_card(self):

        num_ = self.num_card.replace((self.num_card[6:12]), 'xxxxxx')
        return num_[:4] + ' ' + num_[4:8] + ' ' + num_[8:12] + ' ' + num_[12:]

    def format_date(self):

        date = datetime.datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        return f'{date:%d.%m.%Y}'

    def __repr__(self):
        return f'{self.date}.{self.num_card}.{self.num_account}'


info_for_check = []
check = get_executed(check_sorting(delete_void_list_(read_json())))

for i in check[-5:]:
    check_new = Check(i['date'], '', i['to'])

    to_ = i['to']
    if 'from' not in i:
        info_for_check.append({
            'date': check_new.format_date(),
            'description': i['description'],
            'from': 'Личный счет',
            'to': check_new.count_now(to_),
            'operationAmount': i['operationAmount']['amount'] + ' ' + i['operationAmount']['currency']['name']})
    else:
        from_ = i['from']
        to_ = i['to']
        info_for_check.append({
            'date': check_new.format_date(),
            'description': i['description'],
            'from': check_new.count_now(from_),
            'to': check_new.count_now(to_),
            'operationAmount': i['operationAmount']['amount'] + ' ' + i['operationAmount']['currency']['name']})

for info in info_for_check[::-1]:
    print(f"{info['date']} {info['description']}\n"
          f"{info['from']} -> {info['to']}\n{info['operationAmount']}\n")
