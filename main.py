'''
while true
do
python3 discbot.py
sleep 1
done
'''

import discord, datetime, unicodedata, re, string, pytz, hashlib, requests, random, os, sys, regex, json, shlex
from zalgo_text import zalgo
from collections import defaultdict

client = discord.Client()

@client.event
async def on_ready():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('Logged in as {0.user}'.format(client))
    with open('pcmd.txt', 'w') as filetowrite:
        filetowrite.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\nLogged in as {0.user}'.format(client))
    game = discord.Game("a!help")
    await client.change_presence(status=discord.Status.online, activity=game)
    # msgdict = {}

@client.event
async def on_connect():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('Connected')
    with open('pcmd.txt', 'w') as filetowrite:
        filetowrite.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\nConnected')

@client.event
async def on_disconnect():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('Disconnected')
    with open('pcmd.txt', 'w') as filetowrite:
        filetowrite.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\nDisconnected')

@client.event
async def on_message(message):

    pcmd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n{0.author} just sent "{0.content}" to {0.guild}#{0.channel}'.format(message)
    with open('pcmd.txt', 'w') as filetowrite:
        filetowrite.write(pcmd)
    with open('msgspcmd.txt', 'r') as filetoread:
        ahoefiud = filetoread.read()
    with open('msgspcmd.txt', 'w') as filetowrite:
        filetowrite.write(pcmd + '<br>' + ahoefiud)

    words = message.content.lower().split()
    table = str.maketrans('', '', string.punctuation)
    wwm = [w.translate(table).lower() for w in words]
    
    urlregex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)

  # some stuff for certain severs only
    tos = '701616317446226020'
    bt = '703033884928901211'
    flem = '724254242394734592'
    absr = '747680100203364462'
    fcct = '748431401824813126'
    ho = '759299021302661130'

    adb = '704618534012977183'
    anu = '414366946956541952'
    dad = '503720029456695306'
    tyl = '345425473213562900'
    ajl = '701617303996858460'
    cmy = '679496275640844329'
    drew = '671169004366200862'
    eewn = '523832165276844032'

    '''
    if str(message.guild.id) in [tos, bt, flem]:
        print(pcmd)
        if not message.author.bot:
            await message.channel.send("You are not supposed to be using your devices at this time.")
        return
    '''

    if str(message.guild.id) == fcct and 'heil thayallan' in ' '.join(wwm):
        print(pcmd)
        if not message.author.bot:
            await message.channel.send("Heil Thayallan")
    
    if str(message.guild.id) == fcct:
        return

    # C
    try:
        if message.channel.name.lower() in ['c','c-broadcast']:
            print(pcmd)
            if message.content == 'C':
                if message.channel.name == "c-broadcast": #message.author.discriminator == "0000" and 
                    await message.publish()
                await message.add_reaction('\U0001F1E8') # C
            else:
                await message.add_reaction('\U0001F621') # >:(
            if message.author == client.user:
                return
            await message.channel.send('C')
            return
    except:
        if (str(message.channel.type) == 'private' or str(message.channel.type) == 'group') and message.content == 'C':
            print(pcmd)
            await message.add_reaction('\U0001F1E8') # C
            if message.author == client.user:
                return
            await message.channel.send('C')
            return

    if str(message.guild.id) == ho and any([x in message.content.lower() for x in ['fuck','shit','bitch','cunt','cock','hell','nigg','whore','slut','faggot']]):
        print(pcmd)
        await message.channel.send('no swore >:(')
        await message.add_reaction('\U0001F621')
        return

    if "gay" in message.content.lower():
        print(pcmd)
        await message.channel.send(file=discord.File('whygay.png'))
        return

    if "retard" in message.content.lower():
        print(pcmd)
        await message.channel.send(file=discord.File('whyretarded.png'))
        return

    if (('dough' in message.content.lower() and 'know' in message.content.lower()) or (message.content[:12] == "More like, “" and message.author == client.user)) or (message.content in ["Joe Biden","Joe mama","Catherine Eugenia Finnegan","Who's Joe? Joe mama","Who's Joe? Joe Biden","Who's Joe? Catherine Eugenia Finnegan","Who's dough? Dough mama"] and message.author == client.user):
        await message.add_reaction('\U0001F606')
        await message.add_reaction('\U0001F602')
        await message.add_reaction('\U0001F923')

    if message.author == client.user: # so I don't have to do this over and over again
        print(pcmd)
        return

    # chain
    '''
    if message.channel in msgdict:
        msgdict[message.channel].append(message.content)
        if len(msgdict[message.channel]) > 10:
            _ = msgdict[message.channel].pop(0)
    else:
        msgdict[message.channel] = [message.content]
    if len(msgdict[message.channel]) >= 3:
        if msgdict[message.channel][-1].lower() == msgdict[message.channel][-2].lower() and msgdict[message.channel][-2].lower() == msgdict[message.channel][-3].lower():
            await message.channel.send(msgdict[message.channel][-1])'''
    # dict doesn't run over, need to import from file

    msgdict = eval(open('msgs.txt', 'r').read())
    try:
        uniqid = str(message.guild) + '#' + str(message.channel) + ' ' + str(message.guild.id) + '/' + str(message.channel.id)
    except:
        uniqid = str(message.channel.id)
    if uniqid in msgdict:
        msgdict[uniqid].append(message.content)
        if len(msgdict[uniqid]) > 10:
            _ = msgdict[uniqid].pop(0)
    else:
        msgdict[uniqid] = [message.content]

    if len(msgdict[uniqid]) >= 3:
        if msgdict[uniqid][-1].lower() == msgdict[uniqid][-2].lower() and msgdict[uniqid][-2].lower() == msgdict[uniqid][-3].lower():
            await message.channel.send(msgdict[uniqid][-1])
    else:
        pass
            
    with open('msgs.txt', 'w') as filetowrite:
        filetowrite.write(str(msgdict))

    # unredeemed
    if str(message.author.id) == anu:
        print(pcmd)
        await message.add_reaction('\U0001F621')
        #await message.channel.send('unredeemed')
        #return

    # help
    if message.content.lower() == 'a!help' or message.content.lower() == 'a!h' or message.content == '<@!704618534012977183>':
        print(pcmd)
        # • *`a!py <command>`* *(NEW!)* - runs python code that you give
        msg = discord.Embed(title="Hello! I'm AndewBot.", description = '''Here are my main functionalities:
• **[NEW!]** `a!impersonate [<nickname> <optional avatar image url> <message>] or [<@mention> <message>]` - pretends to be someone else with matching username and profile picture
• `a!mock <text>` - makes mOcKiNg tExT
• `a!pol <text>` - converts your text into Poliespellinglish (for more info, visit https://github.com/ajlee2006/poliespellinglish)
• `a!tb <text>` - Google Translates your text many times to make a really bad translation. (Many issues such as: only translates first sentence, for some reason)
• automatic chain detection - adds to message chains.
• whoa - corrects you when you say 'woah'
• `a!trans <from> <to> <text>` - Google Translates your text. Input `<from>` as `detect` for a detect language translation. (Same issues as `a!tb`)
• `a!zh <text>` - converts text to 匚卄工𠘨乇丂乇 乚乇丅丅乇尺丂''', colour = 0x7289da)
        await message.channel.send(embed = msg)
        if str(message.guild.id) == absr:
            await message.channel.send("**🚨 UPDATE:** Functions using Google Translate have been fixed, but with great limitations.\n*For a list of all functionalities, visit: https://ajlee2006.github.io/discbot*")
        else:
            await message.channel.send("**🚨 UPDATE:** Functions using Google Translate have been fixed, but with great limitations.\n*For a list of all functionalities, and to join the AndewBot server to receive more updates, visit: https://ajlee2006.github.io/discbot*")

    if message.content.lower() == 'unredeemed':
        print(pcmd)
        await message.channel.send('unredeemed')

    # greek
    if message.content.lower()[:8] == 'a!greek ' or message.content.lower()[:8] == 'α!γρεεκ ' or message.content.lower()[:4] == 'a!g ' or message.content.lower()[:4] == 'α!γ ':
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:8] == 'a!greek ' or message.content.lower()[:8] == 'α!γρεεκ ':
            s = message.content[8:]
        s = unicodedata.normalize('NFD', s)
        fin = ''
        greek = ':ΕΡΤΥΘΙΟΠΑΣΔΦΓΗΞΚΛΖΧΨΩΒΝΜ;ςερτυθιοπασδφγηξκλζχψωβνμς'
        eng = 'QERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmW'
        for i in s:
            if i in greek:
                fin += eng[greek.find(i)]
            elif i in eng:
                fin += greek[eng.find(i)]
            else:
                fin += i
        fin = unicodedata.normalize('NFC', fin)
        await message.channel.send(fin)

    if message.content.lower()[:5] == 'a!gl ' or message.content.lower()[:5] == 'α!γλ ':
        print(pcmd)
        s = message.content[5:]
        s = unicodedata.normalize('NFD', s)
        fin = ''
        grll = "ERTYUIOPASDFGHJKLZXCVBNMwertyuiopasdfghjklzxcvbnm"
        eng =  "EPTYOIOHAEAG7HEKAZXWOBNMceptu0ionaodgynEkAZxwwBvu"
        for i in unicodedata.normalize('NFD', s):
            if i in grll:
                fin += eng[grll.find(i)]
            else:
                fin += i
        fin = unicodedata.normalize('NFC', fin)
        await message.channel.send(fin)

    # whoa
    if (datetime.datetime.now(pytz.timezone('Etc/GMT-14')).month == 4 and datetime.datetime.now(pytz.timezone('Etc/GMT-14')).day == 1) or (datetime.datetime.now(pytz.timezone('Etc/GMT')).month == 4 and datetime.datetime.now(pytz.timezone('Etc/GMT')).day == 1) or (datetime.datetime.now(pytz.timezone('Etc/GMT+12')).month == 4 and datetime.datetime.now(pytz.timezone('Etc/GMT+12')).day == 1):
        if 'whoa' in message.content.lower():
            print(pcmd)
            await message.channel.send('*woah')
        if 'ςηοα' in message.content.lower():
            print(pcmd)
            await message.channel.send('*ςοαη')
    else:
        if 'woah' in message.content.lower():
            print(pcmd)
            await message.channel.send('*whoa')
        if 'ςοαη' in message.content.lower():
            print(pcmd)
            await message.channel.send('*ςηοα')
        if 'whoa' in message.content.lower():
            print(pcmd)
            await message.channel.send('✅ you used the right spelling of "whoa"')
        if 'ςηοα' in message.content.lower():
            print(pcmd)
            await message.channel.send('✅ υοθ θσεδ τηε ριγητ σπελλινγ οφ "ςηοα"')

    # say
    if message.content.lower()[:6] == "a!say " or message.content.lower()[:4] == "a!s ":
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:6] == 'a!say ':
            s = message.content[6:]
        await message.channel.send(s)

    '''
    if message.content.lower()[:8] == "a!say!s " or message.content.lower()[:6] == "a!s!s ":
        print(pcmd)
        s = message.content[6:]
        if message.content.lower()[:8] == 'a!say!s ':
            s = message.content[8:]
        await message.channel.send(''.join(i + '\U0000200B' for i in s))
    '''

    # googletrans
    if message.content.lower()[:8] == "a!trans " or message.content.lower()[:4] == "a!t ":
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:8] == 'a!trans ':
            s = message.content[8:]
        msg = ''
        translated = ''
        #fullnamelist = ['detect', 'afrikaans', 'albanian', 'arabic', 'azerbaijani', 'basque', 'bengali', 'belarusian', 'bulgarian', 'catalan', 'chinese', 'zh', 'chinese-simplified', 'chinese-traditional', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian-creole', 'hebrew', 'hindi', 'hungarian', 'icelandic', 'indonesian', 'irish', 'italian', 'japanese', 'kannada', 'korean', 'latin', 'latvian', 'lithuanian', 'macedonian', 'malay', 'maltese', 'norwegian', 'persian', 'polish', 'portuguese', 'romanian', 'russian', 'serbian', 'slovak', 'slovenian', 'spanish', 'swahili', 'swedish', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'vietnamese', 'welsh', 'yiddish']
        fullnamelist = ['detect', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'zh', 'chinese', 'chinese-simplified', 'chinese-traditional', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian-creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar', 'burmese', 'nepali', 'norwegian', 'nyanja', 'chichewa', 'odia', 'oriya', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots-gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'sinhalese', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tagalog', 'filipino', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']
        #shortformlist = ['', 'af', 'sq', 'ar', 'az', 'eu', 'bn', 'be', 'bg', 'ca', 'zh-cn', 'zh-cn', 'zh-cn', 'zh-tw', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'iw', 'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'kn', 'ko', 'la', 'lv', 'lt', 'mk', 'ms', 'mt', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk', 'sl', 'es', 'sw', 'sv', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'vi', 'cy', 'yi']
        shortformlist = ['', 'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'zh-cn', 'zh-cn', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'my', 'ne', 'no', 'ny', 'ny', 'or', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tl', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
        templist = s.lower().split()
        one = templist[0]
        two = templist[1]
        msg = s.split(' ', 2)[2]
        try:
            to = shortformlist[fullnamelist.index(two)]
        except:
            try:
                to = shortformlist[shortformlist.index(two)]
            except:
                await message.channel.send('Oops, ' + two + ' isn\'t a (supported) language.\nFor a list of supported languages, visit **https://ajlee2006.github.io/discbot/langlist.html**')
                return
        try:
            fr = shortformlist[fullnamelist.index(one)]
        except:
            try:
                fr = shortformlist[shortformlist.index(one)]
            except:
                await message.channel.send('Oops, ' + one + ' isn\'t a (supported) language.\nFor a list of supported languages, visit **https://ajlee2006.github.io/discbot/langlist.html**')
                return
        if to == '':
            await message.channel.send('Oops, you have to specify a target language.\nFor a list of supported languages, visit **https://ajlee2006.github.io/discbot/langlist.html**')
            return
        elif fr == '':
            await message.channel.send(json.loads(requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=&tl='+to+'&dt=t&q='+msg).text)[0][0][0])
            #await message.channel.send('\n'.join([json.loads(requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=&tl='+to+'&dt=t&q='+i).text)[0][0][0] for i in msg.split('\n')]))
        else:
            await message.channel.send(json.loads(requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl='+fr+'&tl='+to+'&dt=t&q='+msg).text)[0][0][0])
            #await message.channel.send('\n'.join([json.loads(requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl='+fr+'&tl='+to+'&dt=t&q='+i).text)[0][0][0] for i in msg.split('\n')]))
        '''
        if not bool(re.compile('^[a-z]{2} [a-z]{2} ').match(s.lower())):
            if not bool(re.compile('^[a-z]{2} ').match(s.lower())):
                await message.channel.send('Error!')
            else:
                to = s.lower()[:2]
                msg = s[3:]
                await message.channel.send(t.translate(msg, dest=to).text)
        else:
            fr = s.lower()[:2]
            to = s.lower()[3:5]
            msg = s[6:]
            await message.channel.send(t.translate(msg, src=fr, dest=to).text)
        '''
    if message.content.lower() == 'a!help!trans' or message.content.lower() == 'a!help!t' or message.content.lower() == 'a!h!trans' or message.content.lower() == 'a!h!t':
        print(pcmd)
        # msg = discord.Embed(title="List of languages supported by a!trans", description = '• detect [NOTE: only works for `<from>`]\n• afrikaans (af)\n• albanian (sq)\n• arabic (ar)\n• azerbaijani (az)\n• basque (eu)\n• bengali (bn)\n• belarusian (be)\n• bulgarian (bg)\n• catalan (ca)\n• chinese-simplified (zh-cn)\n• chinese-traditional (zh-tw)\n• croatian (hr)\n• czech (cs)\n• danish (da)\n• dutch (nl)\n• english (en)\n• esperanto (eo)\n• estonian (et)\n• filipino (tl)\n• finnish (fi)\n• french (fr)\n• galician (gl)\n• georgian (ka)\n• german (de)\n• greek (el)\n• gujarati (gu)\n• haitian-creole (ht)\n• hebrew (iw)\n• hindi (hi)\n• hungarian (hu)\n• icelandic (is)\n• indonesian (id)\n• irish (ga)\n• italian (it)\n• japanese (ja)\n• kannada (kn)\n• korean (ko)\n• latin (la)\n• latvian (lv)\n• lithuanian (lt)\n• macedonian (mk)\n• malay (ms)\n• maltese (mt)\n• norwegian (no)\n• persian (fa)\n• polish (pl)\n• portuguese (pt)\n• romanian (ro)\n• russian (ru)\n• serbian (sr)\n• slovak (sk)\n• slovenian (sl)\n• spanish (es)\n• swahili (sw)\n• swedish (sv)\n• tamil (ta)\n• telugu (te)\n• thai (th)\n• turkish (tr)\n• ukrainian (uk)\n• urdu (ur)\n• vietnamese (vi)\n• welsh (cy)\n• yiddish (yi)', colour = 0x#518ff5)
        await message.channel.send('For a list of supported languages, visit **https://ajlee2006.github.io/discbot/langlist.html**')

    # nick
    if message.content.lower()[:7] == "a!nick " or message.content.lower()[:4] == "a!n ":
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:7] == 'a!nick ':
            s = message.content[7:]
        await message.guild.me.edit(nick=s)
        await message.channel.send('Nickname changed to ' + s + '!')

    # feminists
    if ('man' in message.content.lower() or 'men' in message.content.lower() or 'male' in message.content.lower() or 'boy' in message.content.lower() or 'mascul' in message.content.lower()) and not message.author.bot:
        print(pcmd)
        words = message.content.lower().split()
        table = str.maketrans('', '', string.punctuation)
        wwm = [w.translate(table).lower() for w in words]
        wwmf = []
        njtm = []
        njtw = []
        for i in wwm:
            if 'men' in i and 'man' not in i and 'male' not in i and 'boy' not in i and 'mascul' not in i:
                j = re.sub(r'(?<!wo)men','women',i)
                k = re.sub(r'(?<!wo)men','children',i)
                njtm.append(i)
                njtw.append((j,k))
            else:
                j = re.sub(r'(?<!wo)men','women',i)
                j = re.sub(r'(?<!wo)man','woman',j)
                j = re.sub(r'(?<!fe)male','female',j)
                j = j.replace('boy','girl')
                j = j.replace('mascul','femin')
            wwmf.append(j)
        fin = []
        for i in range(len(wwm)):
            if wwm[i] != wwmf[i] and wwm[i] not in ['man','male','boy','manly','masculine','boyish'] and wwm[i] not in fin:
                if wwm[i] not in njtm:
                    await message.channel.send('When feminists realise it\'s ' + wwm[i] + ' not ' + wwmf[i])
                else:
                    await message.channel.send('Not just the ' + wwm[i] + ', but the ' + njtw[njtm.index(wwm[i])][0] + ' and the ' + njtw[njtm.index(wwm[i])][1] + ' too!')
                fin.append(wwm[i])

    # hi dad
    if str(message.author.id) == dad:
        print(pcmd)
        if datetime.datetime.now(pytz.timezone('Etc/GMT-14')).date() == datetime.date(datetime.datetime.now(pytz.timezone('Etc/GMT-14')).year, 6, 15).replace(day=(15 + (6 - datetime.date(datetime.datetime.now(pytz.timezone('Etc/GMT-14')).year, 6, 15).weekday()) % 7)) or datetime.datetime.now(pytz.timezone('Etc/GMT')).date() == datetime.date(datetime.datetime.now(pytz.timezone('Etc/GMT')).year, 6, 15).replace(day=(15 + (6 - datetime.date(datetime.datetime.now(pytz.timezone('Etc/GMT')).year, 6, 15).weekday()) % 7)) or datetime.datetime.now(pytz.timezone('Etc/GMT+12')).date() == datetime.date(datetime.datetime.now(pytz.timezone('Etc/GMT+12')).year, 6, 15).replace(day=(15 + (6 - datetime.date(datetime.datetime.now(pytz.timezone('Etc/GMT+12')).year, 6, 15).weekday()) % 7)):
            await message.channel.send('Happy Father\'s Day, Dad!')
        else:
            if message.content[:3] == 'Hi ' and ', I\'m ' in message.content:
                if '{0.author.display_name}'.format(message) == 'Dad Bot' and message.content[-5:] == " Dad!":
                    await message.channel.send('Hi Dad!')
                else:
                    await message.channel.send('Hi ' + '{0.author.display_name}'.format(message) + '!')

    # hindi
    if bool(re.search('[\u0900-\u097F]', message.content.lower())) or 'hindi' in message.content.lower():
        await message.channel.send('Speak Hindi – If you don\'t use it, you will lose it!')

    # xue hua piao piao
    if message.content == '雪花飘飘':
        await message.channel.send('北风啸啸')
    if message.content.lower() == 'xue hua piao piao':
        await message.channel.send('bei feng xiao xiao')
    if message.content.lower() == 'xuehuapiaopiao':
        await message.channel.send('beifengxiaoxiao')
    if message.content.lower() == 'xhpp':
        await message.channel.send('bfxx')

    # lorem ipsum
    if "lorem" in wwm:
        print(pcmd)
        await message.channel.send('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    # mr foo bball
    if str(message.author.id) == tyl:
        print(pcmd)
        await message.add_reaction('\U0001F3C0')
        await message.add_reaction('\u26f9')
        #await message.channel.send('Do you play basketball?')

    # funny number
    #<@& <@! <#
    if '69' in re.sub(r'<.+>', '', message.content):
        print(pcmd)
        await message.channel.send('haha 69 funny number lololololz')
    if '420' in re.sub(r'<.+>', '', message.content):
        print(pcmd)
        await message.channel.send('lolz 420 smoke weed lmao hahahahahah')

    # east coast
    if 'east' in wwm or 'coast' in wwm:
        print(pcmd)
        await message.channel.send('For our East Coast residents, the, we also have a plan for the East Coast. We have a East Coast, Singapore, uh we have a together, an East Coast plan. We care at East Coast.')

    if message.content.lower()[:4] == 'a!d ' or message.content.lower()[:12] == 'a!diacritic ':
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:12] == 'a!diacritic ':
            s = message.content[12:]
        sep = s.split()[0]
        if not bool(re.search(r"(?<!\\)(\\\\)*'", message.content.lower())):
            sep = eval("'" + sep + "'")
        s = s.split(' ', 1)[1]
        await message.channel.send(unicodedata.normalize('NFC',''.join([i + sep for i in s])))

    if message.content.lower()[:6] == 'a!md5 ':
        print(pcmd)
        s = message.content[6:]
        await message.channel.send(hashlib.md5(s.encode('utf-8')).hexdigest())

    if message.content.lower()[:4] == 'a!z ' or message.content.lower()[:8] == 'a!zalgo ':
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:8] == 'a!zalgo ':
            s = message.content[8:]
        s = zalgo.zalgo().zalgofy(s)
        '''
        for i in range(0, len(s), 2000):
            await message.channel.send(s[i:i+2000])
        '''
        await message.channel.send(unicodedata.normalize('NFC',s))

    if message.content.lower()[:7] == 'a!hypy ':
        print(pcmd)
        s = message.content[7:]
        g = eval(requests.get('https://www.google.com/inputtools/request?ime=pinyin&ie=utf-8&oe=utf-8&app=translate&num=10&text=' + s).text)
        try:
            await message.channel.send(g[1][0][1][0])
        except:
            await message.channel.send("Something went wrong.")

    if message.content.lower()[:11] == 'a!presence ' and str(message.author.id) == ajl:
        print(pcmd)
        s = message.content[11:]
        game = discord.Game(s)
        await client.change_presence(status=discord.Status.idle, activity=game)

    # rocket man
    if str(message.author.id) == cmy:
        print(pcmd)
        await message.add_reaction('\U0001F680')
        await message.add_reaction('\U0001F388')
        #await message.channel.send('ok rocket man')

    if str(message.author.id) == drew:
        print(pcmd)
        await message.add_reaction('\u0036\u20E3')
        await message.add_reaction('\u0032\u20E3')

    if str(message.author.id) == eewn:
        print(pcmd)
        await message.add_reaction('\U0001F32D')

    if message.content.lower()[:4] == 'a!w ' or message.content.lower()[:8] == 'a!weird ':
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:8] == 'a!weird ':
            s = message.content[8:]
        f = open('confusables.txt','r')
        confusablesdict = defaultdict(list)
        for line in f:
            try:
                l = line.split(';')
                wrong = l[0].strip()
                right = l[1].strip()
                confusablesdict[chr(int(right,16))].append(chr(int(wrong,16)))
            except:
                pass
        fakestring = ''
        for i in s:
            fakestring += '\u202d'
            if confusablesdict[i] == []:
                fakestring += i
            else:
                fakestring += random.choice(confusablesdict[i])
        await message.channel.send(fakestring)

    if message.content.lower()[:7] == 'a!eval ' and str(message.author.id) == ajl:
        print(pcmd)
        s = message.content[7:]
        await message.channel.send(str(eval(s)))

    if message.content.lower()[:7] == 'a!exec ' and str(message.author.id) == ajl:
        print(pcmd)
        s = message.content[7:]
        exec(s)

    if message.content.lower()[:8] == 'a!embed ':
        print(pcmd)
        s = message.content[8:].split("\n", 1)
        await message.channel.send(embed = discord.Embed(title = s[0], description = s[1]))

    if 'beauty world' in ' '.join(wwm):
        print(pcmd)
        await message.channel.send('cha cha cha')

    if message.content.lower()[:7] == 'a!pron ':
        print(pcmd)
        s = message.content[7:]
        t = Translator()
        await message.channel.send(t.translate(s, dest=t.detect(s).lang).pronunciation)
        await message.channel.send("This function no longer works.")

    # no more dough.
    '''
    if 'dough' in message.content.lower():
        print(pcmd)
        await message.channel.send('How well **‘dough’** you know yourself?')
    if 'eye' in wwm and str(message.guild.id) in [tos,bt,absr,ho]:
        print(pcmd)
        await message.channel.send('**‘eye’**-dentification')
    if 'egg' in wwm and str(message.guild.id) in [tos,bt,absr,ho]:
        print(pcmd)
        await message.channel.send('**‘egg**-cellent’')

    if ('do' in message.content.lower() or 'to' in message.content.lower() or 'the' in message.content.lower() or 'iden' in message.content.lower() or 'exc' in message.content.lower() or 'wow' in message.content.lower()) and not message.author.bot and str(message.guild.id) in [tos,bt,absr,ho]:
        print(pcmd)
        j = re.sub(r'\bdo not\b','**‘doughnut’**',message.content)
        j = re.sub(r'\bDo not\b','**‘Doughnut’**',j)
        j = re.sub(r'do(?!ugh)','**‘dough’**',j)
        j = re.sub(r'Do(?!ugh)','**‘Dough’**',j)
        j = re.sub(r'to','**‘dough’**',j)
        j = re.sub(r'To','**‘Dough’**',j)
        j = re.sub(r'\bthe\b','**‘dough’**',j)
        j = re.sub(r'\bThe\b','**‘Dough’**',j)
        j = re.sub(r'iden','**‘eye’**den',j)
        j = re.sub(r'Iden','**‘Eye’**den',j)
        j = re.sub(r'exc','**‘egg’**c',j)
        j = re.sub(r'Exc','**‘Egg’**c',j)
        j = re.sub(r'(?i)wow','**W@W**',j)
        if j != message.content:
            await message.channel.send("More like, “" + j + "”")
    '''

    if wwm == ['k']:
        print(pcmd)
        await message.channel.send('K? K what? The letter before L? The letter after J? Did you know that in JK the K stands for “kidding?” So your reply is “kidding?” or K as in Potassium? Do you need some Special K for breakfast? K as in I can K/O you? Can I knock you out and feed you to hungry sharks? Sharks have a K in it. "K"? Are you kidding me? I spent a decent portion of my life writing all of that and your response to me is "K"? Are you so mentally handicapped that the only letter you can comprehend is "K" - or are you just some f\\*cking asshole who thinks that with such a short response, he can make a statement about how meaningless what was written was? Well, I\'ll have you know that what I wrote was NOT meaningless. Don\'t believe me? I doubt you would, and your response to this will probably be "K" once again. Do I give a f\\*ck? No, does it look like I give even the slightest f\\*ck about a single letter? I bet you took the time to type that one letter too, I bet you sat there and chuckled to yourself for 20 hearty seconds before pressing "send". You\'re so f\\*cking pathetic. I\'m honestly considering directing you to a psychiatrist, but I\'m simply far too nice to do something like that. You, however, will go out of your way to make a fool out of someone by responding to a well-thought-out, intelligent, or humorous statement that probably took longer to write than you can last in bed with a chimpanzee. What do I have to say to you? Absolutely nothing. I couldn\'t be bothered to respond to such a worthless attempt at a response. Do you want "K" on your gravestone? Do you want people to remember you as the asshat who one day decided to respond to someone with a single letter? "Hey, look, everybody! It\'s that "K" guy!" That\'s who you are. You\'re going to be known as the "K" guy. How does it feel? Do you feel happy? Quite honestly, I don\'t care, which is why I\'m not even going to respond to you. Goodbye, and good luck with your future as that guy who said "K".')

    if message.content == "J":
        print(pcmd)
        await message.add_reaction('\u263A')

    if "brazil" in message.content.lower():
        print(pcmd)
        brazillist = eval(open('brazillist.txt', 'r').read())
        await message.channel.send(random.choice(brazillist))

    if wwm == ['whos','joe']:
        print(pcmd)
        await message.channel.send(random.choice(["Joe Biden","Joe mama","Catherine Eugenia Finnegan"]))
    elif 'joe' in message.content.lower():
        print(pcmd)
        l = ["Who's Joe? Joe mama","Who's Joe? Joe mama","Who's Joe? Joe Biden","Who's Joe? Catherine Eugenia Finnegan","Will you shut up, man"]
        if message.guild.id in [tos,bt,absr,ho]:
            l.append("Who's dough? Dough mama")
        await message.channel.send(random.choice(l))

    if message.content.lower()[:5] == 'a!zh ':
        print(pcmd)
        s = unicodedata.normalize('NFD', message.content[5:])
        fin = ''
        zh = '卂乃匚刀乇下厶卄工丁长乚从𠘨口尸㔿尺丂丅凵リ山乂丫乙卂乃匚刀乇下厶卄工丁长乚从𠘨口尸㔿尺丂丅凵リ山乂丫乙'
        eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        for i in s:
            if i in zh:
                fin += eng[zh.find(i)]
            elif i in eng:
                fin += zh[eng.find(i)]
            else:
                fin += i
        fin = unicodedata.normalize('NFC', fin)
        await message.channel.send(fin)

    if message.content.lower()[:5] == 'a!tb ':
        print(pcmd)
        message1 = await message.channel.send("Translating, please wait...")
        text = message.content[5:]
        lst = ['en','ko','ja','ms','he','eu','zh-cn','ar','sw','am','th','en']
        for i in range(1,len(lst)):
            text = json.loads(requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl='+lst[i-1]+'&tl='+lst[i]+'&dt=t&q='+text).text)[0][0][0]
        await message1.edit(content=text)

    if 'ok ya' in message.content.lower() or 'okya' in message.content.lower():
        print(pcmd)
        await message.channel.send("okya")

    if message.content.lower()[:7] == 'a!chia ' or message.content.lower()[:4] == 'a!c ':
        print(pcmd)
        text = message.content[4:]
        if message.content.lower()[:7] == 'a!chia ':
            text = message.content[7:]
        text = regex.sub(r'(?<=\b\w{6,}\b)(?![\.!\?,;:])', lambda op: random.choice(['-tsa','','-tsa, okya,','',', okya,']), text, flags=regex.IGNORECASE)
        text = regex.sub(r'(?<!\b(okya|ok|ya)\s*)(?<!-tsa\s*),(?!\s*(ya|okya|ok)\b)', lambda op: random.choice(['-tsa, okya,',', okya,','-tsa, ok,',', ok,',',']), text, flags=regex.IGNORECASE)
        text = regex.sub(r'(?<!\b(okya|ok|ya)\s*)(?<!-tsa\s*);(?!\s*(ya|okya|ok)\b)', lambda op: random.choice(['-tsa, okya;',', okya;','-tsa, ok;',', ok;',';']), text, flags=regex.IGNORECASE)
        text = regex.sub(r'(?<!\b(okya|ok|ya)\s*)(?<!-tsa\s*):(?!\s*(ya|okya|ok)\b)', lambda op: random.choice(['-tsa, okya:',', okya:','-tsa, ok:',', ok:',':']), text, flags=regex.IGNORECASE)
        text = regex.sub(r'(?<!\b(okya|ok|ya)\s*)(?<!-tsa\s*)\.(?!\s*(ya|okya|ok)\b)', lambda op: random.choice(['-tsa, okya.','-tsa, ok, ya.','-tsa, ok.','-tsa-okya.',', ok.',', okya.',', ok. Ya.','.']), text, flags=regex.IGNORECASE)
        text = regex.sub(r'(?<!\b(okya|ok|ya)\s*)(?<!-tsa\s*)!(?!\s*(ya|okya|ok)\b)', lambda op: random.choice(['. Ya!','-tsa. Ya!',', ok, ya!','-tsa, ok, ya!',', ok. Ya!','-tsa, ok. Ya!','! Okya.','!']), text, flags=regex.IGNORECASE)
        text = regex.sub(r'(?<!\b(okya|ok|ya)\s*)(?<!-tsa\s*)\?(?!\s*(ya|okya|ok)\b)', lambda op: random.choice(['? Mm, okya.','-tsa?','-tsa? Okya.','? Okya.','?']), text, flags=regex.IGNORECASE)
        await message.channel.send(text)

    if message.content.lower()[:6] == 'a!esp ':
        print(pcmd)
        s = message.content[6:]
        ipalist = ['m', 'n', 'ŋ', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'x', 'h', 'l', 'r', 'j', 'w', 'a', 'æ', 'ɑ', 'ɒ', 'ɔ', 'i', 'ɪ', 'e', 'ɛ', 'ɜ', 'ə', 'o', 'u', 'ʌ', 'ʊ', 'ʧ', 'ʤ', 'ˌ', 'ˈ', '*', 'ː']
        esplist = ['m', 'n', 'ng', 'p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 't', 't', 's', 'z', 'ŝ', 'ĵ', 'ĥ', 'h', 'l', 'r', 'j', 'ŭ', 'a', 'e', 'a', 'a', 'o', 'i', 'i', 'e', 'e', 'a', 'e', 'o', 'u', 'e', 'u', 'ĝ', 'ĉ', '', '', '', '']
        pron = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": s}).text
        pron = pron.replace('ts','c')
        fs = ''
        for i in pron:
            if i in ipalist:
                fs += esplist[ipalist.index(i)]
            else:
                fs += i
        fs = fs.replace('ai','aj')
        fs = fs.replace('ei','ej')
        fs = fs.replace('oi','oj')
        fs = fs.replace('ui','uj')
        fs = fs.replace('au','aŭ')
        fs = fs.replace('eu','eŭ')
        fs = fs.replace('iu','iŭ')
        fs = fs.replace('ou','oŭ')
        s = s.replace('\u0007','').replace('\n','\u0007 ')
        f = fs.replace('\u0007','').replace('\n','\u0007 ')
        fl = f.split(' ')
        sl = s.split(' ')
        for i in range(len(sl)):
            try:
                if sl[i] == sl[i].capitalize():
                    fl[i] = fl[i].capitalize()
                elif sl[i].isupper():
                    fl[i] = fl[i].upper()
                elif sl[i].islower():
                    fl[i] = fl[i].lower()
            except:
                pass
        await message.channel.send(' '.join(fl).replace('\u0007 ','\n'))

    if message.content.lower()[:6] == 'a!vot ':
        print(pcmd)
        s = message.content[6:]
        ipalist = ['m', 'n', 'ŋ', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'x', 'h', 'l', 'r', 'j', 'w', 'a', 'æ', 'ɑ', 'ɒ', 'ɔ', 'i', 'ɪ', 'e', 'ɛ', 'ɜ', 'ə', 'o', 'u', 'ʌ', 'ʊ', 'ʤ', 'ʧ', 'ˌ', 'ˈ', '*', 'ː']
        votlist = ['m', 'n', 'q', 'p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'x', 'ð', 's', 'z', 'c', 'j', 'h', 'h', 'l', 'r', 'y', 'w', 'a', 'a', 'ö', 'ö', 'u', 'y', 'i', 'e', 'e', 'r', 'r', 'o', 'w', 'u', 'w', 'dj', 'tc', '', '', '', '']
        pron = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": s}).text
        pron = pron.replace('ts','c')
        fs = ''
        for i in pron:
            if i in ipalist:
                fs += votlist[ipalist.index(i)]
            else:
                fs += i
        s = s.replace('\u0007','').replace('\n','\u0007 ')
        f = fs.replace('\u0007','').replace('\n','\u0007 ')
        fl = f.split(' ')
        sl = s.split(' ')
        for i in range(len(sl)):
            try:
                if sl[i] == sl[i].capitalize():
                    fl[i] = fl[i].capitalize()
                elif sl[i].isupper():
                    fl[i] = fl[i].upper()
                elif sl[i].islower():
                    fl[i] = fl[i].lower()
            except:
                pass
        await message.channel.send(' '.join(fl).replace('\u0007 ','\n'))

    if message.content.lower()[:6] == 'a!pol ':
        print(pcmd)
        s = message.content[6:].strip()
        ipalist = ['m', 'n', 'ŋ', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'x', 'h', 'l', 'r', 'j', 'w', 'a', 'æ', 'ɑ', 'ɒ', 'ɔ', 'i', 'ɪ', 'e', 'ɛ', 'ɜ', 'ə', 'o', 'u', 'ʌ', 'ʊ', 'ʤ', 'ʧ', 'ˌ', 'ˈ', '*', 'ʔ']
        pollist = ['m', 'n', 'ng', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 't̂', 'ψ', 's', 'z', 'ŝ', 'ĵ', 'ĥ', 'h', 'l', 'r', 'j', 'ŭ', 'a', 'ⱥ', 'a', 'w', 'w', 'i', 'ĭ', 'e', 'ⱥ', 'q', 'x', 'o', 'u', 'q', 'u', 'ĝ', 'ĉ', '', '', '', '']
        pron = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": s}).text
        fs = ''
        for i in pron:
            if i in ipalist:
                fs += pollist[ipalist.index(i)]
            else:
                fs += i
        fs = fs.replace('kts','ẑ')
        fs = fs.replace('gdz','z̆')
        fs = fs.replace('ts','c')
        fs = re.sub('h([mnbk])', r'\1̆', fs)
        fs = fs.replace('pŭ','φ')
        fs = re.sub('([aeiouⱥĭwqxː])[iĭ]', r'\1j', fs)
        fs = re.sub('([aeioⱥĭwqxː])uŭ', r'\1ŭ', fs)
        fs = re.sub('([aeioⱥĭwqxː])u', r'\1ŭ', fs)
        fs = re.sub('ŭj([mnpbtdkgfvt̂ψszŝĵĥhlrjcφ])', r'ŭi\1', fs)
        fs = fs.replace('ː',':')
        s = s.replace('\u0007','').replace('\n','\u0007 ')
        f = fs.replace('\u0007','').replace('\n','\u0007 ')
        fl = f.split(' ')
        sl = s.split(' ')
        for i in range(len(sl)):
            try:
                if sl[i].upper() == sl[i].lower():
                    pass
                elif sl[i].islower():
                    fl[i] = fl[i].lower()
                elif sl[i] == sl[i].capitalize():
                    fl[i] = fl[i].capitalize()
                elif sl[i].isupper():
                    fl[i] = fl[i].upper()
            except:
                pass
        await message.channel.send(' '.join(fl).replace('\u0007 ','\n'))

    if message.content.lower()[:7] == 'a!viet ':
        print(pcmd)
        s = message.content[7:].strip()
        ipalist = ['m', 'n', 'ŋ', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'x', 'h', 'l', 'r', 'j', 'w', 'a', 'æ', 'ɑ', 'ɒ', 'ɔ', 'i', 'ɪ', 'e', 'ɛ', 'ɜ', 'ə', 'o', 'u', 'ʌ', 'ʊ', 'ʤ', 'ʧ', 'ˌ', 'ˈ', '*', 'ʔ', 'ː']
        vietlist = ['m', 'n', ['ng','ngh','nh'], 'p', 'b', 't', 'đ', ['c','k','q'], ['g','gh'], 'ph', 'v', 't', 'đ', ['s','x'], ['d','gi','r'], ['s','x'], ['d','gi','r'], 'kh', 'h', 'l', 'r', ['y','i'], ['u','o'], ['ă','a'], ['a','e'], ['ă','a'], 'o', 'o', ['i','y'], ['ư','i','y'], 'ê', 'e', ['ă','a'], ['â','ơ'], 'ô', 'u', ['ă','a'], 'u', ['ts','tx'], ['đd','đgi','đr'], '', '', '', '', '']
        pron = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": s}).text
        fs = ''
        for i in pron:
            if i in ipalist:
                if isinstance(vietlist[ipalist.index(i)], list):
                    fs += random.choice(vietlist[ipalist.index(i)])
                else:
                    fs += vietlist[ipalist.index(i)]
            else:
                fs += i
        fs = fs.replace('()','')
        s = s.replace('\u0007','').replace('\n','\u0007 ')
        f = fs.replace('\u0007','').replace('\n','\u0007 ')
        fl = f.split(' ')
        sl = s.split(' ')
        for i in range(len(sl)):
            try:
                if sl[i].upper() == sl[i].lower():
                    pass
                elif sl[i].islower():
                    fl[i] = fl[i].lower()
                elif sl[i] == sl[i].capitalize():
                    fl[i] = fl[i].capitalize()
                elif sl[i].isupper():
                    fl[i] = fl[i].upper()
            except:
                pass
        await message.channel.send(' '.join(fl).replace('\u0007 ','\n'))

    if message.content.lower()[:7] == 'a!mock ':
        print(pcmd)
        s = message.content[7:].strip()
        s = unicodedata.normalize('NFD',s)
        fin = ''
        up = False
        for i in s:
            if i.upper() != i.lower():
                if i.lower() == 'i':
                    fin += 'i'
                    up = True
                elif i.lower() == 'l':
                    fin += 'L'
                    up = False
                else:
                    if up:
                        fin += i.upper()
                    else:
                        fin += i.lower()
                    up = not up
            else:
                fin += i
                if i.isspace():
                    up = False
        await message.channel.send(unicodedata.normalize('NFC',fin))

    if message.content.lower()[:6] == 'a!ipa ':
        print(pcmd)
        await message.channel.send(requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": message.content[6:]}).text)

    if message.channel.name == "blaze-it": #message.author.discriminator == "0000" and 
        await message.publish()

    if "blaze" in message.content.lower():
        await message.add_reaction('\U0001F525')
    
    if message.content.lower()[:4] == 'a!i ' or message.content.lower()[:14] == 'a!impersonate ':
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:14] == 'a!impersonate ':
            s = message.content[14:]
        msg = shlex.split(s)
        #print(msg)
        webhooks = await message.channel.webhooks()
        #print(len(webhooks))
        
        webhook = None
        for awebhook in webhooks:
            if awebhook.token is not None and awebhook.name == "impersonator":
                webhook = awebhook
        if webhook is None:
            webhook = await message.channel.create_webhook(name="impersonator")

        username = msg[0]
        avatar_url = None
        content = msg[1]
        embed = None

        contentis = 1

        if re.match('<@!?[0-9]+>',username):
            userid = int(re.search('<@!?([0-9]+)>',msg[0]).group(1))
            #print(userid)
            userpinged = await message.guild.query_members(user_ids=[userid])
            userpinged = userpinged[0]
            #print(userpinged)
            username = userpinged.nick
            #print(userpinged.nick)
            if username == None:
                username = userpinged.name
                #print(userpinged.name)
            avatar_url = userpinged.avatar_url

        if re.match(urlregex, content.strip()) is not None:
            avatar_url = content
            content = msg[2]
            contentis = 2

        if content == "embed":
            content = ""
            colour = discord.Colour.blurple()
            if len(msg) > contentis+3 and msg[contentis+3].isdigit() and int(msg[contentis+3]) < 16777216:
                colour = discord.Colour(int(msg[contentis+3]))
            embed = discord.Embed(title=msg[contentis+1], description=msg[contentis+2], colour=colour)

        # attachments
        files = None
        if message.attachments != None and len(message.attachments) > 0:
            files = [await i.to_file() for i in message.attachments]

        await webhook.send(content=content, username=username, avatar_url=avatar_url, embed=embed, files=files)

        if msg[-1] == "delete":
            await message.delete()
            
    if "charge" in message.content.lower():
        await message.add_reaction('\U0001F50C')
        await message.add_reaction('\u26a1')
        
    if "pld" in message.content.lower():
        await message.add_reaction('\U0001F4BB')

    # python
    '''
    if message.content.lower()[:5] == "a!py " or message.content.lower()[:4] == "a!p ":
        print(pcmd)
        s = message.content[4:]
        if message.content.lower()[:5] == 'a!py ':
            s = message.content[5:]
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        try:
            exec(s)
        except:
            pass
        sys.stdout = old_stdout
        whatWasPrinted = buffer.getvalue()
        if bool(whatWasPrinted) == False:
            try:
                whatWasPrinted = exec(s)
            except:
                pass
        if bool(whatWasPrinted) == False:
            try:
                whatWasPrinted = eval(s)
            except:
                pass
        if bool(whatWasPrinted) == False:
            old_stdout = sys.stdout
            sys.stdout = buffer = io.StringIO()
            try:
                whatWasPrinted = exec("print(" + s + ")")
            except:
                pass
            sys.stdout = old_stdout
            whatWasPrinted = buffer.getvalue()
        whatWasPrinted = '{0}'.format(whatWasPrinted)
        print(whatWasPrinted)
        await message.channel.send(whatWasPrinted)
    '''

@client.event
async def on_reaction_add(reaction, user):
    try:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(str(user) + ' just reacted {0} to "{0.message.content}" in {0.message.guild}#{0.message.channel}'.format(reaction))
    except:
        pass
    try:
        if not message.author.bot:
            await reaction.message.add_reaction(str(reaction))
    except:
        pass

'''
@client.event
async def on_message_delete(message):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('{0.author} just deleted "{0.content}" in {0.guild}#{0.channel}'.format(message))
    await message.channel.send('<@{0.author.id}>\'s message was deleted:\n> {0.content}'.format(message))
'''

client.run(os.environ.get("DISCBOT_TOKEN"))
