"""Credential evidence URL and inventory checks without reading personal media."""
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
LOCAL = re.findall(r"!?\[[^\]]+\]\((\./certs/[^)]+)\)", README)

EXPECTED = {
    "AWS SimuLearn Cloud Practitioner 12h.png",
    "156_3_6860342_1735817985_AWS Course Completion Certificate.pdf",
    "18443_5_6860342_1735810643_AWS Skill Builder Course Completion Certificate.pdf",
    "python 60h.pdf",
}


def resolve_credential(path: str) -> Path:
    decoded = unquote(path)
    relative = Path(decoded)
    if not decoded.startswith("./certs/") or relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Unsafe credential source path")
    target = ROOT / relative
    if target.is_symlink() or not target.resolve().is_relative_to(ROOT):
        raise ValueError("Credential path is outside repo or linked")
    return target


class EvidenceLinks(unittest.TestCase):
    def test_every_local_badge_and_pdf_ref_is_present_and_nonempty(self):
        self.assertEqual(len(LOCAL), 4)
        names = {resolve_credential(uri).name for uri in LOCAL}
        self.assertEqual(names, EXPECTED)
        for uri in LOCAL:
            file = resolve_credential(uri)
            self.assertTrue(file.is_file(), uri)
            self.assertGreater(file.stat().st_size, 1000, uri)
            self.assertIn(file.suffix.lower(), {".pdf", ".png"})

    def test_inventory_has_no_unlinked_certificates(self):
        tracked = {p.name for p in (ROOT / "certs").iterdir()
                   if p.is_file() and p.suffix.lower() in {".png", ".pdf"}}
        self.assertEqual(tracked, EXPECTED)

    def test_external_issuer_links_are_scoped_not_falsely_credentialed(self):
        self.assertIn("not an assertion that I passed", README)
        self.assertIn("Certificate documents may contain personal data", README)
        links = re.findall(r"\]\((https://[^)]+)\)", README)
        self.assertGreaterEqual(len(links), 4)
        for uri in links:
            parsed = urlparse(uri)
            self.assertEqual(parsed.scheme, "https")
            self.assertIn(parsed.hostname, {
                "www.credly.com", "students.mosse-institute.com", "jimblogic.github.io",
            })

    def test_ci_only_performs_safe_static_checks(self):
        ci = (ROOT / ".github/workflows/evidence-links.yml").read_text(encoding="utf-8")
        self.assertIn("contents: read", ci)
        self.assertIn("persist-credentials: false", ci)
        self.assertIn("pull_request:", ci)
        self.assertIn("unittest discover", ci)
        for name in ("contents: write", "pages: write", "upload-artifact", "deploy-pages", "workflow_dispatch"):
            self.assertNotIn(name, ci)


if __name__ == "__main__":
    unittest.main()
