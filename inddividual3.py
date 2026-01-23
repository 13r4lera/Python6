def to_tuple(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.append(to_tuple(item))
        else:
            result.append(item)

    return tuple(result)


if __name__ == "__main__":
    print(to_tuple([1, [2, [3, 4]]]))
    print(to_tuple([[[[1, 2], 3], 4], 5]))
