# PasteJacker [![Python 3.5](https://img.shields.io/badge/Python-3.0+-yellow.svg)](http://www.python.org/download/) ![Version](https://img.shields.io/badge/Version-1.0-red.svg)
The main purpose of the tool is automating (PasteJacking/Clipboard poisoning/whatever you name it) attack with collecting all the known tricks used in this attack in one place and one automated job as after searching I found there's no tool doing this job the right way :smile:

Now while this attack depends on what the user will paste, imagine adding this attack to metasploit web delivery module.

##### This tool uses 3 methods to trick user into copying our payload instead of the command he copies:
 + **Using javascript to hook the copy event and replace copied data.**
    - Advantages :
        1. Anything the user copies in the page will be replaced with our line.
        2. Command executed by itself once target paste it without pressing enter.
    - Disadvantages :
        1. Requires Javascript to be enabled on the target browser.


 + **Using span style attribute to hide our lines by overwriting.**
    - Advantages :
        1. Doesn't require javascript to be enabled.
        2. Works on all browsers.
    - Disadvantages :
        1. Target must select all the text in the page or the first two words to ensure that he copies our hidden malicious lines.


 + **Using span style again but this time to make our text transparent and non-markable.**
    - Advantages :
        1. Doesn't require javascript to be enabled.
    - Disadvantages :
        1. Target must select all the text in the page to ensure that he copies our hidden malicious lines.
        2. Not working on opera and chrome.

##### What's the payload user copies ?
PasteJacker gives you the option to do one of this things:
  1. Generate a msfvenom backdoor on our machine and the liner targets copy will download the backdoor on the target machine, through wget or certutil depends on the OS, then executes it on the background without printing anything to the terminal.
  2. Serve a liner that gets you a reverse netcat connection on the target machine running in the background of course.
  3. Serve your **custom** liner like Metasploit web-delivery payload with adding some touches to hide any possible output.

# Screenshots

<img src="https://github.com/D4Vinci/PasteJacker/blob/master/PasteJacker/Screenshots/p0.png" width="100%"></img>
<img src="https://github.com/D4Vinci/PasteJacker/blob/master/PasteJacker/Screenshots/p1.png" width="100%"></img>
<img src="https://github.com/D4Vinci/PasteJacker/blob/master/PasteJacker/Screenshots/p2.png" width="100%"></img>
<img src="https://github.com/D4Vinci/PasteJacker/blob/master/PasteJacker/Screenshots/p3.png" width="100%"></img>

## Installing and requirements
- Python 3
- Linux or Unix-based system (Currently tested only on Kali Linux rolling and Ubuntu 16.04)
- Third-party requirements like msfvenom but only if you are gonna use the msfvenom option of course
- Third-party library ncurses-dev for Ubuntu (Thanks for @mhaskar)
- Root access

### Installing

+ **For Linux :**
```
git clone https://github.com/D4Vinci/PasteJacker.git
sudo python3 -m pip install ./PasteJacker
sudo pastejacker
```

## Updating the framework or the database
- On Linux while outside the directory
```
cd PasteJacker && git pull && cd ..
sudo python3 -m pip install ./PasteJacker --upgrade
```

## References

- [PasteJacking GitHub repo](https://github.com/dxa4481/Pastejacking)
- [Clipboard poisoning attacks on the Mac - Malwarebytes ](https://blog.malwarebytes.com/threat-analysis/2016/05/clipboard-poisoning-attacks-on-the-mac/)
- [Metasploit web delivery module ](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/script/web_delivery.rb)

## Contact
- [Twitter](https://twitter.com/D4Vinci1)

## Donation
If this tool has been useful for you, feel free to thank me by buying me a coffee :)

[![Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoff.com/d4vinci)

## Disclaimer
PasteJacker is created to help in penetration testing and it's not responsible for any misuse or illegal purposes.

Copying a code from this tool or using it in another tool is accepted as you mention where you get it from :smile:.

> Pull requests are always welcomed :D
