# King's Field release feasibility

Status: `bootstrap_verified`; public `v0.3.0` and `v0.3.3` setup releases are defective

The operator confirmed that the promoted private build reaches gameplay. This
meets the `bootstrap_verified` boundary. The source-only Windows package
builds locally. It must still pass exact-package setup, startup, and remote-byte
gates before public release.

The supported serial set is `SLPS-00017`. The package uses
the owned-input distribution model. The player supplies the supported disc set
and BIOS, and the setup host builds the playable executable locally.

The public `v0.3.0` setup host can build the game, but its first relaunch asks
Windows for the wrong executable name. Issue 10 confirms this defect.

Public `v0.3.3` corrects that name. It still uses the scaffold generated-source
marker `SLUS_01234`. The generator creates `PSX.EXE` sources. CMake therefore
links another setup host, and the rebuilt executable returns to Generate &
Build.

The package must not contain a disc, retail BIOS, generated retail code, save,
capture, prebuilt playable executable, or private absolute path.

## v0.3.3 executable-name correction

Public `v0.3.0` can complete a build and then request the wrong executable.
The corrected source uses `King_s_Field_Recompiled` in all owned name fields.
The 24-title source parity gate passes.
The exact-ZIP automatic-relaunch canary also passes.

This canary proved process startup only. It did not prove that CMake linked the
generated game sources.

## v0.3.4 generated-source correction

The candidate uses `PSX.EXE` for the CMake marker, full-source glob, and setup
marker. The source identity tests pass. The full Windows build completed 171 of
171 steps and compiled both generated game source files.

A hidden startup test advanced to frame 1,408. The terminal heartbeat recorded
PC `0x80035448`, 795,038,575 guest cycles, and no fatal state. This is startup
evidence. It does not replace the operator gameplay gate or exact-package gate.
