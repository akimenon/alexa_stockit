import utils


def createportfolio(portfolioname):
    """
    This function creates a collection with name passed
    in portfolioname
    :param portfolioname:

    """
    # get DB connection
    db = utils.getDBConnection()

    # create table
    db.create_collection(portfolioname + "_pf")


def insertportfolio(tickername, purchasedqty, purchaseprice, collectioname):
    """
    This fucntion inserts data into portfolio
    :param tickername:
    :param purchasedqty:
    :param purchaseprice:
    :param collectioname:
    :return:
    """
    # get DB connection
    db = utils.getDBConnection()
    db[collectioname].insert(
        {
            "ticker": tickername,
            "qty": purchasedqty,
            "price": purchaseprice
        }
    )


def createwishlist(wishlist):
    """
    This function create a collection for wishlist
    :param wishlist:
    :return:
    """
    # get DB connection
    db = utils.getDBConnection()

    # create table
    db.create_collection(wishlist + "_wl")


def insertwishlist(tickername, wishlist):
    """
    this functions inserts data to wishlist collection
    :param tickername:
    :param wishlist:
    :return:
    """
    # get DB connection
    db = utils.getDBConnection()
    db[wishlist].insert(
        {
            "ticker": tickername
        }
    )

def dialogportfolio():
    pass
