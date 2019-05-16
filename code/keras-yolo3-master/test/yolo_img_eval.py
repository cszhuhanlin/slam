
# -*- coding=utf-8 -*-

import sys
import argparse
#from yolo import YOLO, detect_video
from yolo_copy import YOLO, detect_video
from PIL import Image
import glob
import json
import os
from yolo3.utils import letterbox_image
import numpy as np
from timeit import default_timer as timer


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
            np.int16, np.int32, np.int64, np.uint8,
            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32,
            np.float64)):
            return float(obj)
        elif isinstance(obj,(np.ndarray,)): #### This is the fix
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


'''def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()'''


def detect_img(yolo_copy):
    #path = "../../../data/rgbd_dataset_freiburg3_walking_halfsphere/rgb/*.png"
    path = "../../../data/rgbd_dataset_freiburg3_walking_xyz/rgb/*.png"
    #path = "test_image/image/*.jpg"
    outdir = "../../../data/rgbd_dataset_freiburg3_walking_halfsphere/rgb/dataout/"
    #outdir = "test_image/"

    imgs_dict = {}
    image_name_dict = {}
    bbox_all=[]
    for jpgfile in glob.glob(path):

        print(jpgfile)
        list_file.write(jpgfile[-21:]+' ')

        image_name = jpgfile.split('/')[-1]
        img = Image.open(jpgfile)
        #img = yolo.detect_image(img)
        #boxes, scores, classes = yolo_copy.image_eval(img)
        image_list,bbox_out = yolo_copy.image_eval(img,list_file)

        image_name_dict[image_name] = image_list
        #print(image_list)
        list_file.write('\n')

        # print('image: {}'.format(i))
        # print('out_classes: {}'.format(classes))
        # print('out_scores: {}'.format(scores))
        # print('out_boxes: {}'.format(boxes))


        #print(img)
        #img.save("../traffic-data/dataout/"+i, 'jpeg')
        #img.save(outdir + i, 'jpeg')
        #img.save(os.path.join(outdir, os.path.basename(jpgfile)))
        #print('-'*50)

    imgs_dict["imgs"] = image_name_dict
    #print(imgs_dict)
    '''
    dumped = json.dumps(imgs_dict, cls=NumpyEncoder)

    with open(outdir + "image_test_result.json", 'w') as f:
        json.dump(dumped, f)
    '''
    #image_result = open(outdir + "image_test_result.json", "w", encoding='utf-8').write(json.dumps(imgs_dict))

    yolo_copy.close_session()

FLAGS = None

if __name__ == '__main__':
    list_file = open('xyz_bbox.txt', 'w')
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default='2.jpg', action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./path2your_video',
        help = "Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help = "[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
    elif "input" in FLAGS:
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
