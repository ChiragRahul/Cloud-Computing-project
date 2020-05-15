places = open("AreaNameEnum.csv", "r")
areas = places.read()
areas = areas.split('\n')
for i in range(len(areas)):
    areas[i] = areas[i].split(',')
areas.pop(0)
areas.pop(-1)

dbaas = '54.81.160.102'  # DBaaS IP
rides_dns_name = "ec2-3-90-6-131.compute-1.amazonaws.com"
load_balancer = "FinalProject-1098727276.us-east-1.elb.amazonaws.com"
