# Development log

## 2026-09-01 — setup executable-name parity

The public `v0.3.0` source used different CMake and setup-relaunch executable
names. The corrected source uses `King_s_Field_Recompiled` in all three title-owned paths.
`Test-SetupExecutableNameParity.ps1` passes. Exact-ZIP automatic relaunch is
confirmed by GitHub Actions run `33497046872` and its clean extraction test.
The package used source commit `726e4f66a0ded60f0985f54d6ea5ee99a9ebed2c`.
This test proves setup behavior. It does not prove gameplay.

## 2026-09-01 — generated-source marker correction

The issue reporter confirmed that `v0.3.3` and the rebuilt executable return to
Generate & Build. The previous canary started the rebuilt process, but it did
not prove that the process contained game code.

The mandatory corpus search covered the findings registry, finding candidates,
failure catalog, regression ledger, and the 2026-08-04 portfolio sweep.
`PSX-SCAFFOLD-006` explained why the earlier gate was incomplete. `FAIL-079`
supplied the setup-host and game-runtime boundary. No existing row covered a
stale generated-source marker.

The web prior-art check found that the upstream
[`GAME_PROJECT_SETUP.md`](https://github.com/mstan/psxrecomp/blob/master/docs/GAME_PROJECT_SETUP.md)
uses `SLUS_01234` as an example marker. The King's Field scaffold never
replaced this token.

The generator emitted these exact files:

- `generated/PSX.EXE_dispatch.c`
- `generated/PSX.EXE_full_00.c`

The source now uses `PSX.EXE` in `GEN_MARKER`, `GEN_FULL_GLOB`, and
`gen_marker_relpath`. `tests/test_generated_source_identity.py` binds these
three values to `[prepare_disc].boot_exe` in `game.toml`.

Both source tests pass. A clean full Windows build completed 171 of 171 steps.
The configure log states `linking generated game C (full runtime)`. The build
compiled both generated game source files and linked
`King_s_Field_Recompiled.exe` with SHA-256
`743B56A95D75D12ED2674314564093DC283F18F0764E7522E5057C8BA8F9B00E`.

A hidden 10-second startup test advanced to frame 1,408. Its terminal heartbeat
recorded PC `0x80035448`, 795,038,575 guest cycles, zero automatic freeze dumps,
and a null fatal state. The process was stopped after the bounded test. This
result proves that the corrected product leaves setup mode. It does not prove
interactive gameplay.

# 2026-09-03 — portable Linux package canary

The exact `v0.3.5` Linux archive built on Ubuntu 24.04 could not start on the
Rocky Linux 9 qualification host. Its setup binary required `GLIBC_2.35` and
`GLIBC_2.38`. The host supplies glibc 2.34.

The contained correction pins the Linux job to an exact Ubuntu 20.04 container
with glibc 2.31. It pins and verifies the two Focal Vulkan build-tool packages.
The archive gate checks the setup host and both packaged emitters. It rejects a
required glibc symbol newer than 2.31. Windows and macOS jobs keep their
existing hosts.

The first contained run stopped in a title identity test because Ubuntu 20.04
uses Python 3.8, which predates the standard `tomllib` module. The replacement
workflow pins the `tomli` backport for that test only. No build or package step
ran in the stopped attempt.

The second contained run passed the identity test. The Linux dependency step
then waited for an interactive time-zone selection while it configured
`tzdata`. The next replacement keeps package installation non-interactive and
sets `TZ=Etc/UTC`. The stopped Linux job did not reach a build or package step.
