import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file.readlines():
            if line != "":
                all_data.append(line)


# start = datetime.datetime.now()
#
# filenames = [f'file {number}.txt' for number in range(1, 5)]
# for item in filenames:
#     read_info(item)
#
# end = datetime.datetime.now()
#
# print(end-start)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        filenames = []
        for number in range(1, 5):
            filenames.append(f'file {number}.txt')
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end-start)




