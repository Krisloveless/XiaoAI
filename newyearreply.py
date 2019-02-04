# -*- coding:utf-8 -*-
import itchat
words = ["新","年","快","乐"]
dirty = ["傻","傻逼","胖","猪","sb","辣鸡","笨","沙雕"]
praise = ["厉害","聪明","棒棒哒"]
@itchat.msg_register(itchat.content.TEXT,isFriendChat=True)
def text_reply(msg):
	tmp = []
	count = len([i for i in words if i in msg.text])
	if count == 0:
		tmp = "聪明的小机器人不懂你在说啥, 主人现在不在, 请不要说我不懂的 233(This chat bot is written with ❤ by Shuo, 五毛一条, 5 mao one tiao)".format(msg.text)
	else:
		data = itchat.search_friends(userName=msg.fromUserName)
		name = data["RemarkName"] if data["RemarkName"] != "" else data["NickName"]
		tmp = "{}，祝你新年快乐哇(聪明的小贾烁已经想好怎么回复你们了This chat bot is written with ❤ by Shuo, 五毛一条, 5 mao one tiao)".format(name)
	count = len([i for i in dirty if i in msg.text])
	if count != 0:
		v = [i for i in dirty if i in msg.text]
		tmp = "你才是"
		for i in v:
			tmp += "%s," % (i)
		tmp = tmp[:-1]
		tmp += "(不要想趁机欺负不在的小贾烁, This chat bot is written with ❤ by Shuo, 五毛一条, 5 mao one tiao)"		
	count = len([i for i in praise if i in msg.text])
	if count != 0:
		tmp = "对哇我就是聪明厉害棒棒哒的小贾烁机器人(This chat bot is written with ❤ by Shuo, 五毛一条, 5 mao one tiao)"
	return tmp

 #<User: {'HeadImgFlag': 1, 'IsOwner': 0, 'SnsFlag': 17, 'UniFriend': 0, 'EncryChatRoomId': '', 'PYInitial': 'KRISD3V', 'VerifyFlag': 0, 'AttrStatus': 33588157, 'HideInputBarFlag': 0, 'ChatRoomId': 0, 'RemarkPYQuanPin': '', 'Signature': 'Or will you let darkness fall？', 'City': '', 'Sex': 1, 'KeyWord': '', 'MemberList': <ContactList: []>, 'RemarkName': '', 'NickName': 'krisd3v', 'UserName': '@c77b82dc96a1a741b005f2c685526d7bfd3686609b369aad957f0e79ffa5d700', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=0&username=@c77b82dc96a1a741b005f2c685526d7bfd3686609b369aad957f0e79ffa5d700&skey=@crypt_905351b6_a509fd8f88d9399454bfe0e88c1eebeb', 'OwnerUin': 0, 'AppAccountFlag': 0, 'StarFriend': 0, 'DisplayName': '', 'RemarkPYInitial': '', 'WebWxPluginSwitch': 1, 'Uin': 2116349261, 'MemberCount': 0, 'Alias': '', 'Statues': 0, 'ContactFlag': 1, 'PYQuanPin': 'krisd3v', 'Province': ''}>

itchat.auto_login()
itchat.run()

#{'UniFriend': 0, 'City': '', 'DisplayName': '', 'HeadImgFlag': 1, 'RemarkPYQuanPin': '', 'StarFriend': 0, 'Statues': 0, 'Signature': '0 warning, 0 error', 'EncryChatRoomId': '', 'UserName': '@5eb18b26429fd5378a779815714a7b9ba54c73313ca1384d177d0cfa935d0944', 'RemarkName': '', 'Alias': '', 'IsOwner': 0, 'AppAccountFlag': 0, 'SnsFlag': 17, 'HideInputBarFlag': 0, 'AttrStatus': 33592253, 'Province': '', 'PYQuanPin': 'aout', 'VerifyFlag': 0, 'ChatRoomId': 0, 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=0&username=@5eb18b26429fd5378a779815714a7b9ba54c73313ca1384d177d0cfa935d0944&skey=@crypt_905351b6_c868731b4f904913edab632a0ce3fb01', 'OwnerUin': 0, 'RemarkPYInitial': '', 'PYInitial': 'AOUT', 'MemberCount': 0, 'MemberList': <ContactList: []>, 'KeyWord': '', 'Sex': 1, 'WebWxPluginSwitch': 1, 'ContactFlag': 1, 'Uin': 2116349261, 'NickName': 'a.out'}