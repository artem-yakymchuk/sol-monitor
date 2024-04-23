
# Solana New Block Checker

This script is designed to monitor new blocks on the Solana blockchain and to search for new cryptocurrency tokens being created. It utilizes the Solana JSON RPC API to fetch the latest confirmed block and checks for transactions that might indicate the creation of new tokens.

## Features

- Fetch the latest finalized block from the Solana blockchain.
- Analyze transactions within these blocks to identify potential new token creations.
- Run continuously, checking for new blocks every minute.

## Prerequisites

Before you can run the script, you will need to have Python installed on your machine along with the following Python libraries:
- `requests`: For making HTTP requests to the Solana JSON RPC API.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://your-repository-url.git
   cd solana-block-checker
   ```

2. **Install required libraries:**
   If you haven't already installed the required Python libraries, you can install them using pip:
   ```bash
   pip install requests
   ```

## Usage

To start the script, navigate to the script's directory and run:
```bash
python solana_block_checker.py
```
The script will continuously check for new blocks every minute and print out details of new tokens if any are found.

## Configuration

No additional configuration is needed to start using this script. However, depending on your use case, you might want to modify the script to handle different aspects of block data or to interact with other functionalities of the Solana API.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests.
