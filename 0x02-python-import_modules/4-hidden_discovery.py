#!/usr/bin/python3
if __name__ == "__main__":
    """[working whith file like an object]
    """
    import hidden_4
    for text in dir(hidden_4):
        if text[:2] != "__":
            print("{:s}".format(text))
