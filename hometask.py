# написати функцію якам приймає рядок і повертає словник у якому
# ключами є всі символи, які зустрічаються в цьому рядку, а значення - відповідні
# вірогідності зустріти цей символ в цьому рядку.
# № код повинен бути структурований за допомогою конструкції if name == "__main__":,
# всі аргументи і значення що функція повертає повинні бути типізовані, функція має рядок документації


def get_symbol_dict(string: str) -> dict:
    """
    Обчислити ймовірність появи кожного символу у заданому рядку.
    """
    clear_string: str = string.replace(" ", "").lower()
    size: int = len(clear_string)

    result: dict = {
        i: round(clear_string.count(i) / size, 2) for i in set(clear_string)
    }

    return result


if __name__ == "__main__":
    print(get_symbol_dict("Hello world"))
