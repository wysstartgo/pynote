import redis

re = redis.Redis(host='192.168.1.136',port=6379,db=0,password='reRedis123',socket_connect_timeout=5,socket_keepalive=60,max_connections=50)
data = re.get('global:MARKET_CATEGORY_KEY')
print(type(data))
print(data)