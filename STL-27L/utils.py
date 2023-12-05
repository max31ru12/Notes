from PointCloud import PointCloud


def parse_data(data_sixteen: str):
    DATA = {}

    if len(data_sixteen) != 0:
        data_list = data_sixteen.split()
        N = len(data_list)
        try:

            DATA["header"] = data_list[0]
            DATA["VevLen"] = data_list[1]
            DATA["speed"] = int(data_list[3] + data_list[2], 16)
            DATA["start_angle"] = int(data_list[5] + data_list[4], 16) / 100
            DATA["PointCloud"] = PointCloud(data_list[6:N - 5])
            DATA["end_angle"] = int(data_list[N - 4] + data_list[N - 5], 16) / 100
            DATA["timestamp"] = int(data_list[N - 2] + data_list[N - 3], 16)
            DATA["CRC_check"] = int(data_list[N - 1], 16)

        except Exception as E:
            print(E, "data is less than 11 bytes")
            DATA["error"] = "incorrect data"

    else:
        DATA["error"] = "incorrect data"

    return DATA


def interpolation(point_cloud: dict, start_angle: float, end_angle: float) -> dict:

    if 'error' not in point_cloud.keys():
        step = (end_angle - start_angle) / (len(point_cloud) - 1)

        for i in range(0, len(point_cloud)):
            key = f"Point {i + 1}"
            angle = start_angle + step * i
            point_cloud[key]["angle"] = angle
    else:
        point_cloud["interpolation"] = "Interpolation Error"
    return point_cloud
