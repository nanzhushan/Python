����Ҫ��������ַ�����Python�ڲ��ı�ʾ��unicode����. 

��ˣ���������ת��ʱ��ͨ����Ҫ��unicode��Ϊ�м���룬
���Ƚ�����������ַ������루decode����unicode���ٴ�unicode���루encode������һ�ֱ���.

decode�������ǽ�����������ַ���ת����unicode���룬 
��str1.decode('gb2312')����ʾ��gb2312������ַ���ת����unicode���롣
 
encode�������ǽ�unicode����ת��������������ַ����� 
��str2.encode('gb2312')����ʾ��unicode������ַ���ת����gb2312���롣 

����:

(1)
����UliPad���������´��룺 
s=u"����" 
print s 

����ʾ�� 
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)�� 

������ΪUliPad��Ӣ��WindowsXP�ϵĿ���̨��Ϣ��������ǰ���ascii��������ģ�Ӣ��ϵͳ��Ĭ�ϱ�����ascii����
����������е��ַ�����Unicode����ģ��������ʱ�����˴��� 

�����һ���Ϊ��print s.encode('gb2312') ������ȷ��������ġ������֡� 

�����һ���Ϊ��print s.encode('utf8') �������\xe4\xb8\xad\xe6\x96\x87�� 
���ǿ���̨��Ϣ������ڰ���ascii�������utf8������ַ����Ľ����
 
(2)
����ַ������������壺 s=u'����' ����ַ����ı���ͱ�ָ��Ϊunicode�ˣ���python���ڲ����룬��������ļ�����ı����޹ء� 
��ˣ������������������ת����ֻ��Ҫֱ��ʹ��encode��������ת����ָ�����뼴�ɡ� 
���һ���ַ����Ѿ���unicode�ˣ��ٽ��н����򽫳��� 

���ͨ��Ҫ������뷽ʽ�Ƿ�Ϊunicode�����жϣ� 
isinstance(s, unicode) #�����ж��Ƿ�Ϊunicode 



