import pickle

def save(object, name):
    with open('data/' + name, 'wb') as f:
        pickle.dump(object, f, pickle.HIGHEST_PROTOCOL)


def load(name):
    with open('data/' + name, 'rb') as f:
        return pickle.load(f)