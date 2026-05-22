# 1
from pymongo import MongoClient, errors
import dotenv
dotenv.load_dotenv()

class MONGO_DB():
    """
        MongoDB manager for product collection operations.
    """
    def __init__(self):
        self.__client = CLIENTMONGO
        self.__db = self.__client["ich_edit"]
        self.__collection = self.__db[
            "products_121225_anton_samoilenko"
        ]
        self.__client.admin.command("ping")
        print("Connection successful!")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.close()
        print("Connection closed")
        return False

    def clear_collection(self):
        print(f"Deleted documents")
        return self.__collection.delete_many({})

    def add_products(self, products):
        print(
            f"Added products: "
            f"{len(products)}"
        )
        return self.__collection.insert_many(products)

    def show_products(self):
        products = self.__collection.find()

        for number, product in enumerate(products, start=1):
            print(
                f"{number}. "
                f"{product['name']} | "
                f"price: ${product['price']} | "
                f"stock: {product['stock']}"
            )
        return products

    def increase_prices(self):
        result = self.__collection.update_many(
            {},
            {
                "$mul": {
                    "price": 1.2
                }
            }
        )
        print(
            f"Updated products: "
            f"{result.modified_count}"
        )
        return result





products_list = [
    {
        "name": "Laptop",
        "price": 1200,
        "stock": 5
    },
    {
        "name": "Mouse",
        "price": 25,
        "stock": 30
    },
    {
        "name": "Keyboard",
        "price": 75,
        "stock": 15
    }
]

try:
    mango = MONGO_DB()
    with mango as db:
        db.clear_collection()
        db.add_products(products_list)
        print("\nBefore update:\n")
        db.show_products()
        print("\nUpdating prices...\n")
        db.increase_prices()
        print("\nAfter update:\n")
        db.show_products()
except errors.ConnectionFailure:
    print("Errors connection MongoDB")
except errors.OperationFailure:
    print("Errors authentication MongoDB")
