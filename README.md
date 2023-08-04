<h1 align="center">
    DNSleuth
  <br>
</h1>

<h4 align="center">DNSleuth sniffs DNS packets, i.e, allowing you to spy on the DNS queries your machine is making</h4>


<p align="center">
  <a href="#usage">⛏️ Usage</a>
  <a href="#dependencies">📦 Dependencies</a>
  <br>
</p>


# Usage

To install DNSleuth, simply run the `setup.sh` script:

```bash
git clone https://github.com/devanshbatham/DNSleuth
cd DNSleuth
sudo chmod +x setup.sh
./setup.sh
```

and run the following command to start DNSleuth:

```bash
dnsleuth
```

DNSleuth will start sniffing DNS packets on all interfaces and print the DNS queries with colors. To stop DNSleuth, press `Ctrl+C`. 

```bash
(~) >>> dnsleuth                                                                                             

[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] A          oast.site.
[2023-07-31 19:34:41] A          oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
[2023-07-31 19:34:41] AAAA       oast.site.
```

# Dependencies

DNSleuth requires the following dependencies:

* Python 3.x
* Scapy
* Colorama
