import yaml


# ��yaml
def read_yaml(filePath):
    with open(filePath, encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value