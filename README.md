# DNSleuth

DNSleuth is a Python tool that sniffs DNS packets i.e lets you spy on the DNS queries your machine is making

## Usage

To install DNSleuth, simply run the `setup.sh`

```bash
git clone https://github.com/devanshbatham/DNSleuth
cd DNSleuth
./setup.sh
```

and run the following:

```bash
dnsleuth
```


DNSleuth will start sniffing DNS packets on all interfaces and print the DNS queries with colors.To stop DNSleuth, press `Ctrl+C`. 



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
## Dependencies

DNSleuth requires the following dependencies:

* Python 3.x
* Scapy
* Colorama