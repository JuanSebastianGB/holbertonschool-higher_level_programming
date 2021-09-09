#!/usr/bin/python3
if __name__ == "__main__":
    """[Printing all file names]
    """
    import hidden_4
    for text in dir(hidden_4):  # Handeling like an object
        if text[:2] != "__":  # printing all different of attributtes
            print("{}".format(text))
