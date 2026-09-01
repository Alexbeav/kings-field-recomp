# King's Field knowledge report

- Date: 2026-09-01
- Retail identity: Japan NTSC-J `SLPS-00017`
- Architecture lane: source-only owned-input setup host
- Release target: Windows x64, version `0.3.4`
- License boundary: portfolio files use GPL-3.0-only; dependencies keep their licenses

## Current state

The operator confirmed gameplay in the private promoted package. This meets
the `bootstrap_verified` boundary. Public setup releases `v0.3.0` and `v0.3.3`
are defective.

GitHub issue 10 supplied the exact Windows message. The setup host requested
`kings_field__Recompiled.exe`. CMake linked
`King_s_Field_Recompiled.exe`. The released ZIP has SHA-256
`ADC8754976C2B0527EA48AE5D531739179B142F8D133A4785616E60DAEEB6003`.

Branch `codex/issue-10-exe-name` aligns the three title-owned names. The
source test passes. A Windows setup-host build also completed 163 of 163
steps and linked the expected executable.

The reporter then confirmed that `v0.3.3` returns to Generate & Build. The
scaffold retained `SLUS_01234` as its generated-source marker, while the
generator emitted `PSX.EXE` sources. CMake therefore linked another setup host.

The `v0.3.4` candidate binds all generated-source paths to `PSX.EXE`. The full
Windows build completed 171 of 171 steps. A hidden startup test reached frame
1,408 with no fatal state.

## Release controls

- Framework target source: afe9ab299aab0eeba1cc31f81bc4baf4e7fb2ab7
- Current framework gitlink: e6d054de1538881cd81dcf3592de1f561afdbb5b
  (CI test registration only)
- recomp-ui: 4eda65430a431e5685ae0c515ebcd912c7843bff
- RetComM Studio: 249422969c1c59ac2a1f8aa2299e876a7133998e
- Distribution: owned input only
- Platform claim: Windows x64 only
- Deferred work: Linux x64, macOS ARM64, and macOS x64 CI jobs

## Open gates

1. Create a new release version. Do not replace `v0.3.3`.
2. Complete setup from the exact corrected ZIP.
3. Make sure that CMake links the generated game sources.
4. Make sure that the automatic relaunch leaves setup mode.
5. Complete an operator gameplay test and a clean exit.
6. Repeat the remote-byte audit and publication authorization.

## Corpus consulted

The release work uses PSX-PUB-004, PSX-PUB-006, PSX-WIN-004,
PSX-WIN-005, PSX-WIN-006, PSX-PUB-011, and PSX-SCAFFOLD-006.

For issue 10, the corpus search included the findings registry, finding
candidates, failure catalog, regression ledger, and portfolio sweep.
`PSX-SCAFFOLD-006` and `FAIL-092` matched the executable-name owner.

The new setup loop also matched the setup-host boundary in `FAIL-079`. No
existing row covered a stale generated-source marker. The result adds
`PSX-SCAFFOLD-007` and `FAIL-101`.

## Reusable regression

`tests/test_setup_exe_name.py` compares the CMake output name, setup-host
forwarding name, and release-packager name. The release workflow runs this
test before it builds any setup host.

`tests/test_generated_source_identity.py` derives the expected output stem from
`game.toml`. It compares the CMake marker, CMake glob, and setup marker with
that stem.

## Quality debt

| Debt | Owner | User impact | Evidence or containment | Removal gate |
|---|---|---|---|---|
| Public `v0.3.0` first-build relaunch | King's Field release | Windows reports that the built executable is missing | Issue 10; run the linked `King_s_Field_Recompiled.exe` directly | Publish a new exact ZIP after the complete release process passes |
| Deferred helper keeps a pre-configure name | psxrecomp setup host | Other renamed titles can fail after a successful build | 22 of 24 Wave 2 sources have static name differences; only King's Field is reproduced | Add a framework regression and derive the helper target from CMake output |
| Public `v0.3.3` links another setup host | King's Field release | The rebuilt executable returns to Generate & Build | Reporter reproduction; CMake uses placeholder `SLUS_01234` while generation emits `PSX.EXE` | Publish a new exact ZIP only after the product-mode and gameplay gates pass |

## Knowledge-base actions

- Updated PSX-SCAFFOLD-006 with the first-build relaunch boundary.
- Added FAIL-098 for the Windows missing-executable message.
- Updated the regression ledger with the King's Field source test.
- Selected a second punctuation-heavy Wave 2 title as the next consumer.

## v0.3.3 setup correction

The source now uses `King_s_Field_Recompiled` as the only setup executable name.
The batch source gate passes.
The exact-ZIP automatic-relaunch canary passes for the corrected source.
The later reporter test proves that this canary was incomplete. Public `v0.3.3`
starts the rebuilt process, but that process is another setup host.

## v0.3.4 generated-source correction

The source replaces `SLUS_01234` with `PSX.EXE` in all generated-source paths.
The source tests pass. The full Windows build compiles the generated game code.
The bounded startup reaches game RAM with no fatal state.
