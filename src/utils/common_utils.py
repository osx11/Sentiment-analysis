from pickle import load, dump, HIGHEST_PROTOCOL


def load_object(file_name):
    with open(file_name, 'rb') as f:
        obj = load(f)

    return obj


def dump_object(obj, file_name):
    with open(file_name, 'wb') as f:
        dump(obj, f, HIGHEST_PROTOCOL)
