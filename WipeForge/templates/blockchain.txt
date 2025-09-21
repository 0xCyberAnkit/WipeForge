# blockchain_simulation.py - A simplified simulation of a blockchain for immutable wipe logs.

import hashlib
import json
import datetime

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the cryptographic hash of the block's contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    Manages the chain of blocks.
    """
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (the genesis block).
        """
        self.chain.append(Block(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Genesis Block", "0"))

    def get_latest_block(self):
        """
        Returns the most recently added block.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the chain after linking it to the previous one.
        
        Args:
            new_block (Block): The new block to be added.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Checks if the entire chain is valid by verifying all hashes.
        
        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                print("Blockchain invalid: Current block's hash is not correct.")
                return False

            if current_block.previous_hash != previous_block.hash:
                print("Blockchain invalid: Previous block's hash does not match.")
                return False

        return True

# --- Example Usage ---
if __name__ == "__main__":
    wipeforge_blockchain = Blockchain()

    print("Creating the WipeForge blockchain...")
    print(f"Genesis Block hash: {wipeforge_blockchain.get_latest_block().hash}")

    # Simulate adding a wipe log to the blockchain
    print("\nAdding a simulated wipe log for Dell Laptop...")
    wipe_log_data_1 = {
        "log_id": "log_1A2B-3C4D-5E6F",
        "device_id": "1A2B-3C4D-5E6F",
        "wiping_method": "Gutmann Method",
        "status": "Wipe Successful",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    wipeforge_blockchain.add_block(Block(1, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), wipe_log_data_1, ""))

    # Simulate adding another wipe log
    print("Adding another simulated wipe log for Server RAID Array...")
    wipe_log_data_2 = {
        "log_id": "log_7G8H-9I0J-1K2L",
        "device_id": "7G8H-9I0J-1K2L",
        "wiping_method": "DoD 5220.22-M",
        "status": "Wipe Successful",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    wipeforge_blockchain.add_block(Block(2, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), wipe_log_data_2, ""))

    # Print the chain to see the hashes
    print("\nBlockchain created successfully:")
    for block in wipeforge_blockchain.chain:
        print(f"Block #{block.index}")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Data: {block.data}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Current Hash: {block.hash}\n")

    # Verify the integrity of the chain
    print("Verifying the integrity of the chain...")
    if wipeforge_blockchain.is_chain_valid():
        print("The blockchain is valid and secure.")
    else:
        print("The blockchain has been tampered with!")

    # Simulate an attack by tampering with a block
    print("\n--- Simulating a malicious attack on Block #1 ---")
    wipeforge_blockchain.chain[1].data["status"] = "Wipe Failed"
    wipeforge_blockchain.chain[1].hash = wipeforge_blockchain.chain[1].calculate_hash() # The hash of block 1 changes

    print("Re-verifying the integrity of the chain...")
    if wipeforge_blockchain.is_chain_valid():
        print("The blockchain is still valid. (This should not happen!)")
    else:
        print("The blockchain is invalid! Attack detected.")
