import os
from load_dataset_module import ActivityFeatures
import csv

activity_features = (
    ActivityFeatures()
)  ## calling activity features function to provide activity_feature dictionary


def mean(ActivityData) -> dict:
    """
    purpose: function for computing the mean of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with mean values of sensor readings
    """
    for keys in ActivityData:  # every key is our user id
        mean_orientation = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer = sum(ActivityData[keys][6:9]) / len(ActivityData[keys][6:9])
        mean_gyroscope = sum(ActivityData[keys][9:12]) / len(ActivityData[keys][9:12])
        mean_magnetic = sum(ActivityData[keys][12:15]) / len(ActivityData[keys][12:15])

        activity_features[keys].update(
            {
                "id": keys,
                "orMean": mean_orientation,
                "rMean": mean_rotation,
                "accMean": mean_accelerometer,
                "gMean": mean_gyroscope,
                "MagMean": mean_magnetic,
                "Activity": ActivityData[keys][-1],
            }
        )
    return activity_features


def variance(ActivityData) -> dict:
    """
    purpose: function for computig the variance of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with variance values of sensor readings
    """
    for keys in ActivityData:
        mean_orientation = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer = sum(ActivityData[keys][6:9]) / len(
            ActivityData[keys][6:9]
        )
        mean_gyroscope = sum(ActivityData[keys][9:12]) / len(
            ActivityData[keys][9:12]
        )
        mean_magnetic = sum(ActivityData[keys][12:15]) / len(
            ActivityData[keys][12:15]
        )

        # looping through the items in each respective sensor and removing them from the mean calculated before to get variance solution
        variance_orientation = sum(
            [(x - mean_orientation) ** 2 for x in ActivityData[keys][:3]]
        ) / len(ActivityData[keys][:3])
        variance_rotation = sum(
            [(x - mean_rotation) ** 2 for x in ActivityData[keys][3:6]]
        ) / len(ActivityData[keys][3:6])
        variance_accelerometer = sum(
            [(x - mean_accelerometer) ** 2 for x in ActivityData[keys][6:9]]
        ) / len(ActivityData[keys][6:9])
        variance_gyroscope = sum(
            [(x - mean_gyroscope) ** 2 for x in ActivityData[keys][9:12]]
        ) / len(ActivityData[keys][9:12])
        variance_magnetic = sum(
            [(x - mean_magnetic) ** 2 for x in ActivityData[keys][12:15]]
        ) / len(ActivityData[keys][12:15])

        activity_features[keys].update(
            {
                "id": keys,
                "orVar": variance_orientation,
                "rVar": variance_rotation,
                "accVar": variance_accelerometer,
                "gVar": variance_gyroscope,
                "MagVar": variance_magnetic,
                "Activity": ActivityData[keys][-1],
            }
        )
    return activity_features


def standard_deviation(ActivityData) -> dict:
    """
    purpose:function for computing the standard deviation of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with standard_deviation values of each sensor readings
    """

    for keys in ActivityData:
        mean_orientation = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer = sum(ActivityData[keys][6:9]) / len(
            ActivityData[keys][6:9]
        )
        mean_gyroscope = sum(ActivityData[keys][9:12]) / len(
            ActivityData[keys][9:12]
        )
        mean_magnetic = sum(ActivityData[keys][12:15]) / len(
            ActivityData[keys][12:15]
        )

        std_orientation = (
            sum([(x - mean_orientation) ** 2 for x in ActivityData[keys][:3]])
            / len(ActivityData[keys][:3])
        ) ** 0.5
        std_rotation = (
            sum([(x - mean_rotation) ** 2 for x in ActivityData[keys][3:6]])
            / len(ActivityData[keys][3:6])
        ) ** 0.5
        std_accelerometer = (
            sum([(x - mean_accelerometer) ** 2 for x in ActivityData[keys][6:9]])
            / len(ActivityData[keys][6:9])
        ) ** 0.5
        std_gyroscope = (
            sum([(x - mean_gyroscope) ** 2 for x in ActivityData[keys][9:12]])
            / len(ActivityData[keys][9:12])
        ) ** 0.5
        std_magnetic = (
            sum([(x - mean_magnetic) ** 2 for x in ActivityData[keys][12:15]])
            / len(ActivityData[keys][12:15])
        ) ** 0.5

        activity_features[keys].update(
            {
                "id": keys,
                "orStd": std_orientation,
                "rStd": std_rotation,
                "accStd": std_accelerometer,
                "gStd": std_gyroscope,
                "MagStd": std_magnetic,
                "Activity": ActivityData[keys][-1],
            }
        )
    return activity_features


def root_mean_square(ActivityData) -> dict:
    """
    purpose: function for computing the root mean square of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with root mean square of each sensor readings
    """
    for keys in ActivityData:
        root_ms_orientation = sum([x ** 2 for x in ActivityData[keys][:3]]) / len(
            ActivityData[keys][:3]
        )
        root_ms_rotation = sum([x ** 2 for x in ActivityData[keys][3:6]]) / len(
            ActivityData[keys][3:6]
        )
        root_ms_accelerometer = sum([x ** 2 for x in ActivityData[keys][6:9]]) / len(
            ActivityData[keys][6:9]
        )
        root_ms_gyroscope = sum([x ** 2 for x in ActivityData[keys][9:12]]) / len(
            ActivityData[keys][9:12]
        )
        root_ms_magnetic = sum([x ** 2 for x in ActivityData[keys][12:15]]) / len(
            ActivityData[keys][12:15]
        )

        activity_features[keys].update(
            {
                "id": keys,
                "orRms": root_ms_orientation,
                "rRms": root_ms_rotation,
                "accRms": root_ms_accelerometer,
                "gRms": root_ms_gyroscope,
                "MagRms": root_ms_magnetic,
                "Activity": ActivityData[keys][-1],
            }
        )
    return activity_features


def sum_of_square(ActivityData) -> dict:
    """
    purpose: function for computing the sum of square of each sensor readings'
    Argument: ActivityData
    Return: activity_features populated with sum of square of each sensor readings
    """
    for keys in ActivityData:
        mean_orientation = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer = sum(ActivityData[keys][6:9]) / len(
            ActivityData[keys][6:9]
        )
        mean_gyroscope = sum(ActivityData[keys][9:12]) / len(
            ActivityData[keys][9:12]
        )
        mean_magnetic = sum(ActivityData[keys][12:15]) / len(
            ActivityData[keys][12:15]
        )

        sum_of_squares_orientation = sum(
            [(x - mean_orientation) ** 2 for x in ActivityData[keys][:3]]
        )
        sum_of_squares_rotation = sum(
            [(x - mean_rotation) ** 2 for x in ActivityData[keys][3:6]]
        )
        sum_of_squares_accelerometer = sum(
            [(x - mean_accelerometer) ** 2 for x in ActivityData[keys][6:9]]
        )
        sum_of_squares_gyroscope = sum(
            [(x - mean_gyroscope) ** 2 for x in ActivityData[keys][9:12]]
        )
        sum_of_squares_magnetic = sum(
            [(x - mean_magnetic) ** 2 for x in ActivityData[keys][12:15]]
        )

        activity_features[keys].update(
            {
                "id": keys,
                "orSos": sum_of_squares_orientation,
                "rSos": sum_of_squares_rotation,
                "accSos": sum_of_squares_accelerometer,
                "gSos": sum_of_squares_gyroscope,
                "MagSos": sum_of_squares_magnetic,
                "Activity": ActivityData[keys][-1],
            }
        )
    return activity_features


def zero_crossing(ActivityData) -> dict:
    """
    purpose: function for computing the zero crossing of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with zero crossing of each sensor readings
    """
    for keys in ActivityData:
        or_zcross = sum(
            1
            for ind, val in enumerate(ActivityData[keys][:3])
            if (ind + 1 < len(ActivityData[keys][:3]))
            if ActivityData[keys][:3][ind] * ActivityData[keys][:3][ind + 1] < 0
        )
        r_zcross = sum(
            1
            for ind, val in enumerate(ActivityData[keys][3:6])
            if (ind + 1 < len(ActivityData[keys][3:6]))
            if ActivityData[keys][:3][ind] * ActivityData[keys][3:6][ind + 1] < 0
        )
        acc_zcross = sum(
            1
            for ind, val in enumerate(ActivityData[keys][6:9])
            if (ind + 1 < len(ActivityData[keys][6:9]))
            if ActivityData[keys][:3][ind] * ActivityData[keys][6:9][ind + 1] < 0
        )
        g_zcross = sum(
            1
            for ind, val in enumerate(ActivityData[keys][9:12])
            if (ind + 1 < len(ActivityData[keys][9:12]))
            if ActivityData[keys][:3][ind] * ActivityData[keys][9:12][ind + 1] < 0
        )
        m_zcross = sum(
            1
            for ind, val in enumerate(ActivityData[keys][12:15])
            if (ind + 1 < len(ActivityData[keys][12:15]))
            if ActivityData[keys][:3][ind] * ActivityData[keys][12:15][ind + 1] < 0
        )

        activity_features[keys].update(
            {
                "id": keys,
                "orZcross": or_zcross,
                "rZcross": r_zcross,
                "accZcross": acc_zcross,
                "gZcross": g_zcross,
                "MagZcross": m_zcross,
                "Activity": ActivityData[keys][-1],
            }
        )
    return activity_features


def covariance(ActivityData) -> dict:
    """
    purpose: function for computing the covariance of each sensor readings
    Argument: ActivityData
    Return: activity_features populated with covariance of each sensor readings
    """
    # note that we have only one set of observations and no other set of observations to find our covariance against
    # COV(X,X) = VAR(X)\
    for keys in ActivityData:
        mean_orientation_Xi = sum(ActivityData[keys][:3]) / len(ActivityData[keys][:3])
        mean_rotation_Xi = sum(ActivityData[keys][3:6]) / len(ActivityData[keys][3:6])
        mean_accelerometer_Xi = sum(ActivityData[keys][6:9]) / len(
            ActivityData[keys][6:9]
        )
        mean_gyroscope_Xi = sum(ActivityData[keys][9:12]) / len(
            ActivityData[keys][9:12]
        )
        mean_magnetic_Xi = sum(ActivityData[keys][12:15]) / len(
            ActivityData[keys][12:15]
        )

        cov_orientation = sum(
            [(x - mean_orientation_Xi) ** 2 for x in ActivityData[keys][:3]]
        ) / len(ActivityData[keys][:3])
        cov_rotation = sum(
            [(x - mean_rotation_Xi) ** 2 for x in ActivityData[keys][3:6]]
        ) / len(ActivityData[keys][3:6])
        cov_accelerometer = sum(
            [(x - mean_accelerometer_Xi) ** 2 for x in ActivityData[keys][6:9]]
        ) / len(ActivityData[keys][6:9])
        cov_gyroscope = sum(
            [(x - mean_gyroscope_Xi) ** 2 for x in ActivityData[keys][9:12]]
        ) / len(ActivityData[keys][9:12])
        cov_magnetic = sum(
            [(x - mean_magnetic_Xi) ** 2 for x in ActivityData[keys][12:15]]
        ) / len(ActivityData[keys][12:15])

        activity_features[keys].update(
            {
                "id": keys,
                "orCov": cov_orientation,
                "rCov": cov_rotation,
                "accCov": cov_accelerometer,
                "gCov": cov_gyroscope,
                "MagCov": cov_magnetic,
                "Activity": ActivityData[keys][-1],
            }
        )
    return activity_features


def write_features_to_csv(no, ActivityData) -> None:
    """
    purpose: function for writing out feature extracted based on feature choosen
    Argument: no , ActivityData
    Return: None
    """
    print("Computing features...\n")
    if (
        os.path.exists("extracted_features") == False
    ):  # checks if directory exists before creating it
        os.mkdir(
            "extracted_features"
        )  # creating a directory to put the new csv files in
    else:
        pass
    os.chdir("extracted_features")  # changing into the directory
    if no == "1":
        features = mean(ActivityData)
        csv_columns = [
            "id",
            "orMean",
            "rMean",
            "accMean",
            "gMean",
            "MagMean",
            "Activity",
        ]
        csv_filename = "mean_features.csv"
        hold_list = []
        try:
            with open(csv_filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    # print(data)
        except IOError:
            print("I/O error")
    elif no == "2":
        features = variance(ActivityData)
        csv_columns = ["id", "orVar", "rVar", "accVar", "gVar", "MagVar", "Activity"]
        csv_filename = "variance_features.csv"
        hold_list = []
        try:
            with open(csv_filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    # print(data)
        except IOError:
            print("I/O error")
    elif no == "3":
        features = median(ActivityData)
        csv_columns = [
            "id",
            "orMedian",
            "rMedian",
            "accMedian",
            "gMedian",
            "MagMedian",
            "Activity",
        ]
        csv_filename = "median_features.csv"
        hold_list = []
        try:
            with open(csv_filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    # print(data)
        except IOError:
            print("I/O error")
    elif no == "4":
        features = standard_deviation(ActivityData)
        csv_columns = ["id", "orStd", "rStd", "accStd", "gStd", "MagStd", "Activity"]
        csv_filename = "std_features.csv"
        hold_list = []
        try:
            with open(csv_filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    # print(data)
        except IOError:
            print("I/O error")
    elif no == "5":
        features = root_mean_square(ActivityData)
        csv_columns = ["id", "orRms", "rRms", "accRms", "gRms", "MagRms", "Activity"]
        csv_filename = "root_mean_square_features.csv"
        hold_list = []
        try:
            with open(csv_filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    # print(data)
        except IOError:
            print("I/O error")
    elif no == "6":
        features = zero_crossing(ActivityData)
        csv_columns = [
            "id",
            "orZcross",
            "rZcross",
            "accZcross",
            "gZcross",
            "MagZcross",
            "Activity",
        ]
        csv_filename = "zerocrossing_features.csv"
        hold_list = []
        try:
            with open(csv_filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    # print(data)
        except IOError:
            print("I/O error")
    elif no == "7":
        features = sum_of_square(ActivityData)
        csv_columns = ["id", "orSos", "rSos", "accSos", "gSos", "MagSos", "Activity"]
        csv_filename = "sum_squares_features.csv"
        hold_list = []
        try:
            with open(csv_filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    # print(data)
        except IOError:
            print("I/O error")
    elif no == "8":
        features = covariance(ActivityData)
        csv_columns = ["id", "orCov", "rCov", "accCov", "gCov", "MagCov", "Activity"]
        csv_filename = "covariance_features.csv"
        hold_list = []
        try:
            with open(csv_filename, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    # print(data)
        except IOError:
            print("I/O error")
    else:
        raise Exception("Wrong value given")
    print("Feature completed.Check extracted_features folder")
