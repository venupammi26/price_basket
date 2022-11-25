import argparse
import sys


def getParser(argv):
    parser = argparse.ArgumentParser(description='price basket parser')

    parser.add_argument('-soup', action="store", dest="soup_qty", default=0, required=False)
    parser.add_argument('-bread', action="store", dest="bread_qty", default=0, required=False)
    parser.add_argument('-milk', action="store", dest="milk_qty", default=0, required=False)
    parser.add_argument('-apples', action="store", dest="apples_qty", default=0, required=False)

    return parser

def main(argv):
    parser = getParser(argv)
    args = parser.parse_args(argv[1:])

    Soup = 0.65 # 65p per tin
    Bread = 0.80 #80p per loaf
    Milk = 1.30 #  £1.30 per bottle.
    Apples = 1.00 # £1.00 per bag.

    bread_disc = 0 # buy 2 tins of soup and get a loaf of bread for half price for only one loaf of one bread
    Subtotal = Soup* int(args.soup_qty) +  Bread * int(args.bread_qty) + Milk * int(args.milk_qty) + Apples * int(args.apples_qty)

    print("Subtotal: £%.2f" % Subtotal)
    #Apples have a 10% discount off their normal price this week.
    if int(args.apples_qty) != 0:
        print("Apples 10% off: 10p")
        disc = Apples * 10/100
        Apples = 1.00 - disc
    #Buy 2 tins of soup and get a loaf of bread for half price.
    if int(args.soup_qty) >= 2:
        print("Bought 2 soup tins got a loaf of bread for half price {}p".format(int(Bread*100/2)))
        no_of_loaf_of_bread_at_disc = int(args.soup_qty) // 2
        bread_disc= Bread * no_of_loaf_of_bread_at_disc / 2
    total = Soup* int(args.soup_qty) +  Bread * int(args.bread_qty) + Milk * int(args.milk_qty) + Apples * int(args.apples_qty)
    total = total - bread_disc
    print("total: £%.2f" % total)

main( sys.argv )



# python PriceBasket.py -bread=2 -soup=4
