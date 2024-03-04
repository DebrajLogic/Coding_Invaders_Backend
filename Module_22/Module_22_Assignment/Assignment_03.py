
playDuration = int(input('Enter play duration (in hrs): '))
subscribers = int(input('Enter no. of Subscribers: '))


def calculatePay(playDuration, subscribers):
    #  $40 initial pay to start
    initial_pay = 10
    bonus = 0

    #  More than 100 hours playtime and 1 Lakh subscribers - 20$
    if (playDuration > 100 and subscribers >= 1_00_000):
        bonus = 20

    #  More than 500 hours playtime and 5 lakhs subscribers - 30$
    if (playDuration > 500 and subscribers >= 5_00_000):
        bonus = 30

    #  More than 1000 hours playtime and 1 mil subscribers - 40$
    if (playDuration > 1000 and subscribers >= 1_000_000):
        bonus = 40

    return initial_pay + bonus


paycheck = calculatePay(playDuration, subscribers)

print(f"Congrats! you are paid ${
      paycheck} Based on your play duration and subscribers count")
