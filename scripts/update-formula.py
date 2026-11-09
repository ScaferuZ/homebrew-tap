#!/usr/bin/env python3
"""Regenerate Formula/tfw.rb from the latest ScaferuZ/tfw GitHub release.

Runs inside the tap repository's GitHub Action (or by hand) and needs no
secrets for a public upstream: the release metadata and SHASUMS256.txt are
public. Exits non-zero only on a real failure; "nothing to do" is exit 0.
"""

from __future__ import annotations

import json
import os
import pathlib
import sys
import urllib.request

UPSTREAM = "ScaferuZ/tfw"
FORMULA = pathlib.Path(__file__).resolve().parent.parent / "Formula" / "tfw.rb"

TEMPLATE = """\
class Tfw < Formula
  desc "Guardrail for terraform plan/apply: forces 'destroy' instead of 'yes' on destructive plans"
  homepage "https://github.com/{upstream}"
  version "{version}"
  license "MIT"

  livecheck do
    url :homepage
    strategy :github_latest
  end

  on_macos do
    on_arm do
      url "https://github.com/{upstream}/releases/download/v#{{version}}/tfw_darwin_arm64.tar.gz"
      sha256 "{darwin_arm64}"
    end

    on_intel do
      url "https://github.com/{upstream}/releases/download/v#{{version}}/tfw_darwin_amd64.tar.gz"
      sha256 "{darwin_amd64}"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/{upstream}/releases/download/v#{{version}}/tfw_linux_arm64.tar.gz"
      sha256 "{linux_arm64}"
    end

    on_intel do
      url "https://github.com/{upstream}/releases/download/v#{{version}}/tfw_linux_amd64.tar.gz"
      sha256 "{linux_amd64}"
    end
  end

  def install
    bin.install "tfw"
  end

  test do
    assert_match "tfw #{{version}}", shell_output("#{{bin}}/tfw version")
    assert_match "tfw plan", shell_output("#{{bin}}/tfw help 2>&1")
  end
end
"""

PLATFORMS = ("darwin_amd64", "darwin_arm64", "linux_amd64", "linux_arm64")


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def main() -> int:
    release = json.loads(get(f"https://api.github.com/repos/{UPSTREAM}/releases/latest"))
    tag = release["tag_name"].lstrip("v")
    assets = {a["name"]: a["browser_download_url"] for a in release.get("assets", [])}

    sums_url = assets.get("SHASUMS256.txt")
    if not sums_url:
        print(f"{UPSTREAM} {release['tag_name']} has no SHASUMS256.txt asset", file=sys.stderr)
        return 1

    sums = {}
    for line in get(sums_url).decode().splitlines():
        parts = line.split()
        if len(parts) == 2:
            sums[parts[1]] = parts[0]

    missing = [f"tfw_{p}.tar.gz" for p in PLATFORMS if f"tfw_{p}.tar.gz" not in sums]
    if missing:
        print(f"release {release['tag_name']} is missing checksums for: {', '.join(missing)}", file=sys.stderr)
        return 1

    rendered = TEMPLATE.format(
        upstream=UPSTREAM,
        version=tag,
        **{p: sums[f"tfw_{p}.tar.gz"] for p in PLATFORMS},
    )

    if FORMULA.exists() and FORMULA.read_text() == rendered:
        print(f"formula already at {tag}")
        return 0

    FORMULA.parent.mkdir(parents=True, exist_ok=True)
    FORMULA.write_text(rendered)
    print(f"formula updated to {tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
