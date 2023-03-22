from time import sleep

import requests
from web3 import Web3
import configparser
import threading


class Main:
    def __init__(self, choice):
        self.tasks = self.init_wallets()
        self.settings = self.init_settings()
        self.web3 = Web3(Web3.HTTPProvider(self.settings["rpc"]))

        self.contract_claim = self.web3.eth.contract(address=Web3.to_checksum_address("0x67a24CE4321aB3aF51c2D0a4801c3E111D88C9d9"), abi=[{"inputs":[{"internalType":"contract IERC20VotesUpgradeable","name":"_token","type":"address"},{"internalType":"address payable","name":"_sweepReceiver","type":"address"},{"internalType":"address","name":"_owner","type":"address"},{"internalType":"uint256","name":"_claimPeriodStart","type":"uint256"},{"internalType":"uint256","name":"_claimPeriodEnd","type":"uint256"},{"internalType":"address","name":"delegateTo","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"recipient","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"CanClaim","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"recipient","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"HasClaimed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"newSweepReceiver","type":"address"}],"name":"SweepReceiverSet","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Swept","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"recipient","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdrawal","type":"event"},{"inputs":[],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"claimAndDelegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimPeriodEnd","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimPeriodStart","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"claimableTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_recipients","type":"address[]"},{"internalType":"uint256[]","name":"_claimableAmount","type":"uint256[]"}],"name":"setRecipients","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_sweepReceiver","type":"address"}],"name":"setSweepReciever","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"sweep","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"sweepReceiver","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token","outputs":[{"internalType":"contract IERC20VotesUpgradeable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalClaimable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}])
        self.contract_arb = self.web3.eth.contract(address=Web3.to_checksum_address("0x912CE59144191C1204E64559FE8253a0e49E6548"), abi=[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"delegator","type":"address"},{"indexed":True,"internalType":"address","name":"fromDelegate","type":"address"},{"indexed":True,"internalType":"address","name":"toDelegate","type":"address"}],"name":"DelegateChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"delegate","type":"address"},{"indexed":False,"internalType":"uint256","name":"previousBalance","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"newBalance","type":"uint256"}],"name":"DelegateVotesChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"data","type":"bytes"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINT_CAP_DENOMINATOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINT_CAP_NUMERATOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MIN_MINT_INTERVAL","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint32","name":"pos","type":"uint32"}],"name":"checkpoints","outputs":[{"components":[{"internalType":"uint32","name":"fromBlock","type":"uint32"},{"internalType":"uint224","name":"votes","type":"uint224"}],"internalType":"struct ERC20VotesUpgradeable.Checkpoint","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"}],"name":"delegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"delegateBySig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"delegates","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPastTotalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPastVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1TokenAddress","type":"address"},{"internalType":"uint256","name":"_initialSupply","type":"uint256"},{"internalType":"address","name":"_owner","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"l1Address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextMint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"numCheckpoints","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"transferAndCall","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}])
        
        self.starter(choice)

    def starter(self, choice):
        threads = []
        for task in self.tasks:
            if choice == 2:
                t = threading.Thread(target=self.transfer, args=(task,))
            elif choice == 3:
                t = threading.Thread(target=self.claim, args=(task,))
            elif choice == 4:
                t = threading.Thread(target=self.swap, args=(task,))
            elif choice == 5:
                t = threading.Thread(target=self.approve, args=(task,))
            else:
                t = threading.Thread(target=self.run_task, args=(task,))

            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def run_task(self, task):
        self.claim(task)

        if float(task["amount_swap"]) > 0:
            self.swap(task)

        if float(task["amount_transfer"]) > 0:
            self.transfer(task)

    def claim(self, task):
        while True:
            try:
                gas_estimate = self.web3.eth.estimate_gas({"to": self.contract_claim.address, "from": Web3.to_checksum_address(task["address"]), "data": "0x4e71d92d", "value": "0"})
                break
            except Exception as e:
                print(e)

        nonce = self.web3.eth.get_transaction_count(Web3.to_checksum_address(task['address']))

        # NEED MIN 10$ ON THE WALLET
        gas_price = 1000000000

        gas_limit = 1000000
        transaction = self.contract_claim.functions.claim().build_transaction(
            {"maxPriorityFeePerGas": gas_price, "maxFeePerGas": gas_price, "gas": gas_limit, "type": 2, "chainId": 42161, "nonce": nonce}
        )
        signed_tx = self.web3.eth.account.sign_transaction(transaction, task['private_key'])
        print(f"The claim transaction has been sent! Txn Hash: {self.web3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()}")

    def transfer(self, task):
        nonce = self.web3.eth.get_transaction_count(Web3.to_checksum_address(task['address']))

        # NEED MIN 10$ ON THE WALLET
        gas_price = 1000000000

        gas_limit = 1000000
        amount = self.to_decimal(int(task["amount_transfer"]), 18)
        transaction = self.contract_arb.functions.transfer(to=Web3.to_checksum_address(task["transfer_address"]), amount=amount).build_transaction(
            {"maxPriorityFeePerGas": gas_price, "maxFeePerGas": gas_price, "gas": gas_limit, "type": 2, "chainId": 42161, "nonce": nonce}
        )
        signed_tx = self.web3.eth.account.sign_transaction(transaction, task['private_key'])
        print(f"The transfer transaction has been sent! Txn Hash: {self.web3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()}")

    def swap(self, task):
        from_contract_address = "0x912CE59144191C1204E64559FE8253a0e49E6548"  # FROM ARB
        to_contract_address = "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"  # TO USDT (can be changed)
        slippage = int(self.settings['slippage'])
        gas_limit = 11500000
        gas_price = self.web3.eth.gas_price
        amount = self.to_decimal(float(task["amount_swap"]), 18)
        nonce = self.web3.eth.get_transaction_count(Web3.to_checksum_address(task['address']))

        endpoint = f"https://api.1inch.io/v5.0/42161/swap?" \
                   f"fromTokenAddress={from_contract_address}&" \
                   f"toTokenAddress={to_contract_address}&" \
                   f"amount={amount}&" \
                   f"fromAddress={task['address']}&" \
                   f"destReceiver={task['address']}&" \
                   f"slippage={slippage}&" \
                   f"gasPrice={gas_price}&" \
                   f"gasLimit={gas_limit}"

        json_data = self.http_request(endpoint)
        try:
            transaction = json_data['tx']
            transaction['nonce'] = nonce
            transaction['to'] = Web3.to_checksum_address(transaction['to'])
            transaction['gasPrice'] = int(transaction['gasPrice'])
            transaction['value'] = int(transaction['value'])
            signed_tx = self.web3.eth.account.sign_transaction(transaction, task['private_key'])
            print(f"The swap transaction has been sent! Txn Hash: {self.web3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()}")
        except KeyError:
            print(json_data['description'])
            return False

    def approve(self, task):
        nonce = self.web3.eth.get_transaction_count(Web3.to_checksum_address(task['address']))
        gas_price = self.web3.eth.gas_price
        gas_limit = 1000000
        transaction = self.contract_arb.functions.approve(spender=Web3.to_checksum_address("0x1111111254EEB25477B68fb85Ed929f73A960582"), amount=115792089237316195423570985008687907853269984665640564039457584007913129639935).build_transaction(
            {"maxPriorityFeePerGas": gas_price, "maxFeePerGas": gas_price, "gas": gas_limit, "type": 2, "chainId": 42161, "nonce": nonce}
        )
        signed_tx = self.web3.eth.account.sign_transaction(transaction, task['private_key'])
        print(f"The approve transaction has been sent! Txn Hash: {self.web3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()}")

    def http_request(self, url):
        try:
            data = requests.get(url)
        except Exception as e:
            print(e)
            return self.http_request(url)
        try:
            api_data = data.json()
            return api_data
        except Exception as e:
            print(data.text)

    @staticmethod
    def to_decimal(qty, decimal):
        return int(qty * int("".join(["1"] + ["0"] * decimal)))

    @staticmethod
    def init_wallets():
        tasks = []
        with open("wallets.txt", "r+") as file:
            for line in file:
                task = {}
                line_mas = line.split(";")
                task["address"] = line_mas[0]
                task["private_key"] = line_mas[1]
                task["transfer_address"] = line_mas[2]
                task["amount_swap"] = line_mas[3]
                task["amount_transfer"] = line_mas[4].replace('\n', '')

                tasks.append(task)

        return tasks

    @staticmethod
    def init_settings():
        config = configparser.ConfigParser()
        config.read('settings.ini')
        return {"rpc": config['settings']['rpc'], "slippage": config['settings']['slippage']}


print('------ prod By kr1lbo ------')
while True:
    print("--------------------------------------------------------")
    ch = input('1 - Start all\n'
               '2 - Transfer\n'
               '3 - Claim\n'
               '4 - Swap\n'
               '5 - Approve\n'
               'Press "Enter" if you want to exit\n'
               )
    if ch in ["1", "2", "3", "4", "5"]:
        Main(int(ch))
    elif ch == "":
        print("Exit...")
        sleep(1)
        exit()
    else:
        print("kidding?")
