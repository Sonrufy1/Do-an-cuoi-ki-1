from googletrans import Translator
text_input = str (input("Nhập vào thứ bạn muốn dịch: "))
dict = Translator ()
dict_action = dict.translate(text=text_input, src="en", dest="vi")
print(dict_action)



