# JWT Authentication Attack & Secure Fix Lab

## Overview
This project demonstrates how **improper JWT validation** can lead to authentication bypass and privilege escalation.

It shows both:
- How attackers exploit JWT implementation flaws
- How secure validation prevents these attacks

The lab is designed from an **attacker-to-defender** perspective.

---

## Problem Statement
Many applications implement JWT-based authentication without fully understanding:
- Signature verification
- Algorithm enforcement
- Token trust boundaries

This often results in critical authentication vulnerabilities.

---

## What This Project Does
- Implements a vulnerable JWT authentication flow
- Exploits the `alg:none` vulnerability to gain admin access
- Demonstrates a secure implementation with proper validation

---

## Attack Scenario
1. Application disables JWT signature verification
2. Attacker forges a JWT token with elevated privileges
3. Application trusts the token without verification
4. Unauthorized admin access is granted

---

## Secure Fix
- Enforced algorithm validation
- Enabled signature verification
- Proper error handling for invalid tokens

---

## Security Concepts Covered
- JWT internals
- Authentication vs authorization
- Token trust boundaries
- Secure implementation practices

---

## Tech Stack
- Python
- Flask
- JSON Web Tokens (JWT)

---

## Why This Matters
JWT vulnerabilities directly lead to:
- Account takeover
- Privilege escalation
- Full application compromise

This project reflects real-world AppSec issues seen in production systems.

---

## Disclaimer
This lab is for educational and defensive security research only.
