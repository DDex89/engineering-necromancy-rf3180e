# Technical findings (sanitized)

## Platform characteristics observed

| Subsystem | Observed |
| --- | --- |
| CPU | Freescale P1020E (PowerPC) |
| RAM | 1 GiB DDR3 |
| Flash | 512 MiB NAND |
| Bootloader | U-Boot 2010.12 |
| OS / services | Embedded Linux, maintenance shell, application services |
| Persistent filesystem | UBI / UBIFS |
| Firmware generation | 4.5.06.04 |

The storage map contained a bootloader partition, two firmware banks, and a larger UBI/UBIFS filesystem partition. Precise operational offsets and access-related metadata are withheld to prevent the case study being mistaken for a universal flashing recipe.

## Four independent failure and validation layers

**NAND / ECC.** Uncorrectable reads were a direct physical-data integrity signal, not just an application complaint. Recovery candidates were assessed using the relevant NAND controller ECC information.

**UBI / UBIFS.** Filesystem structures yielded an additional layer of integrity validation: recognized UBIFS nodes had CRC fields that could be checked independently of the NAND ECC result. The accepted reconstruction passed the available UBIFS-node checks.

**Application archive.** The boot sequence reported firmware package verification/decryption failures. The recovered stored archive was checked for its expected structure. A message about a failed decryption stage should not be taken as proof that cryptographic keys were invalid.

**Runtime verification.** Restored boot and application service startup provided a higher-level functional check. The result is stronger than a matching checksum by itself, though weaker than full network/load/endurance certification.

## What the four-bit statement means

Four erroneous data bits were repaired in two damaged 512-byte sectors as part of recovering material essential to the stored firmware archive. This is an **observed correction count for this incident**, not a universal prediction about similar products, storage wear, or NAND capabilities.

## Evidence handling rules

- Keep failure-state flash captures immutable and separate from corrected reference images.
- Do not publish embedded vendor images, device credentials, encrypted configuration or cryptographic key material.
- A post-repair image is **device-specific** and is not a generalized factory image.
- Do not treat the presence of a running CLI as proof that every physical Ethernet port has passed qualification.

## Deliberate omissions

No original page/OOB dumps, bad-sector locations, binary patch material, credentials, certificate contents, vendor-specific extraction scripts or maintenance entry procedures are included. These details are unnecessary to communicate the engineering findings.
