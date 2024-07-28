from telebot import TeleBot,types
from kvsqlite.sync import Client
from requests import get
from os import path
from time import sleep,time
from random import choice
from phonenumbers import parse,geocoder



#متكدر تخمط 😁 .


alEx,dalEx=TeleBot("5200444372:AAHfWOOy8Lm2Mz2A6bie4qy3aG7VxsZ1s90"),Client("xXx.alEx")
dalEx.delete('Channel')
Ad = 2067261869
if path.exists("Whit.txt") == False or path.exists("Black.txt") == False:
	with open("Black.txt","a") as g:
		pass
	with open("Whit.txt","a") as g:
		pass


if dalEx.exists("All-Invitation") == False:
	data = {"users":[]}
	dalEx.set("All-Invitation",data)
	
apikey= "api_key"
@alEx.message_handler(content_types=['contact'])
def handle_contact(message):
		
		if dalEx.exists('Channel') == True:
		 	Channel = dalEx.get('Channel')
		else:
		 	Channel = "@TeamRecode"
		if alEx.get_chat_member(Channel,message.chat.id).status == "administrator" or alEx.get_chat_member(Channel,message.chat.id).status == "creator" or alEx.get_chat_member(Channel,message.chat.id).status == "member":
				contact = "+"+str(message.contact.phone_number)			
				parsed_number = parse(contact)
				country = geocoder.description_for_number(parsed_number, "en")
				
				if country == "Iraq" or country == "Egypt" :
					with open("Whit.txt","a") as w:
						w.write(str(message.chat.id)+"\n")
						alEx.reply_to(message,"💎 تم تأكيد حسابك بنجاح ✔️ .\n💎 يمكنك استخدام البوت بحريه الآن .\n⚠️ أضغط /start لأستخدام البوت .")
				else:
					with open("Black.txt","a") as w:
						w.write(str(message.chat.id)+"\n")
					alEx.reply_to(message,'''
📍حسابك غير مؤهل لاستخدام البوت ، انتضر التحديثات القادمة ❕
📍ادخل من حساب عراقي او مصري ❕
''')
		else:
				ChanNel = types.InlineKeyboardMarkup()
				ChanNel.add(types.InlineKeyboardButton('( TeAm ReCode )',url=str(Channel).split('@')[1]+'.t.me'))
				alEx.reply_to(message,f'''
				↯︙عذراً عزيزي عليك الاشتراك في القنوات .
- ↯ /start بعد الاشتراك ارسل 
''',reply_markup=ChanNel)			

@alEx.message_handler(commands=['start'])
def StartBot(message):
	 
	 if str(message.chat.id) in open("Black.txt","r").read().splitlines() and message.chat.id != Ad:
	 	alEx.reply_to(message,'''
📍حسابك غير مؤهل لاستخدام البوت ، انتضر التحديثات القادمة ❕
📍ادخل من حساب عراقي او مصري ❕
''')
	 elif str(message.chat.id) not in open("Black.txt","r").read().splitlines() and str(message.chat.id) not in open("Whit.txt","r").read().splitlines() :
		 markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		 contact_button = types.KeyboardButton("( مشاركة جهة الاتصال )", request_contact=True)
		 markup.add(contact_button)
		 alEx.send_message(message.chat.id,"شارك جهة اتصالك اولا ." ,reply_markup=markup)
	 
	 elif str(message.chat.id) not in open("Black.txt","r").read().splitlines() and str(message.chat.id) in open("Whit.txt","r").read().splitlines() :
		 if dalEx.exists('Channel') == True:
		 	Channel = dalEx.get('Channel')
		 else:
		 	Channel = "@TeamRecode"
		 if dalEx.exists("RunBot") == False and message.chat.id != Ad:
		 	alEx.reply_to(message,'⚙️ عذراً عزيزي البوت تحت الصيانه !')
		 else:
		 	
		 	if dalEx.exists(f"allBuy-{message.chat.id}") == False:
		 			dalEx.set(f"allBuy-{message.chat.id}",0)
		 	
		 	if alEx.get_chat_member(Channel,message.chat.id).status == "administrator" or alEx.get_chat_member(Channel,message.chat.id).status == "creator" or alEx.get_chat_member(Channel,message.chat.id).status == "member":	 	
		 		
			 		if message.chat.id == Ad:
			 			if dalEx.exists("RunBot") == True:
			 				T = "( عمل البوت ✅ )"
			 			else:
			 				T = "( عمل البوت ❌ )"
			 			GoaT = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(T,callback_data="RunBot"))
			 			GoaT.add(types.InlineKeyboardButton('( اضف نقاط )',callback_data='addPoint'),types.InlineKeyboardButton('( الاجباري )',callback_data='GetUserChannel'))
			 			GoaT.add(types.InlineKeyboardButton("( تعديل الاسعار )",callback_data="EditPrice"))
			 			alEx.send_message(Ad,'''
				~ اهلا بك عزيزي .
				• يمكنك زيادة نقاط المشتركين من خلال الازرار :
– – – – – – –
				''',reply_markup=GoaT)
			 		if dalEx.exists(f"{message.chat.id}") == False and message.chat.id != Ad:
			 				with open("Sub.txt",'a') as w:
			 					w.write(f'{message.chat.id}'+'\n')			 				
			 				alEx.send_message(Ad,f'''
– – – – – – – – – – – – – –
				~> تم دخول شخص جديد الى البوت :
				↯︙الاسم : {message.chat.first_name} •
				↯︙معرف العضو : @{message.from_user.username} •
– – – – – – – – – – – – – –
''')
			 				if dalEx.exists(f'{message.chat.id}') == True:
			 					pass
			 				else:
			 					dalEx.set(f'{message.chat.id}',0)
			 		
			 		if " " in message.text:
			 			Id_User = str(message.text).split('/start ')[1]
			 			
			 			if path.exists(f"Invitation-{Id_User}.txt") == False:
			 				with open(f"Invitation-{Id_User}.txt","a") as e:
			 					pass
			 			if str(message.chat.id) in open(f"Invitation-{Id_User}.txt","r").read().splitlines() or message.chat.id == int(Id_User) or str(message.chat.id) in dalEx.get("All-Invitation")["users"]:
			 					Y = None
			 			else:
			 					data = dalEx.get("All-Invitation")
			 					data["users"].append(message.chat.id)
			 					dalEx.set("All-Invitation",data)
			 					
			 					with open(f"Invitation-{Id_User}.txt","a") as a:
			 						a.write(str(message.chat.id)+"\n")
			 						
			 					
			 					Y = '''
		 ↯︙تم دخول شخص جديد الى البوت عبر رابط الدعوه الخاص بك وحصلت على ( 1 ) نقاط في البوت •''';MyPoint= int(dalEx.get(f"{Id_User}"));dalEx.set(f"{Id_User}",int(MyPoint)+1)
		 
		 
			 		try:
				 		if Y == None:
				 			pass
				 		else:
				 			alEx.send_message(message.chat.id,' ↯︙لقد دخلت الى رابط الدعوه الخاص بصديقك وحصل على ( 1 ) نقاط 🤩 .')
				 			alEx.send_message(Id_User,Y) 
				 	except:
				 		pass
				 	
				 	
				 	Name = str(message.chat.first_name)
			 		Dev=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( معلومات حسابك )',callback_data='InfoAcc'))
			 		Dev.add(types.InlineKeyboardButton('( شراء رقم )',callback_data='GetNum'),types.InlineKeyboardButton('( شراء نقاط )',callback_data='point'))
			 		Dev.add(types.InlineKeyboardButton("( تجميع نقاط )",callback_data="GetPoints"))
			 		Dev.add(types.InlineKeyboardButton("[ تعليمات البوت ]",callback_data="Instructions"))
			 		Dev.add(types.InlineKeyboardButton('( قناة السورس )',url='sadem_store19.t.me'))
			 		alEx.reply_to(message,f'''
		[ × ] اهلا ( {Name} )
		– – – – – – –
		— البوت مخصص لبيع ارقام لعدة منصات 🧬 .
		— يمكنك إيجاد المنصات من الازرار الموجوده في الاسفل ↯ :
		– – – – – – –
		''',reply_markup=Dev)
		 	
		 	else:
		 		ChanNel = types.InlineKeyboardMarkup()
		 		ChanNel.add(types.InlineKeyboardButton('( TeAm ReCode )',url=str(Channel).split('@')[1]+'.t.me'))
		 		alEx.reply_to(message,f'''
				↯︙عذراً عزيزي عليك الاشتراك في القنوات .
- ↯ /start بعد الاشتراك ارسل 

''',reply_markup=ChanNel)

x = 0
def EditPrice(message,Reg):
	global x
	x+=1
	if x > 1:
		pass
	else:
		if str(message.text).isdigit():
			dalEx.set(f"Reg-{Reg}",message.text)
			alEx.reply_to(message,f'''
	[√ ] تم حفظ سعر الدوله ( {message.text} ) ❕
	''');x=0
		elif isinstance(message.text,int) == False or "/start" in str(message.text) or "start" in str(message.text):
			pass
a=0
def AddPoint(message):
		global a
		if ':' in str(message.text):
			a+=1
			Name = str(message.chat.first_name)
			point, Id_User = str(message.text).split(':')[1],str(message.text).split(':')[0]
			if a > 1:
				pass
			else:
				try:
					alEx.send_message(int(Id_User),f'''
		↯︙تم تحديث رصيدك اصبح {point} نقطة ❕''');
					dalEx.set(f'{Id_User}',point)
					Backa=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
					alEx.reply_to(message,f'''↯︙تم اضافة {point} •
	↯︙المستخدم ~> {Id_User} •
	''',reply_markup=Backa);a=0
					
				except Exception as e:
					if 'chat not found' in str(e):
						Backa=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
						alEx.reply_to(message,'↯︙هذا المستخدم لم يدخل للبوت !',reply_markup=Backa)
					else:print(e)

def GetChannel(message):
	if "/start" in str(message.text) or "start" in str(message.text) or "@" not in str(message.text):
		pass
	elif "@" in str(message.text):
		dalEx.set('Channel',f'{message.text}')
		alEx.reply_to(message,'↯ تم اضافة قناة الاشتراك الاجباري •\n↯ تذكر بأنك قمت برفع البوت مشرف في قناتك !')
last_pressed_time = {}
@alEx.callback_query_handler(func=lambda call : True)
def CallIng(call):
	current_time = time()
	user_id = call.from_user.id
	if user_id == Ad or user_id not in last_pressed_time or current_time - last_pressed_time[user_id] >= 3:
		
		last_pressed_time[user_id] = current_time
		
		RU = dalEx.get("Reg-RU");UK = dalEx.get("Reg-UK");BKS = dalEx.get("Reg-BKS");HOL = dalEx.get("Reg-HOL");MAX = dalEx.get("Reg-MAX");LET = dalEx.get("Reg-LET");LTV = dalEx.get("Reg-LTV");ISR = dalEx.get("Reg-ISR");END = dalEx.get("Reg-END");CH = dalEx.get("Reg-CH");GOR = dalEx.get("Reg-GOR");FR = dalEx.get("Reg-FR");AST = dalEx.get("Reg-AST");CZ = dalEx.get("Reg-CZ");BUL = dalEx.get("Reg-BUL");AZ = dalEx.get("Reg-AZ");ARG = dalEx.get("Reg-ARG");ANG = dalEx.get("Reg-ANG");US = dalEx.get("Reg-US");GRS = dalEx.get("Reg-GRS")
		
		
		if call.data == 'GetUserChannel':
			alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
	⚙️ ارسل يوزر قناة الاشتراك الاجباري مع @ ↯ :
	'''),GetChannel)
		if call.data=="RunBot":
			dalEx.delete("RunBot")
			GoaT = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("( عمل البوت ❌ )",callback_data="RunOffBot"))
			GoaT.add(types.InlineKeyboardButton('( اضف نقاط )',callback_data='addPoint'),types.InlineKeyboardButton('( الاجباري )',callback_data='GetUserChannel'))
			alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		~ اهلا بك عزيزي .
		• يمكنك زيادة نقاط المشتركين من خلال الازرار :
		________
		''',reply_markup=GoaT)
		elif call.data=="RunOffBot":
			dalEx.set("RunBot",'')
			GoaT = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("( عمل البوت ✅ )",callback_data="RunBot"))
			GoaT.add(types.InlineKeyboardButton('( اضف نقاط )',callback_data='addPoint'),types.InlineKeyboardButton('( الاجباري )',callback_data='GetUserChannel'))
			alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		~ اهلا بك عزيزي .
		• يمكنك زيادة نقاط المشتركين من خلال الازرار :
		________
		''',reply_markup=GoaT)
		elif dalEx.exists("RunBot") == False and call.message.chat.id != Ad:
			Dev=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("( قناة السورس )",url="sadem_store19.t.me"))
			alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
	⚙️ عذراً عزيزي البوت تحت الصيانه !''',reply_markup=Dev)
		if dalEx.exists("RunBot") == True or call.message.chat.id==Ad:		
			if call.data == "InfoAcc":
				MyPoint= dalEx.get(f"{call.message.chat.id}")
				if dalEx.exists(f"allBuy-{call.message.chat.id}")== True:
					Buy = int(dalEx.get(f"allBuy-{call.message.chat.id}"))
				else:
					Buy=0
				if path.exists(f"Invitation-{call.message.chat.id}.txt") == False:
					Invit = 0
				if path.exists(f"Invitation-{call.message.chat.id}.txt") == True:
					G =0
					for Inv in dalEx.get("All-Invitation")["users"]:
						G+=1
					Invit = G
				Back=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("( رجوع )",callback_data="Back"))
				Bot = call.message.from_user.username
				user_id = call.message.chat.id
				Link_ = f"https://t.me/{Bot}?start={user_id}"
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
– معلومات حسابك :

↯ ايديك ~> {call.message.chat.id} •
— — — — — — — 
↯ نقاطك ~>  {MyPoint} •
↯ مرات الشرء ~> {Buy} •

— — — — — — — 

↯ عدد مشاركتك للرابط ~> {Invit} •
↯ رابط الدعوه الخاص بك ~> {Link_} •
''',reply_markup=Back,disable_web_page_preview=True)
		
		
			elif call.data == 'EditPrice':
				keyboard = types.InlineKeyboardMarkup(row_width=2)
				buttons = [types.InlineKeyboardButton(alex, callback_data=f"{alex}") for alex in ["امريكا","انغولا","الارجنتين","اذربيجان","بلغاريا","التشيك","أستونيا","فرنسا","جورجيا","هونغ كونغ","إندونيسيا","إسرائيل","لاتفيا","ليتوانيا","المكسيك","هولندا","باكستان","بريطانيا","روسيا","اليونان"]]
				pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
				for pair in pairs:
					keyboard.row(*pair)
				keyboard.add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
[ ♠ ] قسم تعديل الاسعار للدول ❕
– – – – –
— أختر الدوله المراد تعديل سعرها :
– – – – –
		''',reply_markup=keyboard)
		
			elif call.data == 'اليونان':
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="GRS")		
		
			elif call.data == 'امريكا':
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="US")

			elif call.data == "Instructions":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''

– بعد قرائتك لهذه الشروط والنصائح لا نتحمل مسؤلية عدم عمل البوت معك بشكل صحيح ❗


🔹 كيفية سحب الارقام من البوت ❕

( 1 ) الارقام التي يتم شرائها من البوت دائميه ولا تُحذف ابداُ ... الا اذا قُمت ( بتفعيل التحقق بخطوتين وتأكيده بأيميل ) الأيميل ضروري يجب تفعيله ❗

( 2 ) عند شرائك رقم من البوت اطلب الكود من نسخة تليكرام الاصليه ويجب ان يضهر لك تم إرسال رسالة ( sms ) ، وعند طلبك للكود ارجع الى البوت واضغط زر ( تحديث صندوق الوارده ) اكثر من مره واذا لم يصلك الكود خلال 3 دقائق احذف الرقم وسيتم استرجاع نقاطك 🧬 .


( 3 ) عندما تطلب الكود من النسخه الاصليه ( تم ارسال رسالة sms ) ، وقد حصلت على الكود ولكن من الممكن او 50% يكون الحساب يحتوى على تحقق بخطوتين ، كيف يمكن تخطي هذه المشكله ؟ وسحب الرقم ؟
1 - اطلب حذف الرقم بعدها ستضهر لك واجهة ضع اسمك بعدها سيقول لك حصل خطأ .

2 - اطلب الكود بعد حذفك للحساب وارجع الى البوت واضغط على زر ( الكود ) الذي ضهر عند رسالة الكود في المره الاولى لكي تتمكن من الحصول على الكود مره اخرى .


( 4 ) عندما تطلب كود لرقم مُعين ويقول ( تم ارسال رسالة sms الى الرقم ) ولم تحصل على الكود فهذه المشكله ليست في البوت بل من التليكرام نفسه لان التليكرام لا عطي كود لدول معينه مثل ( هونغ كونغ ) وغيرها الا اذا قمت بتفعيل vpn ونسبة جداً قليله يقوم بأعطائك الكود ❕

''',reply_markup=Back)

			elif call.data == 'انغولا':
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="ANG")

			elif call.data == "الارجنتين":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="ARG")

			elif call.data == "اذربيجان":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="AZ")

			elif call.data == "بلغاريا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="BUL")

			elif call.data == "التشيك":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="CZ")

			elif call.data == "أستونيا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="AST")

			elif call.data == "فرنسا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="FR")

			elif call.data == "جورجيا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="GOR")

			elif call.data == "هونغ كونغ":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="CH")


			elif call.data == "إندونيسيا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="END")

			elif call.data == "إسرائيل":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="ISR")

			elif call.data == "لاتفيا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="LTV")

			elif call.data == "ليتوانيا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="LET")


			elif call.data == "المكسيك":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="MAX")


			elif call.data == "هولندا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="HOL")

			elif call.data == "باكستان":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="BKS")

			elif call.data == "بريطانيا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="UK")

			elif call.data == "روسيا":
				Back = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
– أرسل السعر الأن ...''',reply_markup=Back),EditPrice,Reg="RU")

			elif call.data == 'GetPoints':
				Bot = call.message.from_user.username
				user_id = call.message.chat.id
				Link_ = f"https://t.me/{Bot}?start={user_id}"
				Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("↑ مشاركة الرابط ↑",url=f'''https://t.me/share/url?url=بوت يمكنك من خلاله الحصول على ارقام لعدة منصات ومنها تليجرام .\nسارع بالحصول على رقم مجاني:{Link_}'''))
				Dev.add(types.InlineKeyboardButton("( رجوع )",callback_data="Back"))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
 ↯︙قسم تجميع النقاط :

• يمكنك من خلال هذا القسم زيادة نقاطك في البوت بشكل قانوني ❕
• فقط قُم بمشاركة رابط الدعوه الخاص بك لأصدقائك .
•	ستحصل عند دخول اي احد الى البوت من خلال رابط الدعوه على ( 1 ) نقاط في البوت .

× ماذا تنتضر ؟ قُم بمشاركة رابط الدعوه الخاص بك الان :

رابط الدعوه : {Link_}

× ملاحظة : أضغط على الرابط في مره اخرى في حالة لم يتم احتساب النقاط .
''',reply_markup=Dev,disable_web_page_preview=True)
		
			elif call.data == "Back":
				Name = str(call.message.chat.first_name)
				Dev=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( معلومات حسابك )',callback_data='InfoAcc'))
				Dev.add(types.InlineKeyboardButton('( شراء رقم )',callback_data='GetNum'),types.InlineKeyboardButton('( شراء نقاط )',callback_data='point'))
				Dev.add(types.InlineKeyboardButton("( تجميع نقاط )",callback_data="GetPoints"))
				Dev.add(types.InlineKeyboardButton("[ تعليمات البوت ]",callback_data="Instructions"))
				Dev.add(types.InlineKeyboardButton('( قناة السورس )',url='sadem_store19.t.me'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
[ × ] اهلا ( {Name} )
– – – – – – –
— البوت مخصص لبيع ارقام لعدة منصات 🧬 .
— يمكنك إيجاد المنصات من الازرار الموجوده في الاسفل ↯ :
– – – – – – –
''',reply_markup=Dev)
		
			
			elif call.data == "point":
				Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( شراء نقاط )',url='M_L_F.t.me'))
				Dev.add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
	~ اسعار نقاط بوت الارقام كالآتي :
	 ↯︙35 P ~> 5$ 
	 ↯︙45 P ~> 10$
	 ↯︙55 P ~> 15$
	 ↯︙70 P ~> 20$
	 ↯︙The Points To Million ...
		''',reply_markup=Dev)
			elif call.data == 'addPoint':
				Backa=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( الغاء ورجوع )',callback_data='Backa'))
				alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙ارسل عدد النقاط وايدي المستخدم :
		↯ مثال ~> Ad:10
		↯ حيث الـ Ad هوه ايدي المستخدم .
		↯ والـ 10 هوه عدد النقاط المراد اضافتها للمستخدم .
		''',reply_markup=Backa),AddPoint)
			elif call.data == 'Backa':
				if dalEx.exists("RunBot") == True:
		 				T = "( عمل البوت ✅ )"
				else:
		 				T = "( عمل البوت ❌ )"
				GoaT = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(T,callback_data="RunBot"))
				GoaT.add(types.InlineKeyboardButton('( اضف نقاط )',callback_data='addPoint'),types.InlineKeyboardButton('( الاجباري )',callback_data='GetUserChannel'))
				GoaT.add(types.InlineKeyboardButton("( تعديل الاسعار )",callback_data="EditPrice"))
		 			
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
			~ اهلا بك عزيزي .
			• يمكنك زيادة نقاط المشتركين من خلال الازرار :
			________
			''',reply_markup=GoaT)
			elif call.data == 'GetNum':
				
				
				tg = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( تليجرام )',callback_data="TG"))
				tg.add(types.InlineKeyboardButton("( انستجرام )",callback_data='IG'),types.InlineKeyboardButton("( واتساب )",callback_data='WA'))
				tg.add(types.InlineKeyboardButton('( نيتفلكس )',callback_data='NF'),types.InlineKeyboardButton("( جوجل )",callback_data='Go'))
				tg.add(types.InlineKeyboardButton("( فيسبوك )",callback_data='FB'),types.InlineKeyboardButton('( بايبال )',callback_data='PP'))
				
				tg.add(types.InlineKeyboardButton("( رجوع )",callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""↯︙اختر المنصة المراد شراء رقم لها ↯ :
	________
	""",reply_markup=tg)
	
	
			elif call.data == "IG":
				dalEx.set(f"alEx-{call.message.chat.id}","ig")
				
				keyboard = types.InlineKeyboardMarkup(row_width=2)
				buttons = [types.InlineKeyboardButton(alex, callback_data=f"{alex}") for alex in [f'🇬🇷 اليونان ( {GRS} )',f"🇺🇸 امريكا ( {US} )",f"🇦🇴 انغولا ( {ANG} )",f"🇦🇷 الارجنتين ( {ARG} )",f"🇦🇿 اذربيجان ( {AZ} )",f"🇧🇬 بلغاريا ( {BUL} )",f"🇨🇿 التشيك ( {CZ} )",f"🇪🇪 أستونيا ( {AST} )",f"🇫🇷 فرنسا ( {FR} )",f"🇬🇪 جورجيا ( {GOR} )",f"🇭🇰 هونغ كونغ ( {CH} )",f"🇮🇩 إندونيسيا ( {END} )",f"🇮🇱  إسرائيل ( {ISR} )",f"🇱🇻 لاتفيا ( {LTV} )",f"🇱🇹 ليتوانيا ( {LET} )",f"🇲🇽 المكسيك ( {MAX} )",f"🇳🇱 هولندا ( {HOL} )",f"🇵🇰 باكستان ( {BKS} )",f"🇬🇧 بريطانيا  ( {UK} )",f"🇷🇺 روسيا ( {RU} )"]]
				pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
				for pair in pairs:
					keyboard.row(*pair)
				keyboard.add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙اختر الدوله المراد شراء رقم منها ↯ :
	________
		''',reply_markup=keyboard)
				
			elif call.data == "WA":
				dalEx.set(f"alEx-{call.message.chat.id}","wa")
				keyboard = types.InlineKeyboardMarkup(row_width=2)
				buttons = [types.InlineKeyboardButton(alex, callback_data=f"{alex}") for alex in [f'🇬🇷 اليونان ( {GRS} )',f"🇺🇸 امريكا ( {US} )",f"🇦🇴 انغولا ( {ANG} )",f"🇦🇷 الارجنتين ( {ARG} )",f"🇦🇿 اذربيجان ( {AZ} )",f"🇧🇬 بلغاريا ( {BUL} )",f"🇨🇿 التشيك ( {CZ} )",f"🇪🇪 أستونيا ( {AST} )",f"🇫🇷 فرنسا ( {FR} )",f"🇬🇪 جورجيا ( {GOR} )",f"🇭🇰 هونغ كونغ ( {CH} )",f"🇮🇩 إندونيسيا ( {END} )",f"🇮🇱  إسرائيل ( {ISR} )",f"🇱🇻 لاتفيا ( {LTV} )",f"🇱🇹 ليتوانيا ( {LET} )",f"🇲🇽 المكسيك ( {MAX} )",f"🇳🇱 هولندا ( {HOL} )",f"🇵🇰 باكستان ( {BKS} )",f"🇬🇧 بريطانيا  ( {UK} )",f"🇷🇺 روسيا ( {RU} )"]]
				pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
				for pair in pairs:
					keyboard.row(*pair)
				keyboard.add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙اختر الدوله المراد شراء رقم منها ↯ :
	________
		''',reply_markup=keyboard)
		
			elif call.data == "NF":
				dalEx.set(f"alEx-{call.message.chat.id}","nf")
				keyboard = types.InlineKeyboardMarkup(row_width=2)
				buttons = [types.InlineKeyboardButton(alex, callback_data=f"{alex}") for alex in [f'🇬🇷 اليونان ( {GRS} )',f"🇺🇸 امريكا ( {US} )",f"🇦🇴 انغولا ( {ANG} )",f"🇦🇷 الارجنتين ( {ARG} )",f"🇦🇿 اذربيجان ( {AZ} )",f"🇧🇬 بلغاريا ( {BUL} )",f"🇨🇿 التشيك ( {CZ} )",f"🇪🇪 أستونيا ( {AST} )",f"🇫🇷 فرنسا ( {FR} )",f"🇬🇪 جورجيا ( {GOR} )",f"🇭🇰 هونغ كونغ ( {CH} )",f"🇮🇩 إندونيسيا ( {END} )",f"🇮🇱  إسرائيل ( {ISR} )",f"🇱🇻 لاتفيا ( {LTV} )",f"🇱🇹 ليتوانيا ( {LET} )",f"🇲🇽 المكسيك ( {MAX} )",f"🇳🇱 هولندا ( {HOL} )",f"🇵🇰 باكستان ( {BKS} )",f"🇬🇧 بريطانيا  ( {UK} )",f"🇷🇺 روسيا ( {RU} )"]]
				pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
				for pair in pairs:
					keyboard.row(*pair)
				keyboard.add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙اختر الدوله المراد شراء رقم منها ↯ :
	________
		''',reply_markup=keyboard)	
	
	
			elif call.data == "FB":
				dalEx.set(f"alEx-{call.message.chat.id}","fb")
				keyboard = types.InlineKeyboardMarkup(row_width=2)
				buttons = [types.InlineKeyboardButton(alex, callback_data=f"{alex}") for alex in [f'🇬🇷 اليونان ( {GRS} )',f"🇺🇸 امريكا ( {US} )",f"🇦🇴 انغولا ( {ANG} )",f"🇦🇷 الارجنتين ( {ARG} )",f"🇦🇿 اذربيجان ( {AZ} )",f"🇧🇬 بلغاريا ( {BUL} )",f"🇨🇿 التشيك ( {CZ} )",f"🇪🇪 أستونيا ( {AST} )",f"🇫🇷 فرنسا ( {FR} )",f"🇬🇪 جورجيا ( {GOR} )",f"🇭🇰 هونغ كونغ ( {CH} )",f"🇮🇩 إندونيسيا ( {END} )",f"🇮🇱  إسرائيل ( {ISR} )",f"🇱🇻 لاتفيا ( {LTV} )",f"🇱🇹 ليتوانيا ( {LET} )",f"🇲🇽 المكسيك ( {MAX} )",f"🇳🇱 هولندا ( {HOL} )",f"🇵🇰 باكستان ( {BKS} )",f"🇬🇧 بريطانيا  ( {UK} )",f"🇷🇺 روسيا ( {RU} )"]]
				pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
				for pair in pairs:
					keyboard.row(*pair)
				keyboard.add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙اختر الدوله المراد شراء رقم منها ↯ :
	________
		''',reply_markup=keyboard)
	
			elif call.data == "PP":
				dalEx.set(f"alEx-{call.message.chat.id}","pp")
				
				keyboard = types.InlineKeyboardMarkup(row_width=2)
				buttons = [types.InlineKeyboardButton(alex, callback_data=f"{alex}") for alex in [f'🇬🇷 اليونان ( {GRS} )',f"🇺🇸 امريكا ( {US} )",f"🇦🇴 انغولا ( {ANG} )",f"🇦🇷 الارجنتين ( {ARG} )",f"🇦🇿 اذربيجان ( {AZ} )",f"🇧🇬 بلغاريا ( {BUL} )",f"🇨🇿 التشيك ( {CZ} )",f"🇪🇪 أستونيا ( {AST} )",f"🇫🇷 فرنسا ( {FR} )",f"🇬🇪 جورجيا ( {GOR} )",f"🇭🇰 هونغ كونغ ( {CH} )",f"🇮🇩 إندونيسيا ( {END} )",f"🇮🇱  إسرائيل ( {ISR} )",f"🇱🇻 لاتفيا ( {LTV} )",f"🇱🇹 ليتوانيا ( {LET} )",f"🇲🇽 المكسيك ( {MAX} )",f"🇳🇱 هولندا ( {HOL} )",f"🇵🇰 باكستان ( {BKS} )",f"🇬🇧 بريطانيا  ( {UK} )",f"🇷🇺 روسيا ( {RU} )"]]
				pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
				for pair in pairs:
					keyboard.row(*pair)
				keyboard.add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙اختر الدوله المراد شراء رقم منها ↯ :
	________
		''',reply_markup=keyboard)
	
			elif call.data == "Go":
				dalEx.set(f"alEx-{call.message.chat.id}","go")
				
				keyboard = types.InlineKeyboardMarkup(row_width=2)
				buttons = [types.InlineKeyboardButton(alex, callback_data=f"{alex}") for alex in [f'🇬🇷 اليونان ( {GRS} )',f"🇺🇸 امريكا ( {US} )",f"🇦🇴 انغولا ( {ANG} )",f"🇦🇷 الارجنتين ( {ARG} )",f"🇦🇿 اذربيجان ( {AZ} )",f"🇧🇬 بلغاريا ( {BUL} )",f"🇨🇿 التشيك ( {CZ} )",f"🇪🇪 أستونيا ( {AST} )",f"🇫🇷 فرنسا ( {FR} )",f"🇬🇪 جورجيا ( {GOR} )",f"🇭🇰 هونغ كونغ ( {CH} )",f"🇮🇩 إندونيسيا ( {END} )",f"🇮🇱  إسرائيل ( {ISR} )",f"🇱🇻 لاتفيا ( {LTV} )",f"🇱🇹 ليتوانيا ( {LET} )",f"🇲🇽 المكسيك ( {MAX} )",f"🇳🇱 هولندا ( {HOL} )",f"🇵🇰 باكستان ( {BKS} )",f"🇬🇧 بريطانيا  ( {UK} )",f"🇷🇺 روسيا ( {RU} )"]]
				pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
				for pair in pairs:
					keyboard.row(*pair)
				keyboard.add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙اختر الدوله المراد شراء رقم منها ↯ :
	________
		''',reply_markup=keyboard)
				
			elif call.data == 'TG':
				dalEx.set(f"alEx-{call.message.chat.id}","tg")
				keyboard = types.InlineKeyboardMarkup(row_width=2)
				buttons = [types.InlineKeyboardButton(alex, callback_data=f"{alex}") for alex in [f'🇬🇷 اليونان ( {GRS} )',f"🇺🇸 امريكا ( {US} )",f"🇦🇴 انغولا ( {ANG} )",f"🇦🇷 الارجنتين ( {ARG} )",f"🇦🇿 اذربيجان ( {AZ} )",f"🇧🇬 بلغاريا ( {BUL} )",f"🇨🇿 التشيك ( {CZ} )",f"🇪🇪 أستونيا ( {AST} )",f"🇫🇷 فرنسا ( {FR} )",f"🇬🇪 جورجيا ( {GOR} )",f"🇭🇰 هونغ كونغ ( {CH} )",f"🇮🇩 إندونيسيا ( {END} )",f"🇮🇱  إسرائيل ( {ISR} )",f"🇱🇻 لاتفيا ( {LTV} )",f"🇱🇹 ليتوانيا ( {LET} )",f"🇲🇽 المكسيك ( {MAX} )",f"🇳🇱 هولندا ( {HOL} )",f"🇵🇰 باكستان ( {BKS} )",f"🇬🇧 بريطانيا  ( {UK} )",f"🇷🇺 روسيا ( {RU} )"]]
				pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
				for pair in pairs:
					keyboard.row(*pair)
				keyboard.add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
				alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙اختر الدوله المراد شراء رقم منها ↯ :
	________
		''',reply_markup=keyboard)
		
		
			elif call.data == f"🇷🇺 روسيا ( {RU} )":
				Price = dalEx.get("Reg-US")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=0").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇵🇰 باكستان ( {BKS} )":
				Price = dalEx.get("Reg-BKS")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=66").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)

			elif call.data == f"🇬🇷 اليونان ( {GRS} )":
				Price = dalEx.get("Reg-GRS")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=129").text
					print(GetNumber)
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)		
			elif call.data == f"🇳🇱 هولندا ( {HOL} )":
				Price = dalEx.get("Reg-HOL")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=48").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
		
			elif call.data == f"🇲🇽 المكسيك ( {MAX} )":
				Price = dalEx.get("Reg-MAX")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=52").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇱🇹 ليتوانيا ( {LET} )":
				Price = dalEx.get("Reg-LET")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=44").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)	
			elif call.data == f"🇱🇻 لاتفيا ( {LTV} )":
				Price = dalEx.get("Reg-LTV")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=49").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇮🇱  إسرائيل ( {ISR} )":
				Price = dalEx.get("Reg-ISR")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=13").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇮🇩 إندونيسيا ( {END} )":
				Price = dalEx.get("Reg-END")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=6").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
			elif call.data == f"🇬🇧 بريطانيا  ( {UK} )":
				Price = dalEx.get("Reg-UK")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=16").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin+1)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
			elif call.data == f"🇦🇴 انغولا ( {ANG} )":
				Price = dalEx.get("Reg-ANG")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=76").text
					print(GetNumber)
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
			elif call.data == f"🇦🇷 الارجنتين ( {ARG} )":
				Price = dalEx.get("Reg-ARG")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=39").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇦🇿 اذربيجان ( {AZ} )":
				Price = dalEx.get("Reg-AZ")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=35").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇧🇬 بلغاريا ( {BUL} )":
				Price = dalEx.get("Reg-BUL")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=83").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇨🇿 التشيك ( {CZ} )":
				Price = dalEx.get("Reg-CZ")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=63").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇪🇪 أستونيا ( {AST} )":
				Price = dalEx.get("Reg-AST")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service=tg&country=34").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇫🇷 فرنسا ( {FR} )":
				
				
				Price = dalEx.get("Reg-FR")
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=78").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
			
			elif call.data == f"🇬🇪 جورجيا ( {GOR} )":
				Price = dalEx.get("Reg-GOR")
				Ti = choice([1,2]);sleep(int(Ti))
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == Price or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=128").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		""", show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
		
			elif call.data == f"🇺🇸 امريكا ( {US} )":
				Price = dalEx.get("Reg-US")
				Ti = choice([1,2]);sleep(int(Ti))
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				Coin = int(dalEx.get(f'{call.message.chat.id}'))
				if Coin == int(Price) or Coin > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=187").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
	
			elif call.data == f"🇭🇰 هونغ كونغ ( {CH} )":
				Price = dalEx.get("Reg-CH")
				Ti = choice([1,2]);sleep(int(Ti))
				NumberType=dalEx.get(f"alEx-{call.message.chat.id}")
				
				if int(dalEx.get(f'{call.message.chat.id}')) == int(Price) or int(dalEx.get(f'{call.message.chat.id}')) > int(Price):
					GetNumber = get(f"https://vak-sms.com/stubs/handler_api.php?api_key={apikey}&action=getNumber&service={NumberType}&country=14").text
					
					if 'ACCESS_NUMBER'in GetNumber:
						UtCoin = int(dalEx.get(f'{call.message.chat.id}'))-int(Price)
						dalEx.set(f"Buy-{call.message.chat.id}",Price)
						AllCoin=int(dalEx.get(f"allBuy-{call.message.chat.id}"))+1
						dalEx.set(f"allBuy-{call.message.chat.id}",AllCoin)
						dalEx.set(f'{call.message.chat.id}',UtCoin)
						Delet = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( حذف الرقم )',callback_data='delet'))
						Delet.add(types.InlineKeyboardButton("( تحديث صندوق الوارده )",callback_data='Update'))
						Number = GetNumber.split(':')[2]
						Id_Number = GetNumber.split(':')[1]
						dalEx.set(f"sms-{call.message.chat.id}",0)
						alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
			[√] تم شراء رقم بنجاح ✅ .
			
	↯︙الرقم ~> `{Number}`+ •
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙ايديك ~> {call.message.chat.id} •
		
		× ملاحظة ! : يمكنك حذف الرقم خلال 20 دقيقة واسترجاع نقاطك ( فقط خلال 20 د ) !
		''',reply_markup=Delet,parse_mode="markdown")
					else:
						alEx.answer_callback_query(call.id, text="""
		    ⚠️ - لا توجد سيرفرات على هذا البلد .
		    """, show_alert=True)
				else:
					Dev = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( المطور )',url='M_L_F.t.me'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		• عذرا نقاطك غير كافية !
		
		• يرجى مراسلة المطور لشراء نقاط ↯:
		''',reply_markup=Dev)
	
			elif call.data == 'delet':
				Id_Number = str(call.message.text).split('↯︙ايدي الرقم ~> ')[1].split(' •')[0]
				DeletNumber = get(f"https://vak-sms.com/api/setStatus/?apiKey={apikey}&status=bad&idNum={Id_Number}").text
				print(DeletNumber)
				if 'update' in  DeletNumber:
					Back=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
					Coin = int(dalEx.get(f'{call.message.chat.id}'))
					GetCoin = int(dalEx.get(f"Buy-{call.message.chat.id}"))
					dalEx.set(f'{call.message.chat.id}',Coin+GetCoin)
					
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
		↯︙تم حذف الرقم بنجاح ❌ .
		
		↯︙تم استرجاع نقاطك ({GetCoin}) •
		↯︙يمكنك شراء مره اخره بأي وقت تريد ✅ ↯
		''',reply_markup=Back)
		
				elif "smsReceived" in DeletNumber:
					Back=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙عذرا لا يمكنك حذف الرقم •
		↯︙السبب : تم وصول كود ❗•
		
		↯︙اطلب رقم اخر :
		''',reply_markup=Back)
	
				elif "idNumNotFound" in DeletNumber:
					alEx.answer_callback_query(call.id,text="⚠️ انتهت الـ 20 د لم يعد الرقم ملكك .",show_alert=True)
		
			elif call.data == 'Code':
				Id_Number = str(call.message.text).split('↯︙ايدي الرقم ~> ')[1].split(' •')[0]
				SmSTow = get(f"https://vak-sms.com/api/setStatus/?apiKey={apikey}&status=send&idNum={Id_Number}").text
				if '"countSMS": 1' in SmSTow:
					alEx.answer_callback_query(call.id,text='''
	✅ تم طلب كود جديد بنجاح .''',show_alert=True)
	
				elif "idNumNotFound" in SmSTow:
					Back=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( رجوع )',callback_data='Back'))
					alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
		↯︙عذرا لا يمكنك طلب كود جديد •
		↯︙السبب : انتهت الـ 20 د • ❗•
		
		↯︙اطلب رقم اخر :
		''',reply_markup=Back)
			elif call.data == 'Update':
				Id_Number = str(call.message.text).split('↯︙ايدي الرقم ~> ')[1].split(' •')[0]	
				GetSmS = get(f"https://vak-sms.com/api/getSmsCode/?apiKey={apikey}&idNum={Id_Number}").text
				
				SmSTow = get(f"https://vak-sms.com/api/setStatus/?apiKey={apikey}&status=send&idNum={Id_Number}").text
				print(SmSTow)
				
				if '"countSMS": 0' in SmSTow:
					alEx.answer_callback_query(call.id,text='''
		⚠ لم يتم وصول رسالة جديده بعد ! .
		''')
	
				elif '"countSMS": 1' in SmSTow:
					if "idNumNotFound" not in GetSmS and "null" not in GetSmS:
						SmS2=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("( الكود )",callback_data='Code'))
							
						CodeTg = GetSmS.split('{"smsCode": "')[1].split('"}')[0]
						Upd=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( تحديث )',callback_data='Update'))
						if dalEx.get(f"sms-{call.message.chat.id}") == 1:
							alEx.answer_callback_query(call.id,text='''
		⚠ لم يتم وصول رسالة بعد ❗.
		''')
						dalEx.set(f"sms-{call.message.chat.id}",1)
						alEx.send_message(call.message.chat.id,f'''
		↯︙تم استلام كود بنجاح ✅ •
				
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙الكود ~> (`{CodeTg}`) •
		
		× ملاحظة : في حال لم يعد الكود صالح يمكنك الضغط على الزر ادناه لطلب كود من جديد فقط مره واحده ❗
				•''',reply_markup=SmS2,parse_mode="markdown")
					elif 'idNumNotFound' in GetSmS:
						alEx.answer_callback_query(call.id,text='''
		❌ الرقم منتهي الصلاحية !
		''')
					elif "null" in GetSmS:
						alEx.answer_callback_query(call.id,text='''
		⚠ لم يتم وصول رسالة بعد ❗.
		''')
				
				elif '"countSMS": 2' in SmSTow:
					if "idNumNotFound" not in GetSmS and "null" not in GetSmS:
							SmS2=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("( الكود )",callback_data='Code'))
							
							CodeTg = GetSmS.split('{"smsCode": "')[1].split('"}')[0]
							Upd=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( تحديث )',callback_data='Update'))
							
							
							
							alEx.send_message(call.message.chat.id,f'''
		↯︙تم استلام كود بنجاح ✅ •
				
		↯︙ايدي الرقم ~> {Id_Number} •
		↯︙الكود ~> (`{CodeTg}`) •
		
		× ملاحظة : في حال لم يعد الكود صالح يمكنك الضغط على الزر ادناه لطلب كود من جديد فقط مره واحده ❗
				•''',reply_markup=SmS2,parse_mode="markdown")
					elif 'idNumNotFound' in GetSmS:
						alEx.answer_callback_query(call.id,text='''
		❌ الرقم منتهي الصلاحية !
		''')
					elif "null" in GetSmS:
						alEx.answer_callback_query(call.id,text='''
		⚠ لم يتم وصول رسالة بعد ❗.
		''')
	else:
			alEx.answer_callback_query(call.id,text="❗اضغط الزر كل ثلاث ثواني .")
			
				
#متكدر تخمط 😁 .
alEx.infinity_polling()