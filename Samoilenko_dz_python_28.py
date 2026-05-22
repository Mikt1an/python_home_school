# # 1
#
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

iterator = weekly_schedule.items().__iter__()

while True:
    us_inp = input("Enter: ")
    if us_inp == "q":
        break
    try:
        day, task = next(iterator)
        print(f"{day}: {', '.join(task)}")
    except StopIteration:
        iterator = weekly_schedule.items().__iter__()
        day, task = next(iterator)
        print(f"{day}: {', '.join(task)}")



# 2

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]
#
def product_geenerator(*args):
    """
        Generates product names in lowercase from multiple product lists.

        Args:
            *args: Variable number of lists containing product names.
        Returns:
            generator: A generator object that yields product names
            converted to lowercase one by one.

        Example:
            gen = product_geenerator(fruits, vegetables, dairy)
            next(gen)
            # apple
        """
    return (
        product.lower()
        for products_list in args
        for product in products_list
    )
#
gen = product_geenerator(fruits, vegetables, dairy)
while True:
    try:
        print(next(gen))
    except StopIteration as e:
        break
# Или через For
for item in gen:
    print(item)




# 3

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

def style_generator(*args):
    """
        Generates all possible clothing combinations in the format:
        "Clothe - Color - Size".

        Args:
            *args:
                args[0] -> list of clothes
                args[1] -> list of colors
                args[2] -> list of sizes
        Returns:
            generator: A generator object that yields clothing
            combinations one by one.

        Example:
            gen = style_generator(clothes, colors, sizes)
            next(gen)
            # T-shirt - Red - S
    """
    return (
        f"{cloth} - {color} - {size}"
        for cloth in args[0]
        for color in args[1]
        for size in args[2]
    )


st = style_generator(clothes, colors, sizes)
for gen in st:
    print(gen)




