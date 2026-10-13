# Case study — from boot loop to operational system

## 1. The initial fault

The industrial Ethernet switch was received in a state where its application did not start. The RUN status was absent, expected network link activity did not appear at the outset, and the normal startup sequence fell into a loop. The bootloader and parts of embedded Linux, however, were still functional.

Serial diagnostics identified repeated uncorrectable NAND reads (`EBADMSG`, `-74`) coinciding with failures to verify/load a versioned application package. The device was not simply missing its bootloader: the failure occurred further along the boot chain.

## 2. Defining the boundary

Before touching the flash, the investigation separated the following layers:

| Layer | What was established |
| --- | --- |
| Processor / boot ROM | The system executed U-Boot reliably enough for diagnostics |
| Bootloader / kernel | The maintenance Linux environment remained reachable |
| Flash access | NAND reads had repeatable ECC failures in specific data regions |
| UBI/UBIFS | Flash-resident application data could be inspected, although damaged content was present |
| Application-package verification | Startup could not use the stored package; error text mentioned verification/decryption |
| Network hardware | Some link behavior was absent independently of the failed startup; later port qualification remained open |

This prevented a decryption error message from being misinterpreted as proof of a bad encryption key or broken cryptographic design.

## 3. Preserving evidence

The original NAND-derived material was treated as forensic input, not as a writable work file. Candidate reconstructions were created separately. The investigation did not depend on wiping all UBI data, replacing the bootloader, or blindly flashing a complete image.

The source data included flash-page evidence with out-of-band (OOB) error-correction information; the full proprietary raw data is intentionally excluded from this public repository.

## 4. Offline reconstruction

A local analysis utility reconstructed a candidate data image from the available readable NAND content and independently captured page evidence. The accepted repairs were limited to ECC-consistent sectors.

Two damaged **512-byte sectors** were successfully recovered. Across the relevant contents, **four data-bit errors** were corrected. This was a tiny numerical change with a large system-level consequence.

The candidate was not trusted solely because it looked reasonable. It was cross-checked against **the NAND controller's ECC relationship, UBIFS node CRCs, and the expected firmware-package structure**. Checks that failed or could not be independently established were treated as unresolved rather than silently accepted.

## 5. Minimal intervention

Once the required stored data could be reconstructed and verified offline, the affected application archive was replaced on the target under controlled conditions. The broader operating-system storage, bootloader, and device-specific configuration were not indiscriminately overwritten.

Exact maintenance commands, access details, device-specific addresses, and proprietary package material have been omitted intentionally.

## 6. Observed recovery

Following restart, the device progressed beyond its previous failure point. Startup logs showed the management and supporting services initializing. RUN status illuminated, optical status activity changed, LAN negotiation was observed, and management/CLI functions could be reached.

This established **successful boot recovery**. It did not establish complete hardware health or full production-network readiness.

## 7. Backup and verification

After the successful boot, all four NAND partitions were saved in two formats: a data-area representation and a physical/raw representation including OOB information. The eight files were checked by their recorded checksums. Original failure-state evidence was retained separately from the post-recovery reference images.

A raw+OOB archive is **not a drop-in firmware update** and is not intended to be transferred to another device.

## 8. Lessons learned

- An error near a cryptographic verification stage may originate in bad flash reads several layers below it.
- When dealing with NAND, physical storage details and filesystem integrity checks complement each other.
- Cross-checking independent error detectors is stronger than accepting a single promising hypothesis.
- Minimal repairs are safer than broad flash erases when the remaining system is working.
- A system that boots successfully may still have unrelated hardware faults or aging media.
- Reproducibility depends as much on what is **not** changed as on what is repaired.
