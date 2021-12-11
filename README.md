<img src="https://i.imgur.com/3EbO1np.png" alt="icon" width="256" hight="256"/>


# BTCFucker

BTCFucker is a bitcoin-address generator which tries to generate a wallet which contains bitcoins

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirement frameworks.

```bash
pip install -r requirements.txt
```
## Settings
1. Change the ```log```,```error```,```success``` to your **Discord-WebHook-Link**
2. You can change ```logColor```,```errorColor```,```sucessColor``` to your preferred color 
3. ```addressperRequest``` = How many addresses you want to check per API-Call (**You will get an error from the Blockchain API if you set the ```addressperRequest``` higher than 140**)
4. ```messageInterval``` = changes the interval of the status messages (standard is 120sec = 2min)

```json
{
    "log":"Enter Discord Webhook",
    "error":"Enter Discord-Webhook",
    "success":"Enter Discord-Webhook",
    "logColor":"f2902b",
    "errorColor":"ff2121",
    "sucessColor":"4BB543",
    "addressperRequest":140,
    "messageInterval":120
}
```
## Usage
Just run ```btcfucker.py <number of processes>```

**The Bot uses Multiprocessing to use "all" CPU cores**
## Status
![](https://i.imgur.com/zLuK5Ab.png)

## Error
![](https://i.imgur.com/M1sSulC.png)

## Bitcoin-Address with Bitcoins found
![](https://i.imgur.com/G8a7KFW.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)