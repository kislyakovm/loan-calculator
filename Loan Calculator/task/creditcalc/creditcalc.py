import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('--type')

parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)

args = parser.parse_args()


def period_annuity():
    nominal_interest_rate = args.interest / (12 * 100)

    months = math.ceil(math.log(args.payment / (args.payment - nominal_interest_rate * args.principal),
                                (1 + nominal_interest_rate)))
    overpayment = months * args.payment - args.principal

    if months // 12 == 0:
        print(f'It will take {math.ceil(months)} months to repay this loan!')
    elif months % 12 == 0:
        print(f'It will take {int(months / 12)} years to repay this loan!')
    else:
        print(f'It will take {int(months // 12)} years and {math.ceil(months % 12)} months to repay this loan!')

    print(f'Overpayment = {overpayment}')


def payment_annuity():
    nominal_interest_rate = args.interest / (12 * 100)
    annuity_payment = args.principal * (nominal_interest_rate * (1 + nominal_interest_rate) ** args.periods) / \
                      ((1 + nominal_interest_rate) ** args.periods - 1)

    overpayment = args.periods * math.ceil(annuity_payment) - args.principal

    print(f'Your monthly payment = {math.ceil(annuity_payment)}!')
    print(f'Overpayment = {overpayment}')


def principal_annuity():
    nominal_interest_rate = args.interest / (12 * 100)
    principal = args.payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** args.periods) /
                                ((1 + nominal_interest_rate) ** args.periods - 1))

    overpayment = args.periods * args.payment - principal

    print(f'Your loan principal = {round(principal)}!')
    print(f'Overpayment = {math.ceil(overpayment)}')


def payments_diff():

    nominal_interest_rate = args.interest / (12 * 100)
    amount = 0

    for month in range(1, args.periods + 1):
        diff_payment = args.principal / args.periods + nominal_interest_rate * \
                       (args.principal - args.principal * (month - 1) / args.periods)
        print(f'Month {month}: payment is {math.ceil(diff_payment)}')

        amount += math.ceil(diff_payment)

    overpayment = amount - args.principal
    print()
    print(f'Overpayment = {math.ceil(overpayment)}')


if args.interest and args.interest > 0:
        if args.type == 'diff':
            if not args.payment:
                if args.principal and args.principal > 0 and args.periods and args.periods > 0:
                    payments_diff()
                else:
                    print('Incorrect parameters')
            else:
                print('Incorrect parameters')
        elif args.type == 'annuity':
            if args.periods and args.payment and args.periods > 0 and args.payment > 0:
                principal_annuity()
            elif args.periods and args.principal and args.periods > 0 and args.principal > 0:
                payment_annuity()
            elif args.payment and args.principal and args.payment > 0 and args.principal > 0:
                period_annuity()
            else:
                print('Incorrect parameters')
        else:
            print('Incorrect parameters')
else:
    print('Incorrect parameters')
