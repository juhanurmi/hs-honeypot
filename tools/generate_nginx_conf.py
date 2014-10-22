"""This script generates nginx configure file for Tor."""
# -*- coding: utf-8 -*-
import codecs  # UTF-8 support for the text files


def text2file(txt, filename):
    """Write the txt to the file."""
    outputfile = codecs.open(filename, "w", "utf-8")
    outputfile.write(txt)
    outputfile.close()

def main():
    """Main function."""
    port = 10000
    nginx_conf = """log_format mycustomformat '$host $remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent "$http_referer" '
                  '"$http_user_agent" $server_port';\n\n"""
    for id_num in range(0,100):
        nginx_conf = nginx_conf + "server {\n"
        id_str = str(id_num).zfill(6)
        nginx_conf = nginx_conf + "\tlisten 127.0.0.1:" + str(port+21) + ";\n"
        nginx_conf = nginx_conf + "\tlisten 127.0.0.1:" + str(port+22) + ";\n"
        nginx_conf = nginx_conf + "\tlisten 127.0.0.1:" + str(port+80) + ";\n"
        nginx_conf = nginx_conf + "\troot /usr/share/nginx/html;\n"
        nginx_conf = nginx_conf + "\tindex index.html index.htm;\n"
        nginx_conf = nginx_conf + "\tserver_name " + id_str + ";\n"
        nginx_conf = nginx_conf + "\taccess_log /var/log/nginx/hs_logs/" + id_str + ".access mycustomformat;\n"
        nginx_conf = nginx_conf + "\tlocation / {\n"
        nginx_conf = nginx_conf + "\t\ttry_files $uri $uri/ =404;\n"
        nginx_conf = nginx_conf + "\t}\n"
        nginx_conf = nginx_conf + "\terror_log /var/log/nginx/hs_logs/" + id_str + ".error error;\n"
        nginx_conf = nginx_conf + "}\n\n"
        port = port + 100
    text2file( nginx_conf, "hs")

if __name__ == '__main__':
    main()
