import redis
from Common.ReadYaml import ConfigYaml


class ReDis:

    def __init__(self,value=''):
        '''
        redis连接操作
        :param value:
        '''
        self.ip = ConfigYaml('redisip').base_config
        self.port = ConfigYaml('redisport').base_config
        self.rediskey = ConfigYaml('redisresult').base_config
        self.value = value
        try:
            pool = redis.ConnectionPool(host=self.ip, port=self.port, decode_responses=True)
            self.r = redis.Redis(connection_pool=pool,db=1)
        except:
            raise ConnectionError("redis连接异常...")

    def lpush(self):
        '''
        左添加数据
        :return:
        '''
        return self.r.lpush(self.rediskey,self.value)

    def lrange(self,start=0,end= -1):
        '''
        获所有取数据
        :param start: 开始值
        :param end:结束值
        :return:
        '''
        return self.r.lrange(self.rediskey,start,end)

    def increase(self):
        '''
        追加数据
        :return:
        '''
        return self.r.append(self.rediskey,self.value)

    def llenth(self):
        '''
        获取列表长度
        :return:
        '''
        return self.r.llen(self.rediskey)

    def rpush(self):
        '''
        右插入数据
        :return:
        '''
        return self.r.rpush(self.rediskey,self.value)

    def lpop(self):
        '''
        左删除---返回删除值
        :return:
        '''
        return self.r.lpop(self.rediskey)

    def rpop(self):
        '''
        右删除---返回删除值
        :return:
        '''
        return self.r.rpop(self.rediskey)

    def delete(self):
        '''
        删除简直---表
        :return:
        '''
        if self.r.exists(self.rediskey):
            return self.r.delete(self.rediskey)


if __name__=="__main__":
    ReDis().delete()



