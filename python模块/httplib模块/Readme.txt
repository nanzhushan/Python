httplib�ṩ�ĳ��õ����ͺͷ���:

(1)httplib.HTTPConnection ( host [ , port [ , strict [ , timeout ]]] )

HTTPConnection��Ĺ��캯������ʾһ���������֮��Ľ�����������/��Ӧ������host��ʾ������������ �磺www.csdn.net��portΪ�˿ںţ�Ĭ��ֵΪ80�� ����strict�� Ĭ��ֵΪfalse��
��ʾ���޷��������������ص�״̬��ʱ( status line) ���Ƚϵ��͵�״̬���磺 HTTP/1.0 200 OK �����Ƿ���BadStatusLine �쳣����ѡ����timeout ��ʾ��ʱʱ�䡣

(2)HTTPConnection.request ( method , url [ , body [ , headers ]] )

����request �����������������һ������method ��ʾ����ķ����������з�����get ��post��
url ��ʾ�������Դ��url ��
body ��ʾ�ύ�������������ݣ��������ַ��������method ��"post" ������԰�body ���Ϊhtml ���е����ݣ���
headers ��ʾ�����http ͷ��

(3)HTTPConnection.getresponse ()

��ȡHttp ��Ӧ�����صĶ�����HTTPResponse ��ʵ��������HTTPResponse ������ �ὲ�⡣

(4)HTTPConnection.connect ()
���ӵ�Http ��������

(5)HTTPConnection.close ()
�ر�������������ӡ�

(6)HTTPConnection.set_debuglevel ( level )
���ø߶ȵļ��𡣲���level ��Ĭ��ֵΪ0 ����ʾ������κε�����Ϣ��

(7)httplib.HTTPResponse
HTTPResponse��ʾ�������Կͻ����������Ӧ������ͨ������HTTPConnection.getresponse()���������������·��������ԣ�

(8)HTTPResponse.read([amt])
��ȡ��Ӧ����Ϣ�塣����������һ����ͨ����ҳ����ô�÷������ص���ҳ���html����ѡ����amt��ʾ����Ӧ���ж�ȡָ���ֽڵ����ݡ�

(9)HTTPResponse.getheader(name[, default])
��ȡ��Ӧͷ��Name��ʾͷ��(header field)������ѡ����default��ͷ���������ڵ��������ΪĬ��ֵ���ء�

(10)HTTPResponse.getheaders()
���б����ʽ�������е�ͷ��Ϣ��

(11)HTTPResponse.msg
��ȡ���е���Ӧͷ��Ϣ��

(12)HTTPResponse.version
��ȡ��������ʹ�õ�httpЭ��汾��11��ʾhttp/1.1��10��ʾhttp/1.0��

(13)HTTPResponse.status
��ȡ��Ӧ��״̬�롣�磺200��ʾ����ɹ���

(14)HTTPResponse.reason
���ط�������������Ľ��˵����һ��Ϊ��OK��

