import random

cards = ['As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks',
         'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh',
         'Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc',
         'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd']

deal = random.sample(cards, 8)  #chooses 8 cards from the deck to deal

h_first = deal.pop(0)
v_first = deal.pop(0)
h_second = deal.pop(0)
v_second = deal.pop(0)
h_third = deal.pop(0)
v_third = deal.pop(0)
h_fourth = deal.pop(0)
v_fourth = deal.pop(0)

hfirst_val

# def home(h_first, h_second, h_third, h_fourth):
#    score = h_first + h_second + h_third + h_fourth
#    if h_third == 'As' or h_third == 'Ah' or h_third == 'Ac' or h_third == 'Ad':
#        score += 10

print('   HOME  %s  %s  %s  %s' % (h_first, h_second, h_third, h_fourth))
print('VISITOR  %s  %s  %s  %s' % (v_first, v_second, v_third, v_fourth))


#ASSIGN VALUES
#TAKE BETS
#RUN A MILLION TIMES TO ESTABLISH HOUSE EDGE?