class textiles:
    def __init__(mani,brand,cost):
        mani.brand=brand
        mani.cost=cost

    def textiles_details(mani,size:int):
        print(f"This is {mani.brand} textiles and is cost of {mani.cost} and has a size of {size}")

textiles1=textiles(brand= "ooka kaka",cost="2000")
textiles2=textiles(brand= "woodland",cost="2500")


textiles1.textiles_details(42)
textiles2.textiles_details(46)
