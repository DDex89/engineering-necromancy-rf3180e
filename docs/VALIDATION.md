# Validation matrix and open questions

| Check | Observed result | Interpretation |
| --- | --- | --- |
| Bootloader responds | Yes | Early boot path remained available |
| Maintenance Linux accessible | Yes | OS diagnostics possible independently of normal application boot |
| NAND ECC errors before repair | Reproducible | Supported hypothesis of stored data corruption |
| Candidate sector reconstruction | Two sectors, four corrected bits | Offline recovery targeted the damaged data |
| ECC relationship | Consistent for accepted repair | One independent correctness constraint |
| UBIFS node checksums | Passed on the recovered candidate | Second integrity constraint |
| Application startup after replacement | Passed observed boot sequence | Core recovery outcome |
| RUN indicator | Illuminated | Device application/system reached running state |
| Management and CLI services | Became available | Runtime functionality recovered |
| NAND archives | 4 partitions × 2 representations | Backup coverage |
| Backup-file checksum audit | 8/8 passed | Transfer/file integrity verified at audit time |
| Full VLAN/SFP/port matrix | Not established | Requires separate functional test |
| Long-duration NAND endurance | Not established | Future flash wear remains possible |
| Previously non-linking physical ports | Suspected separate hardware issue | Not claimed as fixed |

## Boundaries of the claim

**Recovered** means that the device resumed its expected OS/application boot and essential management functions following a minimally invasive data correction.

It does **not** mean factory requalification, a hardware guarantee, permanently healthy flash, comprehensive Ethernet testing, or authorization to duplicate a device's stored identity and configuration onto another unit.

## Suggested future non-destructive qualification

A later lab qualification could document link state per physical port, interface statistics and error rates, SFP behavior with known-good modules, VLAN management reachability, and observation across restarts. These tests are **not recorded as completed** in this publication.
