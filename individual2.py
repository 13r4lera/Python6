def format_all(template, *args, **kwargs):
    result = []

    for arg in args:
        res_str = template.format(arg, **kwargs)
        result.append(res_str)

    return result

if __name__ == '__main__':
    print(format_all("User: {name}, ID: {}", 12, 34, name="Alice"))
    print(format_all("User: {name}, ID: {}, his pet: {pet}", 1, 2, 3, 4, 5,  name="vasya", pet="petya"))