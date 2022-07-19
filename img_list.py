import os

LFWDIR = os.path.dirname(os.path.abspath(__file__)) + r'/LFW'


# 导出数据集中图片路径
def img_dir_2_txt(is_train):
    dev_is_train = r'/peopleDevTrain.txt' if is_train is True else r'/peopleDevTest.txt'
    dev_name = open(LFWDIR + dev_is_train, 'r')
    txt = open(LFWDIR + r'/img_list.txt', "w")
    txt.truncate(0)
    dev_name.readline()

    for line in dev_name:
        line = line.strip('\n')
        i = int(line.split('\t')[1])
        while i > 0:
            name = line.split('\t')[0]
            list_train_test = name + '_{:04d}'.format(i) + '.jpg' + ' ' + name + '_{:04d}'.format(i) + '.xml' + '\n' \
                if is_train is True else name + '_{:04d}'.format(i) + '.jpg' + '\n'
            txt.writelines(list_train_test)
            i -= 1


# __main__
if __name__ == '__main__':
    img_dir_2_txt(is_train=True)
    print('img_list.txt done')