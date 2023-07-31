# DNSleuth

DNSleuth is a Python tool that sniffs DNS packets i.e lets you spy on the DNS queries your machine is making

## Usage

To install DNSleuth, simply run the `setup.sh`

```
./setup.sh
```


and run the following:

```
dnsleuth
```



DNSleuth will start sniffing DNS packets on all interfaces and print the DNS queries with colors.To stop DNSleuth, press `Ctrl+C`. 


## Dependencies

DNSleuth requires the following dependencies:

* Python 3.x
* Scapy
* Colorama