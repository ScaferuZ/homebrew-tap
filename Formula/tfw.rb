class Tfw < Formula
  desc "Guardrail for terraform plan/apply: forces 'destroy' instead of 'yes' on destructive plans"
  homepage "https://github.com/ScaferuZ/tfw"
  version "0.2.0"
  license "MIT"

  livecheck do
    url :homepage
    strategy :github_latest
  end

  on_macos do
    on_arm do
      url "https://github.com/ScaferuZ/tfw/releases/download/v#{version}/tfw_darwin_arm64.tar.gz"
      sha256 "3be60b50e8267babb44f825e58c23630dd16f3969801dd4da6a3830559a68177"
    end

    on_intel do
      url "https://github.com/ScaferuZ/tfw/releases/download/v#{version}/tfw_darwin_amd64.tar.gz"
      sha256 "6d156fcc8e1375928792361298675afc06de2291c46e8219db9957a70025597b"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/ScaferuZ/tfw/releases/download/v#{version}/tfw_linux_arm64.tar.gz"
      sha256 "adfe81bb1a4dc755d0a4d1aed24119a5a05b628d23dcdc50ea73c0a641ab258d"
    end

    on_intel do
      url "https://github.com/ScaferuZ/tfw/releases/download/v#{version}/tfw_linux_amd64.tar.gz"
      sha256 "f48f1098c0695e55bfd5869cee047a618779bd5c5d655bd2070fb996394997c2"
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
