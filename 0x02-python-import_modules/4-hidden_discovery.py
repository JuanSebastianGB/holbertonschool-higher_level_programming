#!/usr/bin/python3
if __name__ == "__main__":
    """[Printing all file names]
    """
    import hidden_4
    files = dir(hidden_4)  # Accesing to all propertys of the file hiddden_4
    for file in files:  # Handeling like an object
        if file[:2] != "__":  # printing all different of attributtes
            print(file)
