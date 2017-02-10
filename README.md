# FaceBot - Python Auto Comment & Share Facebook

Facebook auto comment and share, this is very useful for the promotion or any

![Image](https://raw.githubusercontent.com/aldiferdiyan/python_facebook_comment_share/master/ss.jpg)

### Installation:


* we use python 2.7, > for windows download from https://www.python.org/downloads/
* Import Module with pip or easy_install

```python
pip install mechanize
```

For running, go to directory facebot and run
```python
python facebot.py
```

### Configuration:

* set accounts username-password in file : `accounts.txt` separated by a `new line`
* set comments text in file : `comments.txt`  separated them with `::`
* set shares text in file : `shares.txt` separated them with `::`
* and setup delay, id post and url to share in file : `facebot.py`
```python
delay           = 10 # delay change account
delay_comment   = 4 # delay comment
delay_share     = 7 # delay share
delay_logout    = 3 # delay logout
id_post         = '10155125362492079' #id post to comment
link_share      = 'https://www.facebook.com/detikcom/posts/10155125362492079' # url post or url web to share
accounts_file = "accounts.txt" # account file in same folder
comments_file = "comments.txt" # comments file in same folder
shares_file   = "shares.txt" # shares file in same folder
```


That's it ..

### Donation

If this project help you reduce time to develop, you can give me a cup of coffee :)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](aldi_fe@yahoo.com)
