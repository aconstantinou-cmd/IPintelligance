import webbrowser
import re

print("This Python Script searches AlientVault, ThreatCrowd and Shodan databases with a provided IP address.")
print("------------------------------------------------------------------------------------------------------")
print("Please type or copy & paste an IP address")
print("------------------------------------------------------------------------------------------------------")

url= 'https://otx.alienvault.com'
url2= 'https://www.threatcrowd.org'
url3= 'https://www.shodan.io'

def input():
    i=raw_input("Enter an IP:  ")
    pat=re.compile("^((2[0-4][0-9]|25[0-5]|1[0-9]{0,2}|0?[0-9]{2}|[0-9])\.){3}(2[0-4][0-9]|25[0-5]|1[0-9]{0,2}|0?[0-9]{2}|[0-9])$")
    if pat.match(i):
        webbrowser.open_new_tab(url+'/browse/pulses/?q='+i+'&sort=-created')
        webbrowser.open_new_tab(url2+'/ip.php?ip='+i)
        webbrowser.open_new_tab(url3+'/host/'+i)
        print("working................")

    elif i=="":
        print("------------------------------------------------------------------------------------------------------")
        print("No dumbass, enter an IP Address")

    else:
     if i!=pat:
        print("------------------------------------------------------------------------------------------------------")
        print("Invalid IP detected")

input()
