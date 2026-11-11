class Tfw < Formula
  desc "Guardrail for terraform plan/apply: forces 'destroy' instead of 'yes' on destructive plans"
  homepage "https://github.com/ScaferuZ/tfw"
  version "0.3.0"
  license "MIT"

  livecheck do
    url :homepage
    strategy :github_latest
  end

  on_macos do
    on_arm do
      url "https://github.com/ScaferuZ/tfw/releases/download/v#{version}/tfw_darwin_arm64.tar.gz"
      sha256 "b8b2f80fd64a539953f4a1a4279e95cda31ffd547c4996c6e87e7da1e19b5ab3"
    end

    on_intel do
      url "https://github.com/ScaferuZ/tfw/releases/download/v#{version}/tfw_darwin_amd64.tar.gz"
      sha256 "87a7f8c53bad018c63291ce9142e2ad604c5ef8d68e3274a0bcbbc1cbbd08d65"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/ScaferuZ/tfw/releases/download/v#{version}/tfw_linux_arm64.tar.gz"
      sha256 "1a54b34e8deda76c1f4b3e5cf669a2b38f0b1a063ad25eb4ae48cbae6eccd2e7"
    end

    on_intel do
      url "https://github.com/ScaferuZ/tfw/releases/download/v#{version}/tfw_linux_amd64.tar.gz"
      sha256 "493f0bca3dcd12a6f98a09e81b50e279676c6ea5b6d0569651997514732a5718"
    end
  end

  def install
    bin.install "tfw"
  end

  test do
    assert_match "tfw #{version}", shell_output("#{bin}/tfw version")
    assert_match "tfw plan", shell_output("#{bin}/tfw help 2>&1")
  end
end
