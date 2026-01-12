\# JWT Authentication Attack \& Secure Fix Lab



\## Overview

This lab demonstrates how insecure JWT validation can lead to authentication bypass.



\## Vulnerability

\- Signature verification disabled

\- alg:none attack possible



\## Exploit

An attacker can forge a JWT token with admin privileges.



\## Fix

\- Enforced algorithm validation

\- Signature verification enabled



\## Tech Stack

\- Python

\- Flask

\- JWT



\## Learning Outcome

Understanding JWT internals from an attacker and defender perspective.



