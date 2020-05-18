from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime
import random #ランダムモジュール忘れずに
import asyncio #なんか必要らしい

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =698653628176531478  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')

    
    
# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '00:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('☆ワタシワエアドロップロボット‼:robot:☆Airdropの方法は適当にコメントする様にプロクラムされています。\nとても簡単!\nいつコメントするかは分かりません。CMD（Command）も変わったりします。お楽しみに♪気長にまたコメントします:star2: \n @everyone :airplane:') 
    
    if now == '00:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('?☆I"m Mini Airdrop-BOT‼ :robot: I am an Airdrop robot! The Airdrop method is programmed for appropriate comments. \ n Very easy! I don”t know when to comment. The CMD also changes. looking forward to☆I will comment again generously. \n @everyone :airplane:')  
       
    if now == '02:08':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('?フフフモウイチドイイマス☆ワタシワエアドロップロボット‼:robot:☆Airdropの方法は適当にコメントする様にプロクラムされています。\nとても簡単!\nいつコメントするかは分かりません。CMDも変わったりします。お楽しみに:star2: \n @everyone :airplane:') 
    
    if now == '02:09':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Say again.hehe ☆I"m Mini Airdrop-BOT‼ :robot: I am an Airdrop robot! The Airdrop method is programmed for appropriate comments. \n Very easy! I don”t know when to comment. The CMD also changes. looking forward to☆ \n @everyone :airplane:')  
    
    if now == '02:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('キナガニキイテクダサイネ:robot: HELLO!さて、 Airdrop方法は、ダイスです:game_die:！\n 指定のコマンドで、0～100までの数字をランダムに出します。その数字によって当たりが違います。\n :airplane: Airdrop賞が【0.1.77.100番】の4/100の確率です。Balloon賞、mini Drop賞 未公開の賞など複数の暗号通貨で構成されています。★リップル（XRP）もリスティングされています。\n 1回当たりの獲得枚数は、少額ですが回数重ねると大きいものです。\n BOT残高がなくなったら　おしまい...です。わかりましたか？適当な説明でした<:niko_shita:699072695823892561> 　:airplane::robot:')  

    if now == '02:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Please listen for a long time:robot:　HELLO! Airdrop method is dice:game_die:! The specified command will randomly output a number from 0 to 100. \n The number depends on the number. \n :airplane: The Airdrop award is the establishment of 4/100 of [0.1.77.100]:star2:. \n It is composed of multiple cryptocurrencies such as the Balloon Award and mini Drop Award. ★Ripple (XRP) is also listed.\n The number of coins you can get each time is small, but the number of times you get it is large. \n When the BOT balance is exhausted, it is the end ... Did you understand? It was a brief explanation.<:niko_shita:699072695823892561> 　:airplane::robot::')

    if now == '02:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: ゲームは簡単でサイコロ:game_die:振るだけ！エアドロップCommandは【+】から始まります。半角英数小文字でさて何でしょう！？【+●●●】`+???` \n  :white_check_mark:ヒント①`+`は、元気がなくなってきた国を応援する気持ちのプラス。\n :white_check_mark:ヒント②2020年オリンピックが2021年延期しましたね。でも大丈夫かな？残念だけど仕方ない。\n:white_check_mark:ヒント③その国の通貨を意味します。+●●●ならそのスペルに関係します。以上。\n 周りに教えずにCommand打てば削除して下さいね。残高なくなれば終了する予定です。\n :robot:AirdropRobo専用チャンネルでコマンドは入れてください。\n　回数制限もうけてないから適度な回数でおねがいします。テキドナカイスウデ...:robot:') 
    
    if now == '02:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: The game is easy, just roll the dice:game_die:! Air Drop Command starts with [+]. What is it in half-width English letters!? 【+●●●】`+???` \n :white_check_mark: hint①:The `+` is a plus of the feeling of supporting a country that has become less energetic. \n :white_check_mark:hint②：The 2020 Olympics have been postponed to 2021. But is it okay? Unfortunately it can"t be helped.. \n:white_check_mark:hint③： \n It means the currency of the country. + ●●● is related to the spell. that"s all. \n Please delete it by typing Command without telling others. It will end when the balance is exhausted.\n Please enter the command on the :robot:AirdropRobo dedicated channel.\n Since there is no limit on the number of times, please give me an appropriate number of times...... :robot:')  

    if now == '02:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: ◆ :game_die: :robot: コマンドは↓ここのRainRoomじゃなく下のこちらの部屋でお願いします↓For commands, please click here 　↓　\n  #╰🤖airdrop-robo🆕..この部屋でお願いします。I would like the command in this room :robot:') 
    
    if now == '02:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: あっ！言い忘れていました！ｺﾏﾝﾄﾞは途中で変わったりします。動いている時間も不特定です。私を見つけたらｺﾏﾝﾄﾞで呼び出して下さいね☆回数制限はありませんが、連続するとボロだから..ロボでした(〃艸〃)ﾑﾌｯ止まります。ゆっくりと迷惑かからないようにお願いします。:star2:') 
    
    if now == '02:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: Ah! I forgot! The command may change on the way. The time of movement is unspecified. If you find me, please call me with a command ☆ There is no limit on the number of times, but if you continue, it will be boro .. It was a robot (〃 艸 〃) It stops. Please do not be a nuisance slowly.:star2:') 

    if now == '07:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:..:robot:..Please wait..:robot:\n/rain BGPT 7 ALL  :robot:') 
    
    if now == '07:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:..:デハカイセツシマス/ Let me explain:robot:') 
                           
    if now == '07:27':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: ゲームは簡単でサイコロ:game_die:振るだけ！エアドロップCommandは【+】から始まります。半角英数小文字でさて何でしょう！？【+●●●】`+???` \n  :white_check_mark:ヒント①`+`は、元気がなくなってきた国を応援する気持ちのプラス。\n :white_check_mark:ヒント②2020年オリンピックが2021年延期しましたね。でも大丈夫かな？残念だけど仕方ない。\n:white_check_mark:ヒント③その国の通貨を意味します。+●●●ならそのスペルに関係します。以上。\n 周りに教えずにCommand打てば削除して下さいね。残高なくなれば終了する予定です。\n :robot:AirdropRobo専用チャンネルでコマンドは入れてください。\n　回数制限もうけてないから適度な回数でおねがいします。テキドナカイスウデ...:robot:') 
    
    if now == '07:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: The game is easy, just roll the dice:game_die:! Air Drop Command starts with [+]. What is it in half-width English letters!? 【+●●●】`+???` \n :white_check_mark: hint①:The `+` is a plus of the feeling of supporting a country that has become less energetic. \n :white_check_mark:hint②：The 2020 Olympics have been postponed to 2021. But is it okay? Unfortunately it can"t be helped.. \n:white_check_mark:hint③： \n It means the currency of the country. + ●●● is related to the spell. that"s all. \n Please delete it by typing Command without telling others. It will end when the balance is exhausted.\n Please enter the command on the :robot:AirdropRobo dedicated channel.\n Since there is no limit on the number of times, please give me an appropriate number of times...... :robot:')  

    if now == '07:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: ◆ :game_die: :robot: コマンドは↓レインルームじゃなく↓こちらでお願いします↓For commands, please click here 　↓　\n  #╰🤖airdrop-robo🆕..cmd I would like the command in this room :robot:') 
    
    if now == '07:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: あっ！言い忘れていました！ｺﾏﾝﾄﾞは途中で変わったりします。動いている時間も不特定です。私を見つけたらｺﾏﾝﾄﾞで呼び出して下さいね☆回数制限はありませんが、連続するとボロだから..ロボでした(〃艸〃)ﾑﾌｯ止まります。ゆっくりと迷惑かからないようにお願いします。:star2:') 
    
    if now == '07:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: Ah! I forgot! The command may change on the way. The time of movement is unspecified. If you find me, please call me with a command ☆ There is no limit on the number of times, but if you continue, it will be boro .. It was a robot (〃 艸 〃) It stops. Please do not be a nuisance slowly.:star2:') 

    if now == '07:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:..... \n/throw BGPT 80 8 EquallyDistributed  <:good01:699581068285706301> Play with BGPT Slot Games～:star2:')  
    
    if now == '10:55':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('☆ワタシハエアドロップBOT‼:robot:☆AirdropGameの方法は適当にコメントする様にプロクラムされています。\nとても簡単!\nいつコメントするかは分かりません。CMDも変わったりします。お楽しみに:star2:') 
    
    if now == '10:56':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('☆I"m Mini Airdrop-BOT‼ :robot: I am an Airdrop robot! The Airdrop method is programmed for appropriate comments. \ n Very easy! I don”t know when to comment. The CMD also changes. looking forward to:star2:')  
    
    if now == '11:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('キナガニキイテクダサイネ:robot: HELLO!さて、 Airdrop方法は、ダイスです:game_die:！\n 指定のコマンドで、0～100までの数字をランダムに出します。その数字によって当たりが違います。\n :airplane: Airdrop賞が【0.1.77.100番】の4/100の確率です。Balloon賞、mini Drop賞 未公開の賞など複数の暗号通貨で構成されています。★リップル（XRP）もリスティングされています。\n 1回当たりの獲得枚数は、少額ですが回数重ねると大きいものです。\n BOT残高がなくなったら　おしまい...です。わかりましたか？適当な説明でした<:niko_shita:699072695823892561> 　:airplane::robot:')  

    if now == '11:11':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Please listen for a long time:robot:　HELLO! Airdrop method is dice:game_die:! The specified command will randomly output a number from 0 to 100. \n The number depends on the number. \n :airplane: The Airdrop award is the establishment of 4/100 of [0.1.77.100]:star2:. \n It is composed of multiple cryptocurrencies such as the Balloon Award and mini Drop Award. ★Ripple (XRP) is also listed.\n The number of coins you can get each time is small, but the number of times you get it is large. \n When the BOT balance is exhausted, it is the end ... Did you understand? It was a brief explanation.<:niko_shita:699072695823892561> 　:airplane::robot::')

    if now == '11:12':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: あっ！言い忘れていました！ｺﾏﾝﾄﾞは途中で変わったりします。動いている時間も不特定です。私を見つけたらｺﾏﾝﾄﾞで呼び出して下さいね☆回数制限はありませんが、連続するとボロだから..ロボでした(〃艸〃)ﾑﾌｯ止まります。ゆっくりと迷惑かからないようにお願いします。:star2:') 

    if now == '11:13':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:..:robot:..<:heart02:699580174911668225> 100回100通り出る内容が違います!<:good01:699581068285706301> 100 times 100 different contents!')
 
    if now == '11:14':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:ah!I forgot! The command may change on the way. The time of movement is unspecified. If you find me, please call me with a command ☆ There is no limit on the number of times, but it will stop if you continue. Please do not be a nuisance slowly. I"m a bot It will break.:star2:')  
  
    if now == '11:24':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:..:robot:..Please wait..:robot:\n/rain BGPT 7 ALL  :robot:') 
    
    if now == '12:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot:..:デハカイセツシマス/ Let me explain:robot:') 
                           
    if now == '12:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: ゲームは簡単でサイコロ:game_die:振るだけ！エアドロップCommandは【+】から始まります。半角英数小文字でさて何でしょう！？【+●●●】`+???` \n  :white_check_mark:ヒント①`+`は、元気がなくなってきた国を応援する気持ちのプラス。\n :white_check_mark:ヒント②2020年オリンピックが2021年延期しましたね。でも大丈夫かな？残念だけど仕方ない。\n:white_check_mark:ヒント③その国の通貨を意味します。+●●●ならそのスペルに関係します。以上。\n 周りに教えずにCommand打てば削除して下さいね。残高なくなれば終了する予定です。\n :robot:AirdropRobo専用チャンネルでコマンドは入れてください。\n　回数制限もうけてないから適度な回数でおねがいします。テキドナカイスウデ...:robot:') 
    
    if now == '12:27':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: The game is easy, just roll the dice:game_die:! Air Drop Command starts with [+]. What is it in half-width English letters!? 【+●●●】`+???` \n :white_check_mark: hint①:The `+` is a plus of the feeling of supporting a country that has become less energetic. \n :white_check_mark:hint②：The 2020 Olympics have been postponed to 2021. But is it okay? Unfortunately it can"t be helped.. \n:white_check_mark:hint③： \n It means the currency of the country. + ●●● is related to the spell. that"s all. \n Please delete it by typing Command without telling others. It will end when the balance is exhausted.\n Please enter the command on the :robot:AirdropRobo dedicated channel.\n Since there is no limit on the number of times, please give me an appropriate number of times...... :robot:')  

    if now == '12:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':robot: ◆ :game_die: :robot: ↓コマンドはこちらでお願いします↓For commands, please click here 　↓\n  #╰🤖airdrop-robo🆕..:robot:') 
    
   
        

   #ループ処理実行
loop.start()





@client.event
async def on_message(message):
    
    if message.content.startswith("+yen"):
     if client.user != message.author:
       num_random = random.randint(0, 100) #出る目を指定
       m = int(num_random)
       await message.channel.send(m)
     if 0 < m < 2: #1～1
          q = await message.channel.send(f"\n:point_right:rall～:game_die:  _(Dice→)_ :star2:No.:one: :star2: \n\n୨୧┈┈┈┈┈┈┈┈┈┈୨୧\n :airplane:\n:partying_face:tada: **Airdrop!**:confetti_ball: \n୨୧┈┈┈┈┈┈┈┈┈┈୨୧\n\n/tip BGPT 2345.6789 {message.author.mention}  <:BGPT02:698471366004965406> ")
          [await q.add_reaction(i) for i in ('<:heart02:699580174911668225>', '<:BGPT02:698471366004965406>')] # for文の内包表記

     elif 1 < m < 3: #2
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_:two: \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini drop:candy: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GDRH 22 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '🌈')] # for文の内包表記

     elif 2 < m < 4: #3
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :three: \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini drop:candy: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GDRH 33 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '🌈')] # for文の内包表記

     elif 3 < m < 5: #4
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :four: \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini drop:candy: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GDRH 44 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '🌈')] # for文の内包表記

     elif 4 < m < 6: #5
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_:five: \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini Go(5)drop:checkered_flag: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GOGO 55 {message.author.mention}   :checkered_flag:")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:good:699580636448423936>')] # for文の内包表記          
        
     elif 5 < m < 7: #6
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :six:  \n\n・。・。・。・。・。・。・。・。・。\n→mini drop:lollipop: \n・。・。・。・。・。・。・。・。・。\n\n/tip SEYU 6.6 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 6 < m < 8: #7
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ ☆:star2 :seven: :star2:☆ :airplane:\n:partying_face:tada: **Airdrop!mini!** \n\n୨୧┈┈┈┈┈┈┈┈┈୨୧\n\n/tip BGPT 777.7777 {message.author.mention}  <:BGPT02:698471366004965406> ")
          [await q.add_reaction(i) for i in ('<:heart02:699580174911668225>', '<:BGPT02:698471366004965406>')] # for文の内包表記
          
     elif 7 < m < 9: #8
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :eight: \n\n・。・。・。・。・。・。・。・。・。\n→mini drop:lollipop: \n・。・。・。・。・。・。・。・。・。\n\n/tip SEYU 8 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 8 < m < 10: #9
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :nine:   \n\n・。・。・。・。・。・。・。・。・。\n→mini drop:lollipop: \n・。・。・。・。・。・。・。・。・。\n\n/tip SEYU 9 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 9 < m < 11: #10
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :keycap_ten: \n\n・。・。・。・。・。・。・。・。・。\n→mini drop:lollipop: \n・。・。・。・。・。・。・。・。・。\n\n/tip SEYU 10 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 10 < m < 12: #11
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::one:   \n\n・。・。・。・。・。・。・。・。・。\n→mini drop:lollipop: \n・。・。・。・。・。・。・。・。・。\n\n/tip SEYU 11 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 11 < m < 13: #12
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::two:   \n\n・。・。・。・。・。・。・。・。・。\n→mini drop:lollipop: \n・。・。・。・。・。・。・。・。・。\n\n/tip SEYU 12 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 12 < m < 14: #13
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::three:   \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini drop:lollipop: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GDRH 13 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 13 < m < 15: #14
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::four:   \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini drop:candy: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GDRH 14 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 14 < m < 16: #15
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::five:   \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini drop:lollipop: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GDRH 15 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 15 < m < 17: #16
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::six:   \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini drop:lollipop: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GDRH 16 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 16 < m < 18: #17
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::seven:   \n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n→mini drop:lollipop: \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n/tip GDRH 17 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:kaokanga:699072678614663210>')] # for文の内包表記          

     elif 17 < m < 19: #18
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::eight:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:candy: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip EVEO 18 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:uzu1:700858878879072303>')] # for文の内包表記          

     elif 18 < m < 20: #19
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :one::nine:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:candy: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip EVEO 19 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:uzu1:700858878879072303>')] # for文の内包表記          

     elif 19 < m < 21: #20
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::zero:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:candy: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip EVERYLOTO 20 {message.author.mention} ")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:uzu1:700858878879072303>')] # for文の内包表記          

     elif 20 < m < 22: #21
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::one:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 21 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 21 < m < 23: #22
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::two:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 22 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 22 < m < 24: #23
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::three:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 23 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 23 < m < 25: #24
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::four:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 24 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 24 < m < 26: #25
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::five:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 25 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 25 < m < 27: #26
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::six:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 26 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 26 < m < 28: #27
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::seven:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 27 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 27 < m < 29: #28
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::eight:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy: \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 28 {message.author.mention}    :rainbow:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 28 < m < 30: #29
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :two::nine:   \n\n━－☆－━－━－━－━－━－━－☆－━\n→||**Are you a meat lover?**:cut_of_meat: ||\n━－☆－━－━－━－━－━－━－☆－━\n:rainbow:||☆:rainbow::cut_of_meat: **Congratulations** :meat_on_bone:☆\n\n/tip 29coin 292929.2929 {message.author.mention}     ||")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 29 < m < 31: #30
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :three::zero:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 30.29 {message.author.mention}   :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 30 < m < 32: #31
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :three::one:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 31.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 31 < m < 33: #32
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :three::two:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 32.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 32 < m < 34: #33
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :three::three:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 33.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 33 < m < 35: #34
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :three::four:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 34.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 34 < m < 36: #35
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :three::five:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 35.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 35 < m < 37: #36
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :three::six:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 36.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 36 < m < 38: #37
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :three::seven: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 37 < m < 39: #38
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :three::eight: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 38 < m < 40: #39
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :three::nine: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 39 < m < 41: #40
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :four::zero:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 40.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 40 < m < 42: #41
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :four::one:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 41.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 41 < m < 43: #42
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :four::two:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 42.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 42 < m < 44: #43
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :four::three:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 43.29 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 43 < m < 45: #44
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :four::four:   \n\n━－━－━－━－━－━－━－━－━－━\n→||**meat love♡**:cut_of_meat: || \n━－━－━－━－━－━－━－━－━－━\n\n/tip 29coin 4444.4444 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 44 < m < 46: #45
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :four::five:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy:  \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 456.456 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 45 < m < 47: #46
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :four::six:   \n\n━－━－━－━－━－━－━－━－━－━\n→mini drop:candy:  \n━－━－━－━－━－━－━－━－━－━\n\n/tip 456coin 46.456 {message.author.mention}    :meat_on_bone:")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 46 < m < 48: #47
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :four::seven: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 47 < m < 49: #48
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :four::eight: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 48 < m < 50: #49
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :four::nine: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 49 < m < 51: #50
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :five::zero: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 50 < m < 52: #51
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::one: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 5.1 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 51 < m < 53: #52
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::two: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 5.2 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 52 < m < 54: #53
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::three: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 5.3 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 53 < m < 55: #54
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::four: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 5.4 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 54 < m < 56: #55
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::five: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→☆mini GoGo!(55)drop:checkered_flag:☆ \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip GOGO 55.55 {message.author.mention}   :checkered_flag:")
          [await q.add_reaction(i) for i in ('<:good:699580636448423936>', '<:niko_shita:699072695823892561>')] # for文の内包表記

     elif 55 < m < 57: #56
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::six: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 5.6 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:niko_shita:699072695823892561>')] # for文の内包表記

     elif 56 < m < 58: #57
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::seven: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 5.7 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 57 < m < 59: #58
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::eight: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 5.8 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 58 < m < 60: #59
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :five::nine: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 5.9 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 59 < m < 61: #60
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :six::zero: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→☆mini drop:candy:☆ \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 60 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 60 < m < 62: #61
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :six::one: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 6.1 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 61 < m < 63: #62
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :six::two: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 6.2 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 62 < m < 64: #63
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :six::three: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 6.3 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 63 < m < 65: #64
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :six::four: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 6.4 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 64 < m < 66: #65
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :six::five: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Kick Dice!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 65 < m < 67: #66
          q = await message.channel.send(f"\n:game_die::dash::left_facing_fist:Punch!   _(Dice→)_ :boom: :six::six: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Punch Dice!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't Punch the Dice. ～None!\n ダイスをパンチしたらだめよw～!なし")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 66 < m < 68: #67
          q = await message.channel.send(f"\n:game_die::dash::left_facing_fist:Punch!   _(Dice→)_ :boom: :six::seven: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Punch Dice!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't Punch the Dice. ～None!\n ダイスをパンチしたらだめよw～!なし")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 67 < m < 69: #68
          q = await message.channel.send(f"\n:game_die::dash::left_facing_fist:Punch!   _(Dice→)_ :boom: :six::eight: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Punch Dice!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't Punch the Dice. ～None!\n ダイスをパンチしたらだめよw～!なし")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 68 < m < 70: #69
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :two_hearts: :six::nine: :two_hearts: \n\n∽∽♡∽∽∽∽∽∽∽∽∽♡∽∽\n→Love drop:heart: \n∽∽♡∽∽∽∽∽∽∽∽∽♡∽∽\n\n/tip BGPT 696.6969 {message.author.mention}  <:BGPTpink:705616860955148310>:heart:")
          [await q.add_reaction(i) for i in ('<:heart02:699580174911668225>', '<:kanngaeru:699072662382837881>')] # for文の内包表記   

     elif 69 < m < 71: #70
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :seven::zero: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 7 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 70 < m < 72: #71
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :seven::one: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 7.1 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 71 < m < 73: #72
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :seven::two: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 7.2 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 72 < m < 74: #73
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :seven::three: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 7.3 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 73 < m < 75: #74
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :seven::four: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 7.4 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 74 < m < 76: #75
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :seven::five:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:candy: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip EVEO 7.5 {message.author.mention}")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:uzu1:700858878879072303>')] # for文の内包表記          

     elif 75 < m < 77: #76
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :seven::six:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:candy: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip EVERYCOND 76 {message.author.mention}")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:uzu1:700858878879072303>')] # for文の内包表記          

     elif 76 < m < 78: #77
          q = await message.channel.send(f"\n:point_right:roll～:game_die:  _(Dice→)_ :seven::seven: \n\n୨୧┈┈┈┈┈┈┈┈┈┈୨୧\n :balloon:**Jackpot!**\n:partying_face::tada:**Airdrop**:balloon::rocket:\n୨୧┈┈┈┈┈┈┈┈┈┈୨୧\n\n/tip BGPT 3777.77 {message.author.mention}  <:BGPT02:698471366004965406>:confetti_ball: ")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPT02:698471366004965406>')] # for文の内包表記

     elif 77 < m < 79: #78
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :seven::eight:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:candy: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip EVEO 7.8 {message.author.mention}")
          [await q.add_reaction(i) for i in ('<:hai_kao:699072592987947117>', '<:uzu1:700858878879072303>')] # for文の内包表記          

     elif 78 < m < 80: #79
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :seven::nine:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:seedling: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip SPRTS 79 {message.author.mention}   :seedling:")
          [await q.add_reaction(i) for i in ('<:sprts:699076413931782146>', '<:sangras01:699579409220370514>')] # for文の内包表記          

     elif 79 < m < 81: #80
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :eight::zero:   \n\n‥★‥∴‥∵‥∴‥∴‥∵‥∴‥★‥\n→mini drop:seedling: \n‥★‥∴‥∵‥∴‥∴‥∵‥∴‥★‥\n\n/tip SPRTS 800 {message.author.mention}   :seedling:")
          [await q.add_reaction(i) for i in ('<:sprts:699076413931782146>', '<:sangras01:699579409220370514>')] # for文の内包表記          

     elif 80 < m < 82: #81
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :eight::one:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:seedling: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip SPRTS 81 {message.author.mention}   :seedling:")
          [await q.add_reaction(i) for i in ('<:sprts:699076413931782146>', '<:sangras01:699579409220370514>')] # for文の内包表記          

     elif 81 < m < 83: #82
          q = await message.channel.send(f"\n:point_right:roll～:game_die:   _(Dice→)_ :eight::two:   \n\n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n→mini drop:seedling: \n‥∵‥∴‥∵‥∴‥∴‥∵‥∴‥∵‥\n\n/tip SPRTS 82 {message.author.mention}   :seedling:")
          [await q.add_reaction(i) for i in ('<:sprts:699076413931782146>', '<:sangras01:699579409220370514>')] # for文の内包表記          

     elif 82 < m < 84: #83
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :eight::three: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 83 < m < 85: #84
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :eight::four: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 84 < m < 86: #85
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :eight::five: \n\n━－━－━－━－━－━－━－━－━－━\n→★mini drop:candy:★ \n━－━－━－━－━－━－━－━－━－━\n\n/tip KENJ 850 {message.author.mention}   <:kenj:700136543003607101> ")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:kenj:700136543003607101>')] # for文の内包表記        

     elif 85 < m < 87: #86
          q = await message.channel.send(f"\n:game_die::dash::leg:kick!   _(Dice→)_ :boom: :eight::six: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Dice Kick!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't kick the dice with your foot～ None\n ダイスを足で蹴ったらだめよ～!None")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記          

     elif 86 < m < 88: #87
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :eight::seven: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→☆mini drop:candy:☆ \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 87 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 87 < m < 89: #88
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :eight::eight: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→:balloon: Balloon drop :balloon: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 880 {message.author.mention}  <:BGPTpink:705616860955148310>:balloon:")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 88 < m < 90: #89
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :eight::seven: \n\n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n→ mini drop:candy: \n∽∽∽∽∽∽∽∽∽∽∽∽∽∽\n\n/tip BGPT 8.9 {message.author.mention}  <:BGPTpink:705616860955148310>")
          [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPTpink:705616860955148310>')] # for文の内包表記

     elif 89 < m < 91: #90
          q = await message.channel.send(f"\n:game_die::dash::left_facing_fist:Punch!   _(Dice→)_ :boom: :nine::zero: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Punch Dice!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't Punch the Dice. ～None!\n ダイスをパンチしたらだめよw～!なし")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 90 < m < 92: #91
          q = await message.channel.send(f"\n:game_die::dash::left_facing_fist:Punch!   _(Dice→)_ :boom: :nine::one: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Punch Dice!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't Punch the Dice. ～None!\n ダイスをパンチしたらだめよw～!なし")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 91 < m < 93: #92
          q = await message.channel.send(f"\n:game_die::dash::left_facing_fist:Punch!   _(Dice→)_ :boom: :nine::two: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Punch Dice!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't Punch the Dice. ～None!\n ダイスをパンチしたらだめよw～!なし")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 92 < m < 94: #93
          q = await message.channel.send(f"\n:game_die::dash::left_facing_fist:Punch!   _(Dice→)_ :boom: :nine::three: :boom:   \n\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n **Punch Dice!** :dash: \n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n<:namida1:699577954094809088>Don't Punch the Dice. ～None!\n ダイスをパンチしたらだめよw～!なし")
          [await q.add_reaction(i) for i in ('<:niko_shita:699072695823892561>', '<:uzu2:700858786960900117>')] # for文の内包表記   

     elif 93 < m < 95: #94
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :nine::four: \n\n━－━－━－━－━－━－━－━－━－━\n→★mini drop:candy:★ \n━－━－━－━－━－━－━－━－━－━\n\n/tip KENJ 940 {message.author.mention}   <:kenj:700136543003607101> ")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:kenj:700136543003607101>')] # for文の内包表記

     elif 94 < m < 96: #95
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :nine::five: \n\n━－━－━－━－━－━－━－━－━－━\n→★mini drop:candy:★ \n━－━－━－━－━－━－━－━－━－━\n\n/tip KENJ 950 {message.author.mention}   <:kenj:700136543003607101> ")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:kenj:700136543003607101>')] # for文の内包表記

     elif 95 < m < 97: #96
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :nine::six: \n\n━－━－━－━－━－━－━－━－━－━\n→★mini drop:candy:★ \n━－━－━－━－━－━－━－━－━－━\n\n/tip KENJ 960 {message.author.mention}   <:kenj:700136543003607101> ")
          [await q.add_reaction(i) for i in ('<:kanngaeru:699072662382837881>', '<:kenj:700136543003607101>')] # for文の内包表記

     elif 96 < m < 98: #97
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :nine::seven: \n\n‥☆∵‥∴‥∵‥∴<:BENKEICOIN04:698471407650209832>∴‥∵‥∴‥∵☆‥\n→mini drop:candy: \n‥☆∵‥∴‥∵‥∴<:BENKEICOIN04:698471407650209832>∴‥∵‥∴‥∵☆‥\n\n/tip BEN 9.7 {message.author.mention}   <:benkeicoinsl:698471387064696833> ")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:benkeicoinsl:698471387064696833>')] # for文の内包表記

     elif 97 < m < 99: #98
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :nine::eight: \n\n‥☆∵‥∴‥∵‥∴<:BENKEICOIN04:698471407650209832>∴‥∵‥∴‥∵☆‥\n→mini drop:candy: \n‥☆∵‥∴‥∵‥∴<:BENKEICOIN04:698471407650209832>∴‥∵‥∴‥∵☆‥\n\n/tip BEN 9.8 {message.author.mention}   <:benkeicoinsl:698471387064696833> ")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:benkeicoinsl:698471387064696833>')] # for文の内包表記

     elif 98 < m < 100: #99
          q = await message.channel.send(f"\n:pinching_hand:roll～:game_die:  _(Dice→)_ :nine::nine: \n\n‥☆∵‥∴‥∵‥∴<:BENKEICOIN04:698471407650209832>∴‥∵‥∴‥∵☆‥\n→:balloon: Balloon drop:candy: :balloon: \n‥☆∵‥∴‥∵‥∴<:BENKEICOIN04:698471407650209832>∴‥∵‥∴‥∵☆‥\n\n/tip BEN 99.9 {message.author.mention}   <:benkeicoinsl:698471387064696833>:balloon: ")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:benkeicoinsl:698471387064696833>')] # for文の内包表記
            
     else: #それ以外なので今回の場合100が出た時に処理される
          q = await message.channel.send(f"\n:point_right:roll～:game_die:  _(Dice :zero: or :one::zero::zero:)_ \n\n୨୧┈┈┈┈┈┈┈┈┈┈୨୧\n:partying_face::tada: **Airdrop!** :rocket::confetti_ball: \n୨୧┈┈┈┈┈┈┈┈┈┈୨୧\n\n/tip BGPT 2345.6789 {message.author.mention}  <:BGPT02:698471366004965406>:confetti_ball: ")
          [await q.add_reaction(i) for i in ('<:good01:699581068285706301>', '<:BGPT02:698471366004965406>')] # for文の内包表記




# Botの起動とDiscordサーバーへの接続
client.run(token)

