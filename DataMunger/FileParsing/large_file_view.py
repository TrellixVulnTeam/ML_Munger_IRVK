def get_small_view(filename, num_characters):
    lines = []
    count = 0
    with open(filename, 'r') as file:
        text = file.read(num_characters)
        print(text)
    # return lines

# filename = "dlib.json"

# print(get_small_view(filename, 5000))