def convert(number):
    data = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
    }

    result = [v for k, v in data.items() if number % k == 0]

    return "".join(result) or str(number)
