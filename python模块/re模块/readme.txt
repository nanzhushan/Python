(1)Python REģ����search()��match()������:

match��������ֻ���RE�ǲ�����string�Ŀ�ʼλ��ƥ�䣬
 search()��ɨ������string����ƥ�䣻
Ҳ����˵match����ֻ����0λ��ƥ��ɹ��Ļ����з��أ�
������ǿ�ʼλ��ƥ��ɹ��Ļ���match()�ͷ���none��

���磺
print(re.match(��super��, ��superstition��).span())   �᷵��(0, 5)
��print(re.match(��super��, ��insuperable��))   �򷵻�None

search()��ɨ�������ַ��������ص�һ���ɹ���ƥ��
���磺print(re.search(��super��, ��superstition��).span())����(0, 5)
print(re.search(��super��, ��insuperable��).span())����(2, 7)