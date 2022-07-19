import os

from sklearn import datasets
import load_dataset_module
import csv

activity_features = datasets.ActivityFeatures()  ## calling activity features function to provide activity_feature dictionary


def mean(ActivityData) -> dict:
    """
    purpose: function for computing the mean of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with mean values of sensor readings
    """
    for keys in ActivityData: #every key is our user id
        mean_orientation_Xi = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation_Xi = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer_Xi = sum(ActivityData[keys][6:9]) / len(ActivityData[keys][6:9])
        mean_gyroscope_Xi = sum(ActivityData[keys][9:12]) / len(ActivityData[keys][9:12])
        mean_magnetic_Xi = sum(ActivityData[keys][12:15]) / len(ActivityData[keys][12:15])
        
        activity_features[keys].update({'id':keys, 'orMean':mean_orientation_Xi, 'rMean':mean_rotation_Xi, 'accMean':mean_accelerometer_Xi,
        'gMean':mean_gyroscope_Xi,'MagMean':mean_magnetic_Xi,'Activity':ActivityData[keys][-1]})
    return activity_features