# ECDSA Implementation

## Overview
This project implements the **Elliptic Curve Digital Signature Algorithm (ECDSA)** using the **secp256k1** curve. The implementation includes key generation, message signing, and signature verification. The program operates through command-line parameters, following a structured input/output format.

## Features
- **User ID Retrieval** (`userid` mode)
- **Key Generation** (`genkey` mode)
- **Message Signing** (`sign` mode)
- **Signature Verification** (`verify` mode)

## Requirements
- The implementation exclusively uses the **secp256k1** curve, with fixed parameters:
  - \( a = 0 \)
  - \( b = 7 \)
- All input and output values are **non-negative base-10 integers**.
- The prime modulus \( p \) and curve order \( o \) are guaranteed to be **prime numbers**.
- No error checking is required for input parameters.

## Usage

### 1. User ID Retrieval (`userid`)
Prints the user ID of the implementer.

#### Example:
```sh
$ ./ecdsa.sh userid
mst3k
```

### 2. Key Generation (`genkey`)
Generates a **random private key** and computes the corresponding **public key**.

#### Input:
```sh
$ ./ecdsa.sh genkey p o Gx Gy
```

#### Where:
```sh
p = Prime modulus
o = Curve order
Gx, Gy = Base point coordinates
```

#### Example:
```sh
$ ./ecdsa.sh genkey 43 31 25 25
16
37
36
```
### 3. Message Signing (sign)
Signs a **message hash** using the **private key**.

#### Input:
```sh
$ ./ecdsa.sh sign p o Gx Gy d h
```

#### Where:
```sh
p, o, Gx, Gy = Standard curve parameters
d = Private key
h = Hash of the message (precomputed integer)
```

#### Example:
```sh
$ ./ecdsa.sh sign 43 31 25 25 16 30
12
24
```

### 4. Signature Verification (verify)
Verifies if a given **signature** is valid for a **message hash**.

#### Where:

```sh
p, o, Gx, Gy = Standard curve parameters
Qx, Qy = Public key coordinates
r, s = Signature values
h = Hash of the message
Example (Valid Signature):
```

#### Example:

```sh
$ ./ecdsa.sh verify 43 31 25 25 37 36 12 24 30
True
```

#### Example (Invalid Signature):
```sh
$ ./ecdsa.sh verify 43 31 25 25 37 36 12 24 29
False
```
