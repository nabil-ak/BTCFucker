#Public Key: wallet.address.mainnet.pubaddr1
#Private Key: wallet.key.mainnet.wif
import json
import requests
import time
import sys
import threading
from multiprocessing import Process
from discord_webhook import DiscordWebhook, DiscordEmbed
from bitcoinaddress import Wallet

DISCORDWEBHOOK = ""


def runInstance(pID,tID):
    currentwallets = 0
    addressperRequest = 140
    messageInterval = 120
    nextMessage = time.time() + messageInterval + pID + tID
    sendMessage(f"STARTED",pID,tID)
    while True:
        wallets = []
        requestAdress = "https://blockchain.info/balance?active="
        for x in range(addressperRequest):
            wallet = Wallet()
            wallets.append(wallet)
            requestAdress += wallet.address.mainnet.pubaddr1+","
        
        request = requests.get(requestAdress)
        if request.status_code != 200:
            print(f"{pID}.{tID} || HTTP Error :{request.status_code} with accesing Blockchain.info\n{request.content}")
            sendMessage(f"HTTP Error {request.status_code}",pID,tID,1)
            exit()

        response = json.loads(request.content)
        for x in range(addressperRequest):
            if list(response.values())[x]["final_balance"] != 0:
                for y in range(addressperRequest):
                    if list(response)[x] == wallets[y].address.mainnet.pubaddr1:
                        private = wallets[y].key.mainnet.wif
                        public = wallets[y].address.mainnet.pubaddr1
                        balance = str(list(response.values())[x]["final_balance"])
                        txt = open("wallets.txt", "a")
                        txt.write("Public: " + public + "\n" + "Private: "+private + "\n" + "Balance: " + balance + "\n\n")
                        txt.close()
                        print(f"{pID}.{tID} || Public: "+public)
                        print(f"{pID}.{tID} || Private: "+private)
                        print(f"{pID}.{tID} || Balance: " + balance)
                        sendMessage("",pID,tID,2,{"private":private,"public":public,"balance":balance})
                        exit()

        currentwallets += addressperRequest
        print(f"{pID}.{tID} || Wallets Checked: "+ str(currentwallets))
        if nextMessage <= time.time():
            sendMessage(f"{currentwallets} addresses checked",pID,tID)
            nextMessage = time.time() + messageInterval + pID + tID

def sendMessage(message,pID,tID,type=0,wallet=""):
    webhook = DiscordWebhook(url=DISCORDWEBHOOK,rate_limit_retry=True)
    color = "f2902b"
    title = f"Thread {pID}.{tID} | Status"
    if type==1:
        title = f"Thread {pID}.{tID} | Error"
        color = "ff2121"
    elif type == 2:
        title = f"Thread {pID}.{tID} | Bitcoins FOUND"
        color = "4BB543"
   
    embed = DiscordEmbed(title=message, color=color)
    embed.set_author(name=title)
    embed.set_footer(text='BTCGEN Bot', icon_url='https://m.media-amazon.com/images/I/51O6ByIc8OL._AC_SY450_.jpg')
    embed.set_timestamp()

    if type==2:
        embed.add_embed_field(name='Public', value=wallet["public"])
        embed.add_embed_field(name='Private', value=wallet["private"])
        embed.add_embed_field(name='Balance', value=wallet["balance"])

    webhook.add_embed(embed)

    response = webhook.execute()

def startProcess(pID):
    for x in range(3):
        instance = threading.Thread(target=runInstance, args=(pID,x+1,))
        instance.start()

    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You need to provide how many Process you want to start!!")
        exit()
    for x in range(int(sys.argv[1])):
        instance = Process(target=startProcess, args=(x+1,))
        instance.start()



        