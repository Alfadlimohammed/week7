names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print(names)
if __name__ == '__main__':
    sentence = "this is a sentence containing some letters"
    unique_letters = {x for x in sentence}
    print(unique_letters)
if __name__ == '__main__':
    names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
    input_name = input("Enter a name: ")
    if input_name not in names:
        print(f"{input_name} is not in the set of known names.")
    else:
        print(f"{input_name} is already in the set of known names.")
if __name__ == '__main__':
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    directors = {"Kelly", "Rupert", "Cyril", "Jon"}
    help(set)
if __name__ == '__main__':
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    staff = staff | {"Mark", "Ringo"}
    print(staff)
if __name__ == '__main__':
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    directors = {"Kelly", "Rupert", "Cyril", "Jon"}
    staff_directors = staff & directors
    print(staff_directors)
if __name__ == '__main__':
    external = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    directors = {"Kelly", "Rupert", "Cyril", "Jon"}
    external = directors - external
    print(external)
if __name__ == '__main__':
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    directors = {"Kelly", "Rupert", "Cyril", "Jon"}
    staff_or_external = directors ^ staff
    print(staff_or_external)
if __name__ == '__main__':
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    directors = {"Kelly", "Rupert", "Cyril", "Jon"}

    staff = staff.union({"Mark", "Ringo"})
    print("Union:", staff)
if __name__ == '__main__':
    vowels = set({"a", "e", "i"})
    vowels_update = vowels.update("u""o")
    print(vowels)
if __name__ == '__main__':
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}
    subset = managers <= staff
    print(subset)
if __name__ == '__main__':
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}
    proper_superset = managers > staff
    print(proper_superset)
if __name__ == '__main__':
    suits = frozenset({"heart", "club", "spade", "diamond"})
    answer = {"club", "diamond"} < suits
    print(answer)
if __name__ == '__main__':
    import math

    roots = {n: math.sqrt(n) for n in range(1, 26)}
if __name__ == '__main__':
    stock = {"apple": 10, "banana": 15, "orange": 11}
    stock["kiwi"] = 10
    print("Apple stock level is", stock)
if __name__ == '__main__':
    stock = {"apple": 10, "banana": 15, "orange": 11}
    if "apple" in stock:
        print("Apples have a stock level is", stock["apple"])
if __name__ == '__main__':
    stock = {"apple": 10, "banana": 15, "orange": 11}
    stock = stock.popitem()
    print("Removed item:", stock)
if __name__ == '__main__':
    import math

    roots = {n: math.sqrt(n) for n in range(1, 26)}
    for num, sqrt in roots.items():
        print(f"The square root of {num} is {sqrt}")