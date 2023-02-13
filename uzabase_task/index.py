import requests,re
from bs4 import BeautifulSoup


def start():
    try:
        input_rss()
        ##複数個rssを入力する際にコメントアウトを外す
        # again()
    except:
        print('エラー:start関数内での予期せぬエラー発生')


def input_rss():
    while True:
        string = input('入力したいRSSを入力してください:')
        if re.search(r'rss',string):
            try:
                req = requests.get(string)
                txt= BeautifulSoup(req.text, 'html.parser')
            except :
                print('URLエラー:入力されたURLでは作業できません')
                print('形式をもう一度確認し、入力してください')
                continue
            else:
                txt_fix = str(txt).replace('NewsPicks','')
                print(txt_fix)
                break 
        else:
            print('エラー:入力された値に文字列(rss)を検知できませんでした')
            print('形式をもう一度確認し、入力してください')
            continue
#     #テキストファイル作成時にコメントアウトを外す
#     return mktxt(txt_fix)


# #テキストファイル作成時にコメントアウトを外す
# def mktxt(txt_fix):
#     file_name = input('作成するテキストファイルの名前を記入してください:')
#     f = open('uploads/'+str(file_name)+'.txt', mode='w')
#     f.write(txt_fix)  
#     f.close()



# #複数個rssを入力する際にコメントアウトを外す
# def again():
#     while True:
#         strings = input('他にもRSSを入力しますか？(y/n):')
#         if strings == 'y':
#             start()
#             break
#         elif strings == 'n':
#             break
#         else:
#             print('エラー:y(yes)かn(no)で答えてください')
#             continue


start()
