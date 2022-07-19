import os
import shutil


THISDIR = os.path.dirname(os.path.abspath(__file__))


# 导出数据集中图片路径
def img_dir_2_txt(is_train):
    txt_is_train = r'\train.txt' if is_train is True else r'\test.txt'
    dev_is_train = r'\peopleDevTrain.txt' if is_train is True else r'\peopleDevTest.txt'
    dev_name = open(THISDIR + dev_is_train, 'r').readlines()
    count = int(open(THISDIR + dev_is_train, 'r').readlines()[0])
    txt = open(THISDIR + txt_is_train, "w")
    txt.truncate(0)

    for root, dirs, files in os.walk(THISDIR + r'\lfw'):
        dir_name = root[len(THISDIR + r'\lfw') + 1:]
        i = count
        while dir_name != dev_name[i].split('\t')[0] and i > 0:
            i -= 1
        if i != 0:
            for file in files:
                txt.writelines(os.path.join(root, file) + "\n")

    print(txt_is_train[1:] + ' done')


# 将txt中路径的文件复制到对应文件夹中
def copy_img_2_dir(is_train):
    txt_is_train = r'\train.txt' if is_train is True else r'\test.txt'
    dir_is_train = r'\train' if is_train is True else r'\test'
    txt = open(THISDIR + txt_is_train, 'r')

    for line in txt:
        img_path = line.strip()
        # people_name = img_path[len(LFWDIR + r'\LFW\images') + 1:].split('\\')[0]
        dir_path = THISDIR + dir_is_train # + '\\' + people_name
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        shutil.copy(img_path, dir_path)

    print(dir_is_train[1:] + ' done')


# __main__
if __name__ == '__main__':
    img_dir_2_txt(is_train=True)
    copy_img_2_dir(is_train=True)
    img_dir_2_txt(is_train=False)
    copy_img_2_dir(is_train=False)