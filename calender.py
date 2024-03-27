# In class asssignment
def days2Months():
    z = input('Enter the month: ')
    months = [('January' or 'january'), ('February' or 'february'), ('March' or 'march'), ('April' or 'april'), ('May'), ('June' or 'june'), ('August'), ('September' or 'september'), ('October'), ('November' or 'november'), ('December')]
    days = [31, 28, 30,]
    if days2Months(2):
        print(f'February has {days[2]} days, unless its an leap year.')
    elif ('April' or 'april') or ('June' or 'june') or ('September' or 'september') or ('November' or 'november'):
        print(f'{z} has {days[30]} days.')
    else:
        print(f'{z} has {days[31]} days.')
days2Months()
