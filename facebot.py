import mechanize
import sys
import time
import random
import os

## config
delay           = 10
delay_comment   = 4
delay_share     = 7
delay_logout    = 3
id_post         = '10155125362492079' #id post to comment
link_share      = 'https://www.facebook.com/detikcom/posts/10155125362492079' # url post or url web to share
accounts_file = "accounts.txt" ## account file in same folder
comments_file = "comments.txt" ## comments file in same folder
shares_file   = "shares.txt" ## shares file in same folder


print "==================================================================="
print "======================== INDONESIA MERDEKA ========================"
print "==================================================================="


def login(username,password):
    print "[-] LOGIN"
    print "[+] username : "+ username
    print "[+] password : "+ password
    br = mechanize.Browser()
    cj = mechanize.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open("https://m.facebook.com/")
    br.select_form(nr=0)
    br.form['email'] = username
    br.form['pass'] = password
    br.submit()
    print "[-] SUCCESS LOGIN"
    return br

def comments(br,id_post,text_komen):
    print "[-] CREATE COMMENT "
    br.open("https://m.facebook.com/"+id_post)
    br.select_form(nr=0)
    br.set_all_readonly(False)
    br.form['comment_text'] = text_komen
    br.submit()
    br.response().read()
    print "[-] SUCCESS CREATE COMMENT "

def shares(br,link_post,text_share):
    print "[-] CREATE SHARE"
    br.open("https://www.facebook.com/sharer/sharer.php?u="+link_post)
    br.select_form(nr=0)
    br.set_all_readonly(False)
    br.form['xhpc_message'] = text_share
    br.submit(name='__CONFIRM__')
    br.response().read()
    print "[-] SUCCESS SHARE"

def logout(br):
    print "[-] LOGOUT"
    br.open("https://m.facebook.com/bookmarks")
    for link in br.links(url_regex="logout.php"):
        br.open("https://m.facebook.com"+link.url)


def debug_form(br):
    for form in br.forms():
        print form



def mulai():
         dir_path = os.path.dirname(os.path.realpath(__file__))
         with open(dir_path+"/"+accounts_file) as f: s = f.read()
         akun_list = s.split('\n')
         nomor = 0
         for akun in akun_list:
             try:
                 nomor += 1
                 print "[>] No. "+ str(nomor)
                 user_pass = akun.split(':')
                 br = login(user_pass[0],user_pass[1])

                 print "[-] Delay Comment " + str(delay_comment) + " Second"
                 time.sleep(delay_comment)

                 # komen
                 with open(dir_path+"/"+comments_file) as f: s = f.read()
                 komen_list = s.split("::")
                 komen = random.choice(komen_list)
                 comments(br,id_post,komen)

                 print "[-] Delay share " + str(delay_share) + " Second"
                 time.sleep(delay_share)

                 # share
                 with open(dir_path+"/"+shares_file) as f: s = f.read()
                 share_list = s.split("::")
                 share = random.choice(share_list)
                 shares(br,link_share,share)

                 print "[-] Delay logout " + str(delay_logout) + " Second"
                 time.sleep(delay_logout)

                 # logout
                 logout(br)

                 print "[-] Delay change account " + str(delay) + " Second"
                 print "------------------------------------------------"
                 time.sleep(delay)

             except Exception as e:
                 print "[-] Failed ..."
                 print "[-] Message : " + str(e)
                 print "------------------------------------------------"

mulai()
