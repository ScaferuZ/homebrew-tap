# homebrew-tap

Homebrew tap for [ScaferuZ/tfw](https://github.com/ScaferuZ/tfw) — a guardrail for
`terraform plan` / `terraform apply` that makes destroys impossible to miss.

## Install

```sh
brew install ScaferuZ/tap/tfw
```

That fully-qualified name is the recommended form: recent Homebrew versions
trust a tap **per item**, and naming the formula explicitly is what grants that
trust. It works without a separate `brew tap` step.

If you prefer the short name, tap and trust first:

```sh
brew tap ScaferuZ/tap
brew trust --formula ScaferuZ/tap/tfw
brew install tfw
```

Upgrade:

```sh
brew upgrade tfw
```

## Platforms

macOS and Linux, Intel and Apple Silicon. Windows: use the `.zip` from
[tfw releases](https://github.com/ScaferuZ/tfw/releases).

## How this tap stays current

`Formula/tfw.rb` installs the prebuilt binary from the upstream release (no
compiler needed) and is regenerated from the latest upstream release by
`.github/workflows/update.yml` — daily, plus manual dispatch — including the
`sha256` for every platform. The generator is `scripts/update-formula.py` and
needs no secrets (public upstream); run it locally with `python3
scripts/update-formula.py`.

`brew livecheck tfw` reads the upstream GitHub releases, so a version bump shows
up before the formula is regenerated.
