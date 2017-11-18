import csv
import os
try:
    import statistics
except:
    import statistics_standin_for_py2 as statistics


# Due to the way I have constructed the file hierachy I had to move the data_types file to
# the top level to enable this import, this kinda sucks but it is how imports and relative imports work
# in python. Sigh!!!


from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('------------------------------------')
    print('     REAL ESTATE MINING APP')
    print('------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    # with open(filename, 'r', encoding='utf-8') as fin:
    with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases

        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(row)
        #
        # header = fin.readline().strip()
        # print('Found header' + header)

# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('Found header' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)
#
#         print(lines[:5])


#    return []

# def get_price(p):
#    return p.price


def query_data(data): #list[Purchase]):
    # if data was sorted by price:
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # most expensive house
    high_purchase = data[-1]
    print("The most expensive house is ${:,} wiith {} beds and {} baths".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    # least expensive house
    low_purchase = data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price of a house
    prices = []
    for pur in data:
        prices.append(pur.price)

    ave_price = statistics.mean(prices)
    print("The avaerage home price is ${:}".format(int(ave_price)))

    # price of 2 bedroom houses
    prices = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)

    ave_price = statistics.mean(prices)
    print("The avaerage 2 bedroom home price is ${:}".format(int(ave_price)))


if __name__ == '__main__':
    main()
