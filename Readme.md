# 0g3: The Decentralized Programming Language

## Overview

0g3 is an innovative programming language designed to facilitate the creation of decentralized applications (DApps) without the need for additional contracts. By leveraging blockchain technology, 0g3 stores all proof of work directly within the blockchain, ensuring true decentralization and eliminating the complexities associated with contract management.

## Features

### Decentralization

- **Proof of Work on Blockchain**: 0g3 stores all proof of work directly within the blockchain, ensuring transparency, security, and true decentralization of applications built using the language.

### Native Language Support

- **English, Tamil, and Hindi**: 0g3 supports three native languages - English, Tamil, and Hindi, making it accessible to developers and users from diverse linguistic backgrounds.

### Seamless Transactions

- **Smooth Transaction Processing**: 0g3 ensures smooth and efficient transaction processing on the blockchain, leading to minimal disruptions and delays in the execution of decentralized applications.

### Simplified Development

- **Elimination of Additional Contracts**: With 0g3, developers can build decentralized applications without the need for additional contracts, simplifying the development process and reducing overhead.

### Smart Contract Integration

- **Seamless Integration with Smart Contracts**: 0g3 seamlessly integrates with existing smart contracts, allowing developers to leverage the full power of blockchain technology in their applications.

### Enhanced Security

- **Robust Security Measures**: 0g3 incorporates robust security measures to protect against malicious attacks and unauthorized access, ensuring the integrity and safety of decentralized applications.

## Benefits

### True Decentralization

0g3 promotes true decentralization by storing all proof of work within the blockchain, ensuring that applications built using the language are not subject to centralized control or manipulation.

### Enhanced Efficiency

By eliminating the need for additional contracts, 0g3 streamlines the development process and improves the efficiency of decentralized application development.

### Improved User Experience

With seamless transaction processing and native language support, 0g3 offers an improved user experience for both developers and end-users, leading to greater adoption of decentralized applications.

## Getting Started

### Installation

Install the 0g3 compiler and set up your development environment. Detailed installation instructions are available in the documentation.

## Additional Features of 0g3

- **Onchain Execution**: Code executed in 0g3 runs directly on the blockchain, providing true onchain execution.
- **Batch Transaction Execution**: Utilizes batch transaction execution for efficiency.
- **Code Backtracking**: Easily backtrack the code to debug and analyze.
- **Ownership Management**: Each process is owned by the owner, ensuring security and accountability.
- **Language Flexibility**: If you know 0g3, you can deploy it anywhere without learning another contract language. Convert 0g3 to any contract language like Move, Solidity, or Rust easily.
- **Self Deployment**: Code can self-deploy on the blockchain.
- **Python Integration**: Built on Python, enabling easy access to Python's features.
- **Multi-Chain Support**: Supports multiple blockchain networks.
- **Pure Decentralized Onchain Execution**: Created for pure decentralized onchain execution, allowing easy debugging and testing with AI.

## 0g3 Editor

### Overview

The 0g3 editor is a web-based text editor powered by AI. It allows developers to ask questions, get documentation, and receive code modifications or corrections through an AI chatbot.

### Features

- **AI-Powered Assistance**: Use AI to improve, explain, and generate code.
- **Code Runner and Debugger**: Integrated tools for running and debugging code.
- **Documentation Creation**: Generate documentation within the editor.
- **Chrome Extension**: Use the editor as a Chrome extension.
- **Move Language Training**: The AI is specifically trained for the Move language.
- **Code Conversion**: Convert pseudocode in languages like Python, JS, and C to Move, Rust, or Solidity.

### Usage

- **Upload Files**: Upload files to the editor and edit as needed.
- **AI Features**: Use Ctrl + K for AI features if code is selected, otherwise, AI will respond to general queries.

## Code Convertor

The code convertor tool provides conversion from any language to Move, Solidity, and Rust, primarily focused on Move.

## Scanner

### Overview

The 0g3 scanner is akin to Polygon and Ethereum scanners, allowing you to track and scan transaction data.

### Features

- **Data Tracking**: Monitor and track transaction data effectively.
- **Security**: Ensure secure and transparent tracking of blockchain transactions.

## API Documentation

### Endpoints

- **Generate Code**
    `path("generate_code", generate_solidity_code, name="generate_solidity_code")` 
    
- **Compile**
    
    `path("compile", compile, name="compile")` 
    
- **Scan**
    
    `path("scan", scan, name="scan")` 
    

### Usage Examples

#### JavaScript


```javascript // Generate Code Example
fetch('https://api.yourdomain.com/generate_code', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    sourceCode: 'your_source_code_here'
  })
})
.then(response => response.json())
.then(data => console.log(data));

// Compile Example
fetch('https://api.yourdomain.com/compile', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    sourceCode: 'your_source_code_here'
  })
})
.then(response => response.json())
.then(data => console.log(data));

// Scan Example
fetch('https://api.yourdomain.com/scan', {
  method: 'GET',
})
.then(response => response.json())
.then(data => console.log(data));
```


#### Python

```python import requests

# Generate Code Example
response = requests.post(
    'https://api.yourdomain.com/generate_code',
    json={'sourceCode': 'your_source_code_here'}
)
print(response.json())

# Compile Example
response = requests.post(
    'https://api.yourdomain.com/compile',
    json={'sourceCode': 'your_source_code_here'}
)
print(response.json())

# Scan Example
response = requests.get('https://api.yourdomain.com/scan')
print(response.json())
```

## Documentation

For more details, check out the [official blog](https://nagis-organization.gitbook.io/0g3/).