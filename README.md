# homebrew-tap

Homebrew tap for [ScaferuZ/tfw](https://github.com/ScaferuZ/tfw) — a guardrail for
`terraform plan` / `terraform apply` that makes destroys impossible to miss.

```sh
brew tap ScaferuZ/tap
brew install tfw
```

Or in one shot, fully qualified (this is the form Homebrew trusts per item):

```sh
brew install ScaferuZ/tap/tfw
```

Upgrade:

```sh
brew upgrade tfw
```

## Platforms

macOS and Linux, Intel and Apple Silicon. Windows: use the `.zip` from
[tfw releases](https://github.com/ScaferuZ/tfw/releases).

The formula installs the prebuilt binary from the upstream release (no compiler
needed). `Formula/tfw.rb` is regenerated from the latest upstream release by
`.github/workflows/update.yml` (daily + manual dispatch), including the
`sha256` for every platform.
