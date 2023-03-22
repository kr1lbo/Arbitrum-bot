# Arbitrum bot
____
## Features
* Working with multiple wallets.
* Claim arb tokens.
* Approve access to dex 1inch tokens.
* Transfer a certain number of tokens to the wallet.
* Exchange a certain number of tokens for another currency on dex 1inch.
* You can separately launch a claim, send or exchange.

# Warning!
### **It is advisable to have at least $15 in ETH in the Arbitrum network.**

## Configuration
> In the settings.ini file, you can set your own rpc and the desired slippage for exchange.

> To a file wallets.txt we record data about wallets. An example of its filling is in wallets_example.txt.
> > In amountSwap and amountTransfer, we record the number of tokens in the ether format (integers of tokens).
> 
> > `amountSwap` and `amountTransfer` can be equal to 0. In this case, the execution of the function will be skipped.
> > _<br>You can set the `amountSwap` -> 0 and `amountTransfer` -> 0 and then only claim will be executed._

## The sequence of actions.
1. Download the files, put them in a separate folder.
2. Open this folder in the console and run the command `pip install -r requirements.txt`
3. Open File wallets.txt and fill it out with an example wallets_example.txt.
4. Open the settings.ini file, specify your rpc and optionally change the slippage.
5. If you are going to use the swap. Then you need to approve the token in advance.
6. Start the program and press the number `1` and `Enter` some time before the claim, thereby starting the program.

## LINKS
Claim contract: https://arbiscan.io/address/0x67a24CE4321aB3aF51c2D0a4801c3E111D88C9d9

$ARB contract: https://arbiscan.io/address/0x912CE59144191C1204E64559FE8253a0e49E6548

1inch contract: https://arbiscan.io/address/0x1111111254eeb25477b68fb85ed929f73a960582

### Credits and donations
Script was created by kr1lbo specifically for https://t.me/alliancealfa.

If you want to donate:

Address: `0xEEA680953D3eA76b47E9d7ba4a417dcA4C7529f9` (any token, all chains)