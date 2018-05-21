import time
from functools import wraps


import inspect
 

# def get_current_function_name():
    # return inspect.stack()[1][3]
def test(a=1,b=2):
    print(a)
    print(b)

def test_d(**params):
    print(params)

def timer(name):

    def inner(func):
        @wraps(func)
        def wrapper(self,**params):
            print(name,func.__name__,"=======begin=====",self.arg)
            start = time.time()
            r = func(self,**params)
            print(name,func.__name__,"======end======",self.arg,time.time() - start)
            return r
        return wrapper
    return inner


class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

    @timer('123')
    def func1(self,**params):
        time.sleep(5)
        print(params)
        print("func1!")


    @timer('456')
    def func2(self,**params):
        time.sleep(2)
        print(params)
        print("func2!")


    def haha(self):
        print("haha in")
        
        self.gaga()
        print("haha out")
    
    def gaga(self):
        print("gaga in")
        
        self.jaja()
        print("gaga out")

    def jaja(self):
        print("jaja in")
        # print(inspect.stack()[1])
        print(inspect.stack()[1][3])
        print("jaja out")

[FrameInfo(frame=<frame object at 0x7fb984003408>, filename='/Users/m92/Documents/gitlab/nano_model/dbhelper/mysql/mysql_helper.py', lineno=30, function='query', code_context=['        print("==================",inspect.stack())\n'], index=0), FrameInfo(frame=<frame object at 0x114c719f8>, filename='/Users/m92/Documents/gitlab/nano_model/dbhelper/dbhelper.py', lineno=24, function='inner_func_wrapper', code_context=['            return func(self, *args, **kwargs)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb9840030d8>, filename='/Users/m92/Documents/gitlab/nano_model/dbhelper/dbhelper.py', lineno=88, function='function_wrapper', code_context=['                return func(other, *args, **kwargs)  # 不改变原函数的执行逻辑，仅仅是重复执行罢了\n'], index=0), FrameInfo(frame=<frame object at 0x114c71428>, filename='/Users/m92/Documents/gitlab/nano_model/dbhelper/dbhelper.py', lineno=26, function='function_wrapper', code_context=['        return inner_func_wrapper(self, *args, **kwargs)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb984001428>, filename='/Users/m92/Documents/gitlab/nano_model/dao/mobile_card_dao.py', lineno=77, function='get_customer_basic_info', code_context=['            ret = self.query(sql)[0]  # todo 即便重试也出错，具体如何处理待定\n'], index=0), FrameInfo(frame=<frame object at 0x114c71048>, filename='/Users/m92/Documents/gitlab/nano_model/objects/user_info.py', lineno=60, function='get_user_basic_info', code_context=['        return Mobile_Card_Dao.get_customer_basic_info(self.customer_id)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb984002bc8>, filename='/Users/m92/Documents/gitlab/nano_model/utils/memoize.py', lineno=40, function='__call__', code_context=['            res = cache[key] = self.func(*args, **kw)\n'], index=0), FrameInfo(frame=<frame object at 0x114c6fbe8>, filename='/Users/m92/Documents/gitlab/nano_model/objects/user_info.py', lineno=114, function='__get_elemet_from_basic_info', code_context=['        info =  self.get_user_basic_info()\n'], index=0), FrameInfo(frame=<frame object at 0x114c6f9f8>, filename='/Users/m92/Documents/gitlab/nano_model/objects/user_info.py', lineno=56, function='examine_amount', code_context=["        return self.__get_elemet_from_basic_info('examine_amount', 0)\n"], index=0), FrameInfo(frame=<frame object at 0x114c6f808>, filename='/Users/m92/Documents/gitlab/nano_model/controllers/pre_score.py', lineno=89, function='payday_amount', code_context=['    examine_amount = float(user_info.examine_amount)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983fa6578>, filename='/Users/m92/Documents/gitlab/nano_model/controllers/pre_score.py', lineno=72, function='get_payday_pre_score_controller', code_context=['            feature_result, model_result = payday_amount(user_info,feature_generator, investor_id)\n'], index=0), FrameInfo(frame=<frame object at 0x114c62dd8>, filename='/Users/m92/Documents/gitlab/nano_model/server.py', lineno=41, function='api_get_user_pre_score_fun', code_context=['    r = get_payday_pre_score_controller(request.json)\n'], index=0), FrameInfo(frame=<frame object at 0x114c62808>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/site-packages/flask/app.py', lineno=1598, function='dispatch_request', code_context=['        return self.view_functions[rule.endpoint](**req.view_args)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983b90b28>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/site-packages/flask/app.py', lineno=1612, function='full_dispatch_request', code_context=['                rv = self.dispatch_request()\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983b8f438>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/site-packages/flask/app.py', lineno=1982, function='wsgi_app', code_context=['                response = self.full_dispatch_request()\n'], index=0), FrameInfo(frame=<frame object at 0x114d58618>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/site-packages/flask/app.py', lineno=1997, function='__call__', code_context=['        return self.wsgi_app(environ, start_response)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983b8f1f8>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/site-packages/werkzeug/serving.py', lineno=197, function='execute', code_context=['            application_iter = app(environ, start_response)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983ec03d8>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/site-packages/werkzeug/serving.py', lineno=209, function='run_wsgi', code_context=['            execute(self.server.app)\n'], index=0), FrameInfo(frame=<frame object at 0x114d46618>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/site-packages/werkzeug/serving.py', lineno=267, function='handle_one_request', code_context=['            return self.run_wsgi()\n'], index=0), FrameInfo(frame=<frame object at 0x114d46428>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/http/server.py', lineno=418, function='handle', code_context=['        self.handle_one_request()\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983ebf5f8>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/site-packages/werkzeug/serving.py', lineno=232, function='handle', code_context=['            rv = BaseHTTPRequestHandler.handle(self)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983ebef78>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/socketserver.py', lineno=696, function='__init__', code_context=['            self.handle()\n'], index=0), FrameInfo(frame=<frame object at 0x114d339f8>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/socketserver.py', lineno=361, function='finish_request', code_context=['        self.RequestHandlerClass(request, client_address, self)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983ebed38>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/socketserver.py', lineno=639, function='process_request_thread', code_context=['            self.finish_request(request, client_address)\n'], index=0), FrameInfo(frame=<frame object at 0x114d33808>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/threading.py', lineno=864, function='run', code_context=['                self._target(*self._args, **self._kwargs)\n'], index=0), FrameInfo(frame=<frame object at 0x7fb983ebe5b8>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/threading.py', lineno=916, function='_bootstrap_inner', code_context=['                self.run()\n'], index=0), FrameInfo(frame=<frame object at 0x114d34230>, filename='/Users/m92/anaconda/envs/py36/lib/python3.6/threading.py', lineno=884, function='_bootstrap', code_context=['            self._bootstrap_inner()\n'], index=0)]
        
if __name__ == '__main__':
    # test({'a':1,'b':3})
    # test_d(**{'a':1,'b':3})
    # c = ClassName(5)
    # c.func1()
    # c.func2()

    # c.haha()

    