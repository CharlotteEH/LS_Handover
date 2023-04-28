from c_ros_1 import rosd
import pandas as pd


rosd["ros_vol"] = rosd["total_vol"]/rosd["dist"]
rosd["ros_val"] = rosd["total_val"]/rosd["dist"]
rosd["ros_quan"] = rosd["total_quan"]/rosd["dist"]
rosd["avg_price"] = rosd["total_val"]/rosd["total_quan"]

print(rosd.head())