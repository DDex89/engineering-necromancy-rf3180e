# Publication and responsible disclosure boundaries

This repository intentionally documents an engineering recovery **without distributing sensitive or proprietary device-derived material**.

## Never upload here

- Production NAND dump images, raw/OOB pages, bad-block tables or extracted partitions.
- Vendor firmware packages, decrypted binaries, original reconstruction scripts with embedded page data, or vendor certificates and cryptographic material.
- Serial numbers, switch management addresses, MAC addresses, real customer/site identifiers, network layouts or internal screenshots.
- Passwords, account databases, hash files, authentication material, recovery tokens, or scripts for privilege changes.
- Live device logs not individually reviewed for secrets and sensitive identifiers.
- Any documents or backups belonging to an employer, customer or other third party without authorization.

## Before publication

1. Open every file to confirm that only intentionally authored, sanitized material is present.
2. Review `git status --short` and the exact diff of the intended commit.
3. Check for sensitive data and device-derived payloads; `.gitignore` only reduces mistakes and is **not** a security boundary.
4. Obtain any necessary authorization before publishing work derived from proprietary equipment or workplace data.
5. If sensitive content has *ever* been committed, removing it in the newest commit does **not** remove it from Git history. Rotate leaked credentials and rewrite history appropriately before publishing.

## Scope

The repository contains a retrospective, non-sensitive engineering case study and a generic read-only binary comparison demonstration. It does not attempt to bypass equipment authentication, defeat firmware-signing controls, disclose vulnerabilities or offer instructions for modifying someone else's network device.
