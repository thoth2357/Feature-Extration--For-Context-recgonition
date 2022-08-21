#import file handling libraries
import csv

#open and read dataset into dictreader
file = open('activity_context_tracking_data.csv', 'r', encoding='utf-8')
file_to_dict = csv.DictReader(file)


def ActivityData() -> dict:
    """
        purpose: provides the functionality of the reading the datsets and populating the dictionary from it
        Argument: None
        Return: ActivityData Dictionary
    """
    activity_data = {}
    for rows in file_to_dict:
        activity_data[rows['_id']] = [int(rows['orX']), int(rows['orY']),int(rows['orZ']),float(rows['rX']),float(rows['rY']),float(rows['rZ']),float(rows['accX']),float(rows['accY']),float(rows['accZ']),
        float(rows['gX']),float(rows['gY']),float(rows['gZ']),float(rows['orX']),float(rows['mX']),float(rows['mY']),float(rows['mZ']),rows['activity']]
    return activity_data


def ActivityFeatures() -> dict:
    """
        purpose: creates the activity features dictionary and populates with only user ids for now as keys and empty dictionary as value
        Argument: None
        Return: ActivityFeatures Dictionary
    """
    activity_features = {}
    for rows in file_to_dict:
        activity_features[rows['_id']] = {}
    return activity_features


