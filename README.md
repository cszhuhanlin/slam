This is the yolov3 person object detection framework which is based on the open-source keras yolov3 architecture.

The original project can be found in https://github.com/qqwweee/keras-yolo3. 


###############################################################

#files description

##############################################################

--code

----keras-yolo3-master

------logs

--------000

----------trained_weights_final_2.h5            #final weight

----------ep004-loss36.290-val_loss34.747.h5    #middle weight

------model_data

--------coco_classes.txt                        #coco data label class

--------voc_classes.txt                         #voc data label class

--------yolo_anchors.txt                        #yolov3 anchor boxes size

--------yolo_weights.h5                         #original yolov3 weight

------test

--------yolo3

----------__init__.py

----------model.py                              #yolov3 model

----------utils.py

--------1341846332.086502.png                   #object detection example of freiburg3

--------1341846337.150037.png                   #object detection example of freiburg3

--------halfsphere_bbox.txt                     #object detection result of freiburg3_walking_halfsphere data

--------show_pic.py                             #use the model to detect the freiburg3 example

--------xyz_bbox.txt                            #object detection result of freiburg3_walking_xyz data

--------yolo_copy.py                            #yolo_img_eval.py  invoking function

--------yolo_img_eval.py                        #detect the object in freiburg3_walking_halfsphere and freiburg3_walking_xyz
data

------yolo3

--------__init__.py

--------model.py                                #yolov3 model

--------utils.py

------coco_train.txt                            #coco 2014 train data labels

------yolo_anchors.txt                          #yolov3 anchor boxes size

------yolo.py                                   #yolov3 detect object and function

------yolov3.cfg                                #yolov3 parameter

------2012_person_val.txt                       #voc 2012 validation data labels

------2012_person_train.txt                     #voc 2012 train data labels

------kmeans.py                                 #k-means algorithm to get the suitable anchor boxes

------voc_annotation.py                         #get voc 2012 labels from original annotation format

------coco_voc.txt                              #voc 2012 and coco 2014 labels

------coco_val.txt                              #coco 2014 validation labels

------convert.py

------darknet53.cfg                             #darknet parameters

------train.py                                  #train the yolov3 model

------coco_annotation.py                        #get coco 2014 labels from original annotation format

--data

----annotations

------person_keypoints_train2014.json           #coco 2014 original labels(person train)

------person_keypoints_val2014.json             #coco 2014 original labels(person validation)

----rgbd_dataset_freiburg3_walking_halfsphere

------rgb                                       #freiburg3_walking_halfsphere rgb images

------depth                                     #freiburg3_walking_halfsphere depth images

------accelerometer.txt

------depth.txt

------groundtruth.txt

------rgb.txt

----rgbd_dataset_freiburg3_walking_xyz

------rgb                                       #freiburg3_walking_halfsphere rgb images

------depth                                     #freiburg3_walking_halfsphere depth images

------accelerometer.txt

------depth.txt

------groundtruth.txt

------rgb.txt

----train2014                                   #coco 2014 images

----VOCdevkit

------VOC2012

--------Annotations                             #all voc xml labels

--------ImageSets

----------main

------------person_trainval.txt                 #voc person image IDs

------------person_train.txt                    #voc person train imgae IDs

------------person_val.txt                      #voc person validation image IDs

--------JPEGImages                              #voc images

--------SegmentationClass

--------SegmentationObject

################################################################

#code opration method

################################################################

1.  run "voc_annotation.py"  #get voc person labels, store them in  "2012_person_val.txt" and "2012_person_train.txt".
    run "coco_annotation.py"  #get coco person labels, store them in  "coco_train.txt" and "coco_val.txt".

2.  convert the "2012_person_val.txt" and the "coco_train.txt", store them in "coco_voc.txt".

3.  run "k-means.py" to get the suitable anchor boxes size, which will use "coco_voc.txt".

3.  run "train.py" to train the model. #"train.py" will use "trained_weights.h5", "yolo3","coco_voc.txt","voc_classes.txt","yolo_anchors.txt" and store the new weights

4.  run "test/yolo_img_eval.py", use the trained model to detect the freiburg3 dataset and store the result in "halfsphere_bbox.txt" and "halfsphere_bbox.txt".
    run "test/show_pic.py" to show object detection example in  freiburg3 dataset.


############################

ps: The data file does not have the image data,
    you can download the    "VOCtrainval_11-May-2012.tar" from voc webpage,
                            "annotations_trainval2014.zip" and "train2014.zip" in coco web page,
                            "rgbd_dataset_freiburg3_walking_halfsphere.tgz" and "rgbd_dataset_freiburg3_walking_xyz.tgz" from freiburg3 web page.
    Then un compress them in the "data" folder.

