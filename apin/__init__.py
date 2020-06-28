from apin.runner import Runner


def run(file):
    """run the cases"""
    return Runner().run(file)


if __name__ == '__main__':
    run('../samples/test_ref.yml')