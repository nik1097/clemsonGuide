import yaml

yfn = 'clemsonGuide.yaml'
yf  = open(yfn, 'r')
yd  = yaml.safe_load(yf)

panels = yd['panels']
dir    = panels['directory']
grp= yd['groups']

print("all:",       yd)
print("panels:",    panels)
print("groups:",grp)
print("directory:", dir)

### end ###
