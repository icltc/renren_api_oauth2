# -*- coding: utf-8 -*-
__version__ = '1.0.0'
__author__ = 'Tianchi Liu (liutianchi@yahoo.com)'

import renren
from renren import APIClient
from pprint import pprint
import sys
import logging,urllib2
from termcolor import colored

APP_KEY = '267865509b3f4d6d8750c0e589981511'
APP_SECRET = 'd722b9598dbb44a9815e6c3e25f7f70f'
CALLBACK_URL = 'http://www.amadeus.com'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
code = 'bqkobMjx51yKY8NtElYimTGhdq5O8uAI'

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level = logging.DEBUG)

#r = client.request_access_token(code)
#access_token = r.access_token # 新浪返回的token，类似abc123xyz456
#expires_in = r.expires_in # 
access_token = '266188|6.161d8c1d31806bfc366340649742cf63.2592000.1400194800-311554316' #r.access_token
expires_in = '1400194800' #r.expires_in 
client.set_access_token(access_token, expires_in)



class testApi(object):
    def __init__(self):
        self.case_count = 0
        self.success = 0
        self.fail = 0
    def test(self,func, *args,**kwargs):
        try:
            self.case_count += 1
            print "# Case: " + colored(str(self.case_count),'cyan')
            r = func(*args,**kwargs)
            self.success += 1
            logging.info( str(self.case_count) + ". " +colored("OK",'green'))
            return r
        except urllib2.HTTPError, e:
            #e = sys.exc_info()
            self.fail += 1
            logging.debug( str(self.case_count) + ". " + colored("KO",'red') + ": "+ str(e) )
        except urllib2.URLError, e:
            self.fail += 1
            logging.debug( str(self.case_count) + ". " + colored("KO",'red') + ": "+ str(e) )
            
    def result_statistic(self):
        print "\n\n**************"
        print "# success: " + colored(str(self.success), 'green')
        print "# failed: " + colored(str(self.fail), 'red')
        print "**************"


if __name__=='__main__':
    api = testApi()
    
    # Location
    api.test(client.location.feed.list.GET,locationFeedType = 'TYPE_ALL', longitude = 0.18, latitude =51.49 )
    api.test(client.location.get.GET, longitude = 0.18, latitude =51.49)

    #album
    api.test(client.album.list.GET, ownerId = 251560914)
    api.test(client.album.get.GET, ownerId = 251560914, albumId = 893413930)
    api.test(client.album.put.POST, name = "Test")

    #blog
    api.test(client.blog.list.GET,ownerId = 251560914)
    api.test(client.blog.put.POST, title = "Test", content = 'This is test blog!')
    api.test(client.blog.get.GET,ownerId = 311554316,blogId = 926485461)
    #vipinfo
    api.test(client.vipinfo.get.GET, userId = 251560914)

    #evaluation
    api.test(client.evaluation.put.POST, content = "Test", placeId=00000)
    api.test(client.evaluation.reply.put.POST, content = "Test!", ownerId = 311554316, evaluationId =3037359 )
    api.test(client.evaluation.reply.list.GET,ownerId = 311554316, evaluationId =3037359,pageNo = 1, pageSize = 10)


    #share
    api.test(client.share.ugc.put.POST, ugcOwnerId = 311554316, ugcId = 926434846, ugcType = 'TYPE_BLOG')
    api.test(client.share.count.get.GET,ugcOwnerId = 311554316, ugcId = 926434846, ugcType = 'TYPE_BLOG')
    
    api.test(client.share.hot.list.GET, shareType = 'TYPE_BLOG')
    api.test(client.share.url.put.POST,url = 'https://pypi.python.org/pypi/termcolor/1.1.0')
    api.test(client.share.url.count.get.GET,url = 'https://pypi.python.org/pypi/termcolor/1.1.0')
    api.test(client.share.list.GET, ownerId = 251560914)
    api.test(client.share.get.GET, shareId = 17101055494,ownerId = 287286115)

    #page
    api.test(client.page.isfan.GET, pageId=600003167)
    api.test(client.page.user.list.GET, pageSize = 20, pageNumber=1)
    api.test(client.page.list.GET, pageSize = 20, pageNumber=1)
    api.test(client.page.get.GET, pageId=600003167)
    #ubb
    api.test(client.ubb.list.GET)

    #notification
    api.test(client.notification.user.put.POST, content = "Test", userIds = "251560914")
    api.test(client.notification.app.put.POST, content = "Test", userIds = "311554316")

    #feed
    api.test(client.feed.put.POST,message = 'Test', title = 'test', description = "Test", targetUrl = 'http://page.renren.com/601621937')
    api.test(client.feed.list.GET)

    #invitation
    #api.test(client.invitation.put.POST, userId = 251560914,url = 'http://apps.renren.com/bxsjbei?origin=40021')

    #place
    api.test(client.place.friend.feed.list.GET, pageNo = 1, pageSize = 10)
    api.test(client.place.put.POST, address = 'Wimbledon', name = 'Wimbledon',longitude = 0.18, latitude =51.49)
    api.test(client.place.feed.list.GET, placeId = 819126040, locationFeedType = 'TYPE_ALL')
    api.test(client.place.list.GET, longitude = 0.18, latitude =51.49)

    #profile
    api.test(client.profile.get.GET, userId = 251560914)

    #app
    api.test(client.app.get.GET)

    #status
    api.test(client.status.get.GET,statusId = 4868403165,ownerId = 251560914)
    api.test(client.status.put.POST, content = "Test Renren!")
    api.test(client.status.list.GET, ownerId = 251560914)
    api.test(client.status.share.POST, content = "Test   Share!", statusId = 4866345182,ownerId = 251560914 )

    #like
    api.test(client.like.ugc.put.POST,ugcOwnerId = 311554316,likeUGCType = 'TYPE_STATUS', ugcId =25108221616 )
    api.test(client.like.ugc.remove.POST, ugcOwnerId = 311554316,likeUGCType = 'TYPE_STATUS', ugcId =25108221616 )

    api.test(client.like.ugc.info.get.GET, likeUGCType = 'TYPE_STATUS', ugcId =4868403165 )

    #photo
    api.test(client.photo.upload.POST, file = "a.jpg" , description = "Test!",albumId = "1003510802")
    api.test(client.photo.get.GET, photoId = 7262324276, ownerId = 251560914)
    api.test(client.photo.list.GET, albumId = 893413930, ownerId = 251560914)


    #checkin

    api.test(client.checkin.put.POST,content = "Test", placeId=00000)
    api.test(client.checkin.list.GET,pageNo = 1,pageSize=5)
    api.test(client.checkin.get.GET,checkinId = 117691883)
    api.test(client.checkin.reply.put.POST,checkinId = 117691883, content = "Test")
    api.test(client.checkin.reply.list.GET,checkinId =117691883,pageNo = 1,pageSize=5 )
    
    #comment
    api.test(client.comment.put.POST, content = 'Test', commentType='STATUS', entryOwnerId=251560914 ,entryId = 4868403165)
    api.test(client.comment.list.GET, commentType='STATUS',  entryOwnerId=251560914 ,entryId = 4868403165)

    #user
    api.test(client.user.batch.GET, userIds = "251560914,253671230")
    api.test(client.user.get.GET, userId = 251560914)
    api.test(client.user.friend.list.GET, userId = 251560914)
    api.test(client.user.friend.uninstall.list.GET)
    api.test(client.user.friend.mutual.list.GET, userId = 251560914)
    api.test(client.user.friend.app.list.GET, userId = 251560914)
    api.test(client.user.login.get.GET)

    #friend
    api.test(client.friend.list.GET)

   

    api.result_statistic()

#http://graph.renren.com/oauth/grant?client_id=267865509b3f4d6d8750c0e589981511&redirect_uri=http%3A%2F%2Fwww.amadeus.com&response_type=code&display=page&scope=read_user_blog+read_user_checkin+read_user_feed+read_user_guestbook+read_user_invitation+read_user_like_history+read_user_message+read_user_notification+read_user_photo+read_user_status+read_user_album+read_user_comment+read_user_share+read_user_request+publish_blog+publish_checkin+publish_feed+publish_share+write_guestbook+send_invitation+send_request+send_message+send_notification+photo_upload+status_update+create_album+publish_comment+operate_like&state=&secure=true&origin=00000


