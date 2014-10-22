hs-honeypot - Honeypot Hidden Service system
============================================

This is a simple way to build honeypot system. These scripts deploy hidden services and setup nginx to log the traffic.

Tutorial
--------

- Install Tor
- Generate torrc configuration for Tor

```sh
$ cp torrc /etc/tor/torcc
$ mkdir /var/lib/tor/hss/
$ chmod 777 /var/lib/tor/hss/
```

- Install nginx
- Generate nginx configuration

```sh
$ rm /etc/nginx/sites-available/default
$ cp hs /etc/nginx/sites-available/hs
$ ln -s /etc/nginx/sites-available/hs /etc/nginx/sites-enabled/hs
```

Finally, restart the services and your logging systems is ready.

```sh
$ service nginx restart
$ service tor restart
```

You can follow possible TCP traffic to selected ports.

```sh
$ ls -l /var/log/nginx/hs_logs/
```
