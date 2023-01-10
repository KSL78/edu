import os

file_dir = '../trans'


def main():
    i = 0
    file_names = os.listdir(file_dir)
    for file_name in file_names:
        src = os.path.join(file_dir, file_name)
        dst = os.path.join(file_dir, (str(i).zfill(4) + '.jpg'))
        os.rename(src, dst)
        i += 1
    print(i)


if __name__ == '__main__':
    main()