import yaml
with open("number.yaml") as f:
        data = yaml.load(f)
        data1 = data.items()
        data2 = list(data1)
        print(data2[0][1][0])
# class calc:
#     def __init__(self):
#         self.add1 = data[0][0]
#     def add(self):

