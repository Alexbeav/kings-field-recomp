# Development log

## 2026-09-01 — setup executable-name parity

The public `v0.3.0` source used different CMake and setup-relaunch executable
names. The corrected source uses `King_s_Field_Recompiled` in all three title-owned paths.
`Test-SetupExecutableNameParity.ps1` passes. Exact-ZIP automatic relaunch is
confirmed by GitHub Actions run `33497046872` and its clean extraction test.
The package used source commit `726e4f66a0ded60f0985f54d6ea5ee99a9ebed2c`.
This test proves setup behavior. It does not prove gameplay.
