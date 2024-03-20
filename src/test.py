#!/usr/bin/env python
# import the yaml module
import yaml
import rospkg

rospack = rospkg.RosPack()
print(rospack.get_path('drone_control')+'/config/dysl_config.yaml')
# load the yaml file
# document = open('../config/dysl_config.yaml', 'r')
# and finally parse the file
# parsed = yaml.load(document)
# print(parsed.D_x)
