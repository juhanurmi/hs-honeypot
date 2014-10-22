"""This script generates torrc configure file for Tor."""
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
    FILE_PATH = "/var/lib/tor/hss/"
    torrc_conf = "SocksPolicy accept 10.8.0.0/24\n"
    torrc_conf = torrc_conf + "SocksPolicy accept 127.0.0.0/8\n\n"
    torrc_conf = torrc_conf + "ControlPort 9051\n\n"
    for id_num in range(0,10):
        id_str = str(id_num).zfill(3)
        torrc_conf = torrc_conf + "# Hidden Service " + id_str + "\n"
        torrc_conf = torrc_conf + "HiddenServiceDir " + FILE_PATH + "hidden_service_" + id_str + "/\n"
        torrc_conf = torrc_conf + "HiddenServicePort 21 127.0.0.1:" + str(port+21) + "\n"
        torrc_conf = torrc_conf + "HiddenServicePort 22 127.0.0.1:" + str(port+22) + "\n"
        torrc_conf = torrc_conf + "HiddenServicePort 80 127.0.0.1:" + str(port+80) + "\n\n"
        port = port + 100
    text2file( torrc_conf, "torrc")

if __name__ == '__main__':
    main()