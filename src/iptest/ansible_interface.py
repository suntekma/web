# -*- coding:utf-8 -*-
import json
from ansible_api import AnsibleAPI


class AnsiInterface(AnsibleAPI):
    def __init__(self, resource, *args, **kwargs):
        super(AnsiInterface, self).__init__(resource, *args, **kwargs)

    @staticmethod
    def deal_result(info):
        host_ips = info.get('success').keys()
        info['success'] = host_ips

        error_ips = info.get('failed')
        error_msg = {}
        for key, value in error_ips.items():
            temp = {}
            temp[key] = value.get('stderr')
            error_msg.update(temp)
        info['failed'] = error_msg
        return json.dumps(info)

    def copy_file(self, host_list, src=None, dest=None):
        """
        copy file
        """
        module_args = "src=%s  dest=%s"%(src, dest)
        self.run(host_list, 'copy', module_args)
        result = self.get_result()
        return self.deal_result(result)

    def exec_command(self, host_list, cmds):
        """
        commands
        """
        self.run(host_list, 'command', cmds)
        result = self.get_result()
        return self.deal_result(result)

    def exec_script(self, host_list, path):
        """
        ��Զ������ִ��shell�������.sh�ű�
        """
        self.run(host_list, 'shell', path)
        result = self.get_result()
        return self.deal_result(result)

    def Get_face(self, host_list):
        """
        ��ȡԶ������faces
        """
        self.run(host_list, 'setup','')
        result = self.get_result()
        return self.deal_result(result)


if __name__ == "__main__":
    resource = [{"hostname": "10.16.50.181", "port": "22", "username": "root", "password": "newegg@123", "ip": '10.16.50.181'}]
    interface = AnsiInterface(resource)
    print "copy: ", interface.copy_file(['10.16.50.181'], src='/Users/majing/test1.py', dest='/opt')
    print "commands: ", interface.exec_command(['10.16.50.181'], 'hostname')
    print "shell: ", interface.exec_script(['10.16.50.181'], 'chdir=/home ls')
    print "shell: ", interface.exec_script(['10.16.50.181'], 'sh /opt/test.sh')
    print "setup: ", interface.Get_face(['10.16.50.181'])
    