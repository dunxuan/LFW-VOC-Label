# LFW-VOC-Label

LFW数据集标注后的VOC格式。一张图片只标注了一张人脸，人脸的范围中包含额头、耳朵等裸露的头部皮肤。


<!--more-->


## img_list.py

按照```/lfw/peopleDevTrain.txt```或```/lfw/peopleDevTest.txt```的顺序，将图片路径导出到```/lfw/img_list.txt```。

	img_dir_2_txt(is_train = True/False)

## jpg_2_dir.py

按照```/lfw/peopleDevTrain.txt```或```/lfw/peopleDevTest.txt```的分类，将图片分别放到```/lfw/train```根目录或```/lfw/test```根目录，不再放置到人名子目录。

	# __main__
	if __name__ == '__main__':
	img_dir_2_txt(is_train=True)
	copy_img_2_dir(is_train=True)
	img_dir_2_txt(is_train=False)
	copy_img_2_dir(is_train=False)

## 相关

使用[chaiwenda/ImgLabel](https://github.com/chaiwenda/ImgLabel)手动标注。

## License

[MIT license](https://github.com/dunxuan/LFW-VOC-Label/blob/main/LICENSE)


----------


<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">LFW-VOC-Label</span> 由 <a xmlns:cc="http://creativecommons.org/ns#" href="https://www.dunxuan.xyz/experience/LFW-VOC-Label.html" property="cc:attributionName" rel="cc:attributionURL">顿玄</a> 采用 <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">知识共享 署名-相同方式共享 4.0 国际 许可协议</a>进行许可。<br />基于<a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/dunxuan/LFW-VOC-Label" rel="dct:source">https://github.com/dunxuan/LFW-VOC-Label</a>上的作品创作。
