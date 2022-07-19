import os
from typing import Dict

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

def variance(ActivityData) -> dict:
    """
    purpose: function for computig the variance of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with variance values of sensor readings
    """
    for keys in ActivityData:
        mean_orientation_Xi = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation_Xi = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer_Xi = sum(ActivityData[keys][6:9]) / len(ActivityData[keys][6:9])
        mean_gyroscope_Xi = sum(ActivityData[keys][9:12]) / len(ActivityData[keys][9:12])
        mean_magnetic_Xi = sum(ActivityData[keys][12:15]) / len(ActivityData[keys][12:15]) 
        
        #looping through the items in each respective sensor and removing them from the mean calculated before to get variance solution
        var_orientation = sum([(x - mean_orientation_Xi) **2 for x in ActivityData[keys][:3]]) / len(ActivityData[keys][:3])
        var_rotation = sum([(x - mean_rotation_Xi) **2 for x in ActivityData[keys][3:6]]) / len(ActivityData[keys][3:6])
        var_accelerometer = sum([(x - mean_accelerometer_Xi) **2 for x in ActivityData[keys][6:9]]) / len(ActivityData[keys][6:9])
        var_gyroscope = sum([(x - mean_gyroscope_Xi) **2 for x in ActivityData[keys][9:12]]) / len(ActivityData[keys][9:12])
        var_magnetic = sum([(x - mean_magnetic_Xi) **2 for x in ActivityData[keys][12:15]]) / len(ActivityData[keys][12:15])
        
        activity_features[keys].update({'id':keys, 'orVar':var_orientation, 'rVar':var_rotation, 'accVar':var_accelerometer,
        'gVar':var_gyroscope,'MagVar':var_magnetic,'Activity':ActivityData[keys][-1]})
    return activity_features


def std_deviation(ActivityData) -> Dict:
    """
    purpose:function for computing the standard deviation of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with std_Deviation values of each sensor readings
    """

    for keys in ActivityData:    
        mean_orientation_Xi = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation_Xi = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer_Xi = sum(ActivityData[keys][6:9]) / len(ActivityData[keys][6:9])
        mean_gyroscope_Xi = sum(ActivityData[keys][9:12]) / len(ActivityData[keys][9:12])
        mean_magnetic_Xi = sum(ActivityData[keys][12:15]) / len(ActivityData[keys][12:15]) 
        
        std_orientation = (sum([(x - mean_orientation_Xi) **2 for x in ActivityData[keys][:3]]) / len(ActivityData[keys][:3])) ** 0.5
        std_rotation = (sum([(x - mean_rotation_Xi) **2 for x in ActivityData[keys][3:6]]) / len(ActivityData[keys][3:6])) ** 0.5
        std_accelerometer = (sum([(x - mean_accelerometer_Xi) **2 for x in ActivityData[keys][6:9]]) / len(ActivityData[keys][6:9])) ** 0.5
        std_gyroscope = (sum([(x - mean_gyroscope_Xi) **2 for x in ActivityData[keys][9:12]]) / len(ActivityData[keys][9:12])) ** 0.5
        std_magnetic = (sum([(x - mean_magnetic_Xi) **2 for x in ActivityData[keys][12:15]]) / len(ActivityData[keys][12:15])) ** 0.5
        
        activity_features[keys].update({'id':keys, 'orStd':std_orientation, 'rStd':std_rotation, 'accStd':std_accelerometer,
        'gStd':std_gyroscope,'MagStd':std_magnetic,'Activity':ActivityData[keys][-1]})
    return activity_features


def root_ms(ActivityData) -> Dict:
    """
    purpose: function for computing the root mean square of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with root mean square of each sensor readings
    """
    for keys in ActivityData:
        rms_orientation = sum([x**2 for x in ActivityData[keys][:3]]) / len(ActivityData[keys][:3])
        rms_rotation = sum([x**2 for x in ActivityData[keys][3:6]]) / len(ActivityData[keys][3:6])
        rms_accelerometer = sum([x**2 for x in ActivityData[keys][6:9]]) / len(ActivityData[keys][6:9])
        rms_gyroscope = sum([x**2 for x in ActivityData[keys][9:12]]) / len(ActivityData[keys][9:12])
        rms_magnetic = sum([x**2 for x in ActivityData[keys][12:15]]) / len(ActivityData[keys][12:15])
        
        activity_features[keys].update({'id':keys, 'orRms':rms_orientation, 'rRms':rms_rotation, 'accRms':rms_accelerometer,
        'gRms':rms_gyroscope,'MagRms':rms_magnetic,'Activity':ActivityData[keys][-1]})
    return activity_features


def sum_squares(ActivityData) -> dict:
    """
    purpose: function for computing the sum of square of each sensor readings'
    Argument: ActivityData
    Return: activity_features populated with root mean square of each sensor readings
    """
    for keys in ActivityData:
        mean_orientation_Xi = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation_Xi = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer_Xi = sum(ActivityData[keys][6:9]) / len(ActivityData[keys][6:9])
        mean_gyroscope_Xi = sum(ActivityData[keys][9:12]) / len(ActivityData[keys][9:12])
        mean_magnetic_Xi = sum(ActivityData[keys][12:15]) / len(ActivityData[keys][12:15]) 
        
        sos_orientation = sum([(x - mean_orientation_Xi) **2 for x in ActivityData[keys][:3]])
        sos_rotation = sum([(x - mean_rotation_Xi) **2 for x in ActivityData[keys][3:6]])
        sos_accelerometer = sum([(x - mean_accelerometer_Xi) **2 for x in ActivityData[keys][6:9]]) 
        sos_gyroscope = sum([(x - mean_gyroscope_Xi) **2 for x in ActivityData[keys][9:12]])
        sos_magnetic = sum([(x - mean_magnetic_Xi) **2 for x in ActivityData[keys][12:15]])
        
        activity_features[keys].update({'id':keys, 'orSos':sos_orientation, 'rSos':sos_rotation, 'accSos':sos_accelerometer,
        'gSos':sos_gyroscope,'MagSos':sos_magnetic,'Activity':ActivityData[keys][-1]})
    return activity_features

def median(ActivityData) -> dict:
    """
    purpose: function for computing the median of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with root mean square of each sensor readings
    """
    # since our no of observations is an odd number
    for keys in ActivityData:
        #sorting respective featues in an ascending order
        ActivityData[keys][:3].sort() #orientation
        ActivityData[keys][3:6].sort() #rotation
        ActivityData[keys][6:9].sort() #accelerometer
        ActivityData[keys][9:12].sort() #gyroscope
        ActivityData[keys][12:15].sort() #magnetic

        med_orientation = ActivityData[keys][:3] [int(((len(ActivityData[keys][:3]) + 1) / 2)) -1  ]
        med_rotation = ActivityData[keys][3:6] [int(((len(ActivityData[keys][3:6]) + 1) / 2)) -1 ]
        med_accelerometer = ActivityData[keys][6:9] [int(((len(ActivityData[keys][6:9]) + 1) / 2)) -1 ]
        med_gyroscope = ActivityData[keys][9:12] [int(((len(ActivityData[keys][9:12]) + 1) / 2)) -1 ]
        med_magnetic = ActivityData[keys][12:15] [int(((len(ActivityData[keys][12:15]) + 1) / 2)) -1 ]
        
        activity_features[keys].update({'id':keys, 'orMedian':med_orientation, 'rMedian':med_rotation, 'accMedian':med_accelerometer,
        'gMedian':med_gyroscope,'MagMedian':med_magnetic,'Activity':ActivityData[keys][-1]})
    return activity_features

