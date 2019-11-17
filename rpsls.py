#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：朱如勇
日期：11.16
"""
# 0 - 石头
# 1 - 史波克
# 2 - 布
# 3 - 蜥蜴
# 4 - 剪刀
def name_to_number(choice_name):#建立函数
	if choice_name=="石头": # 使用if/elif/else语句将各游戏对象对应到不同的整数
		choice_number=int(0)
		return choice_number#返回结果
	elif choice_name=="史波克":
		choice_number=int(1)
		return choice_number#返回结果
	elif choice_name=="布":
		choice_number=int(2)
		return choice_number#返回结果
	elif choice_name=="蜥蜴":
		choice_number=int(3)
		return choice_number#返回结果
	elif choice_name=="剪刀":
		choice_number=int(4)
		return choice_number#返回结果
	else:
		choice_number=int(5)
		return choice_number	 
		
		   
def number_to_name(comp_number):#建立函数
	if comp_number==0: # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
	   comp_name="石头"
	   return comp_name
	elif comp_number==2:
		comp_name="布"
		return comp_name
	elif comp_number==3:
		comp_name="蜥蜴"
		return comp_name#分别返回结果
	elif comp_number==1:
		comp_name="史波克"
		return comp_name
	elif comp_number==4:
		comp_name="剪刀"
		return comp_name
		
		
def rpsls(choice_number,comp_number):#建立函数判断胜负
	dif=choice_number-comp_number
	if dif==-3 or dif==-4 or dif==1 or dif==2:#判断条件
		print("你赢了")
	elif dif==0:
		print("你和计算机出的一样呢")
	else:
		print("计算机赢了")
		
		
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入你的选择：")
choice_name=input()#输入自己的选择
choice_number=name_to_number(choice_name)#调用函数，得到选择所对应的数字
if choice_number==5:
   print("Error: No Correct Name")
else:
	import random#调用randon函数，让计算机随机报出一个数
	comp_number=random.randrange(0,5)#把随机的数赋值给comp_number
	comp_name=number_to_name(comp_number)#调用函数，得到该数对应的选择
	print("计算机的选择为：%s"%comp_name)#利用占字符输出结果
	rpsls(choice_number,comp_number)#调用函数，得到结果

	
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
