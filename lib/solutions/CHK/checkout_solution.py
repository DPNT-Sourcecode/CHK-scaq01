
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            'A' : 50,
            'B' : 30,
            'C' : 20,
            'D' : 15,
        }

        offers = {
            'A':(3,130)
            'B':(2,45)
        }

        if skus == "":
            return 0

        for ch in skus:
            if ch not in prices:
                return -1

        from collections 


