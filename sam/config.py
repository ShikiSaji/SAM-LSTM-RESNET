#########################################################################
# RESOURCES URL														    #
#########################################################################
DATASET_IMAGES_URL = (
    "https://github.com/SheikSadi/SAM-LSTM-RESNET/releases/download/1.0.0/images.zip"
)
DATASET_MAPS_URL = (
    "https://github.com/SheikSadi/SAM-LSTM-RESNET/releases/download/1.0.0/maps.zip"
)
DATASET_FIXS_URL = (
    "https://github.com/SheikSadi/SAM-LSTM-RESNET/releases/download/1.0.0/fixations.zip"
)
SAM_RESNET_SALICON_2017_WEIGHTS = "https://github.com/SheikSadi/SAM-LSTM-RESNET/releases/download/1.0.0/sam-resnet_salicon_weights.pkl"
TH_WEIGHTS_PATH_NO_TOP = "https://github.com/SheikSadi/SAM-LSTM-RESNET/releases/download/1.0.0/resnet50_weights_th_dim_ordering_th_kernels_notop.h5"
#########################################################################
# MODEL PARAMETERS														#
#########################################################################
# batch size
b_s = 1
# number of rows of input images
shape_r = 240
# number of cols of input images
shape_c = 320
# number of rows of downsampled maps
shape_r_gt = 30
# number of cols of downsampled maps
shape_c_gt = 40
# number of rows of model outputs
shape_r_out = 480
# number of cols of model outputs
shape_c_out = 640
# final upsampling factor
upsampling_factor = 16
# number of epochs
nb_epoch = 10
# number of timestep
nb_timestep = 4
# number of learned priors
nb_gaussian = 16
# Percentage of the total attention to retain
retained_attention = 0.5
# aspect ratio of the cropped image
aspect_ratio = 1.4444444444444444  # 260/180

#########################################################################
# TRAINING SETTINGS										            	#
#########################################################################
# path of training images
imgs_train_path = "/mnt/d/smart-cropping/salicon_dataset_2017/images/train/"
# path of training maps
maps_train_path = "/mnt/d/smart-cropping/salicon_dataset_2017/maps/train/"
# path of training fixation maps
fixs_train_path = "/mnt/d/smart-cropping/salicon_dataset_2017/fixations/train/"
# path of validation images
imgs_val_path = "/mnt/d/smart-cropping/salicon_dataset_2017/images/val/"
# path of validation maps
maps_val_path = "/mnt/d/smart-cropping/salicon_dataset_2017/maps/val/"
# path of validation fixation maps
fixs_val_path = "/mnt/d/smart-cropping/salicon_dataset_2017/fixations/val/"
