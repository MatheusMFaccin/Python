def delet(path):
    import os
    try:
        os.remove(path)

    except FileNotFoundError:
        print("file not found :(") 