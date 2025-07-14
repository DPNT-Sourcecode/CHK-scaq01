
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            'A' : 50,
            'B' : 30,
            'C' : 20,
            'D' : 15,
            'E' : 40
        }

        offers = {
            'A':[(5,200), (3,130)],
            'B':[(2,45)]
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
            if item in offers:
                for offer_qty, offer_price in offers[item]:
                    special_sets = count // offer_qty
                    count -= special_sets * offer_qty
                    total += offer_price * special_sets

                total += special_sets * offer_price + remaining * prices[item]
            else:
                total += count * prices[item]

        return total

