#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�11.16
"""
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����
def name_to_number(choice_name):#��������
	if choice_name=="ʯͷ": # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
		choice_number=int(0)
		return choice_number#���ؽ��
	elif choice_name=="ʷ����":
		choice_number=int(1)
		return choice_number#���ؽ��
	elif choice_name=="��":
		choice_number=int(2)
		return choice_number#���ؽ��
	elif choice_name=="����":
		choice_number=int(3)
		return choice_number#���ؽ��
	elif choice_name=="����":
		choice_number=int(4)
		return choice_number#���ؽ��
	else:
		choice_number=int(5)
		return choice_number	 
		
		   
def number_to_name(comp_number):#��������
	if comp_number==0: # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
	   comp_name="ʯͷ"
	   return comp_name
	elif comp_number==2:
		comp_name="��"
		return comp_name
	elif comp_number==3:
		comp_name="����"
		return comp_name#�ֱ𷵻ؽ��
	elif comp_number==1:
		comp_name="ʷ����"
		return comp_name
	elif comp_number==4:
		comp_name="����"
		return comp_name
		
		
def rpsls(choice_number,comp_number):#���������ж�ʤ��
	dif=choice_number-comp_number
	if dif==-3 or dif==-4 or dif==1 or dif==2:#�ж�����
		print("��Ӯ��")
	elif dif==0:
		print("��ͼ��������һ����")
	else:
		print("�����Ӯ��")
		
		
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("���������ѡ��")
choice_name=input()#�����Լ���ѡ��
choice_number=name_to_number(choice_name)#���ú������õ�ѡ������Ӧ������
if choice_number==5:
   print("Error: No Correct Name")
else:
	import random#����randon�������ü�����������һ����
	comp_number=random.randrange(0,5)#�����������ֵ��comp_number
	comp_name=number_to_name(comp_number)#���ú������õ�������Ӧ��ѡ��
	print("�������ѡ��Ϊ��%s"%comp_name)#����ռ�ַ�������
	rpsls(choice_number,comp_number)#���ú������õ����

	
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
