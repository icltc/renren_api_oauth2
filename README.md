#Renren OAuth 2 API Python SDK
#使用简介
#Step 1: 注册人人APP
注册人人App后，可以获得app key和app secret，然后定义网站回调地址：

#Step 2: 从注册的APP中得到如下参数
from renren import APIClient

API_KEY = '1234567' # api key
APP_SECRET = 'abcdefghijklmn' # app secret
REDIRECT_URL = 'http://www.example.com/callback' # callback url


#Step 3: 得到authorize code
引导用户点击
http://graph.renren.com/oauth/grant?client_id=267865509b3f4d6d8750c0e589981511&redirect_uri=http%3A%2F%2Fwww.amadeus.com&response_type=code&display=page&scope=&state=&secure=true&origin=00000
read_user_blog

client_id是API_KEY
redirect_uri 是 REDIRECT_URL
responsetype 是 code

其中scope选填(不同的权限由‘+’分开，更多参考http://wiki.dev.renren.com/wiki/%E6%9D%83%E9%99%90%E5%88%97%E8%A1%A8)：
+read_user_checkin
+read_user_feed
...


建议在网站放置“使用人人账号登录”的链接，

当用户点击链接后，引导用户跳转至上述URL：

用户授权后，将跳转至网站回调地址，在url上会附加参数code=abcd1234：

#Step 4: 获取access token
// 获取URL参数code:
code = #将上面获得的code取出放在此处
client = APIClient(app_key=API_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
r = client.request_access_token(code)
access_token = r.access_token # 人人返回的access token
expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4

//token 被设定在了client里，以后调用api的时候免去了输入token
client.set_access_token(access_token, expires_in)
#Step 5: 调用API
然后，可调用任意API：

print client.statuses.user_timeline.get()
print client.statuses.update.post(status=u'测试OAuth 2.0发微博')
print client.statuses.upload.post(status=u'测试OAuth 2.0带图片发微博', pic=open('/Users/michael/test.png'))
【API调用规则】

首先查看人人API文档（http://wiki.dev.renren.com/wiki/API2），例如：

API：/v2/status/list

请求格式：GET

请求参数：
名称	  类型	必选	 描述
ownerId	long	true	状态所有者的用户ID


调用方法：将API的“/”变为“.”，根据请求格式是GET或POST，调用get ()或post()并传入关键字参数，但不包括source和access_token参数：

GET 调用：
r = client.status.list.get(ownerId = 251560914)

for st in r['response']:
    print st['content']


若为POST调用，则示例代码如下：

r = client.album.put.post(name = "Test")




