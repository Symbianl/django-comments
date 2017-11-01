# -*-coding:utf-8 -*-
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template import loader
from django.conf import settings

class SendEmail():
    '''send email'''
    def __init__(self):
        pass

    def send_html_email(self,subject,html_content,to_list):
        '''发送html邮件'''
        send_from = settings.DEFAULT_FROM_EMAIL
        msg = EmailMessage(subject,html_content,send_from,to_list)
        msg.content_subtype = 'html'#设置类型html
        msg.send()

    def send_text_email(self,subject,body,to_list,is_fail_silently=False):
        """发送简单的文本邮件"""
        send_from = settings.DEFAULT_FROM_EMAIL
        send_mail(subject,body,send_from,to_list,fail_silently=is_fail_silently)

    def send_email_by_template(self,subject,module,data,to_list):
        """
        使用模板发送邮件
        :param subject: string, 主题
        :param module: string , 模板名称
        :param data: dict, 数据
        :param to_list: list, 收件人
        :return:
        """
        html_content = loader.render_to_string(module,data)
        self.send_html_email(subject,html_content,to_list)
















