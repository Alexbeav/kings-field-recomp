# King's Field release feasibility

Status: `bootstrap_verified`; public `v0.3.0` has a first-build relaunch defect

The operator confirmed that the promoted private build reaches gameplay. This
meets the `bootstrap_verified` boundary. The source-only Windows package
builds locally. It must still pass exact-package setup, startup, and remote-byte
gates before public release.

The supported serial set is `SLPS-00017`. The package uses
the owned-input distribution model. The player supplies the supported disc set
and BIOS, and the setup host builds the playable executable locally.

The public `v0.3.0` setup host can build the game, but its first relaunch asks
Windows for the wrong executable name. Issue 10 confirms this defect. The
corrected source uses `King_s_Field_Recompiled` for CMake, the setup host, and
the release packager. A new version must repeat the complete release process.

The package must not contain a disc, retail BIOS, generated retail code, save,
capture, prebuilt playable executable, or private absolute path.
