import os

def print_docs(dir):
    for root, dirs, files in os.walk(dir):
        print(f'Папка', root, 'содержит:')
        print(f'Директории: {", ".join([folder for folder in dirs])}')
        print(f'Файлы: {", ".join([file for file in files])}')
        print("-"*60)


print_docs("/home/user/PycharmProjects/pythonProject")
