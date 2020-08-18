import os

DATA_FOLDER = 'Data'
TRAIN_CSV = os.path.join(DATA_FOLDER, 'train.csv')
VAL_CSV = os.path.join(DATA_FOLDER, 'test.csv')

DATA_FOLDER2 = 'models'
SAVED_ESTIMATOR = os.path.join(DATA_FOLDER2, 'SVC.pickle')