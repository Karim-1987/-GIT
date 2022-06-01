from Cat import Cat

cats = [
    {
        "name": "Барон",
        "gender": "мальчик",
        "age": "2"

    },
    {
        "name": "Сэм",
        "gender": "мальчик",
        "age": "2"
    }
]
for item in cats:
    cat_items = Cat(name=item.get("name"),
                    gender=item.get("gender"),
                    age=item.get("age"))
    print(f"{cat_items.get_name()} {cat_items.get_gender()} {cat_items.get_age()}")
