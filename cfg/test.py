import yaml

with open("../config/dysl_config.yaml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)