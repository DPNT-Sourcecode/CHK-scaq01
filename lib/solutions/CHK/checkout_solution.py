
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            'A' : 50,
            'B' : 30,
            'C' : 20,
            'D' : 15,
            'E' : 40,
            'F' : 10,
            'G' : 20,
            'H' : 10,
            'I' : 35,
            'J' : 60,
            'K' : 80,
            'L' : 90,
            'M' : 15,
            'N' : 40,
            'O' : 10,
            'P' : 50,
            'Q' : 30,
            'R' : 50,
            'S' : 30,
            'T' : 20,
            'U' : 40,
            'V' : 50,
            'W' : 20,
            'X' : 90,
            'Y' : 10,
            'Z' : 50
        }

        multi_offers = {
            'A':[(5,200), (3,130)],
            'B':[(2,45)],
            'H':[(10,80), (5,45)],
            'K':[(2,150)],
            'P':[(5,200)],
            'Q':[(3,80)],
            'V':[(3,130), (2,90)],
        }

        same_ch_free = {
            'F':2,
            'U':3
        }

        item_count = {}
        for ch in skus:
            if ch not in prices:
                return -1
            item_count[ch] = item_count.get(ch, 0) + 1

        if 'E' in item_count:
            free_b_from_e = (item_count['E'] // 2)
            if free_b_from_e > 0:
                current_b = item_count.get('B',0)
                item_count['B'] = max(0, current_b - free_b_from_e)

        total = 0
        for item, count in item_count.items():
            if item == 'F':
                payable_f = count - (count // 3)
                total += payable_f * prices['F']
            elif item in offers:
                for offer_qty, offer_price in offers[item]:
                    special_sets = count // offer_qty
                    count -= special_sets * offer_qty
                    total += offer_price * special_sets
                total += count*prices[item]
            else:
                total += count * prices[item]

        return total
