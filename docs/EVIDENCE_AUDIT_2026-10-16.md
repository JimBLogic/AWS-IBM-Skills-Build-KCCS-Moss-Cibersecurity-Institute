# AWS / IBM SkillsBuild / MCSI training evidence audit (2026-10-16)

**Repository:** Original public non-fork `JimBLogic/AWS-IBM-Skills-Build-KCCS-Moss-Cibersecurity-Institute`. Baseline main `3222c26a31185c424a322d879bac02b7fd9d8184`, candidate branch `audit/credential-evidence-links-20261016`. No merge or deployment, no PDF/media modification, no new certifications or personal info added.

## Verified baseline inventory

- Existing README linked `certs/AWS SimuLearn Cloud Practitioner 12h.png` as a training badge image, linked the IBM Python 60h PDF and cited external Credly and MCSI platforms.
- Two existing AWS course-completion PDFs were **present in the repo but not linked by the README**: `156_3_6860342_1735817985_AWS Course Completion Certificate.pdf` and `18443_5_6860342_1735810643_AWS Skill Builder Course Completion Certificate.pdf`. The candidate adds explicit local links using existing bytes. A lack of README links does not imply the actual documents were unavailable or fraudulent.
- The baseline had no existing GitHub Actions CI run or regression guard for the evidence links. An independently hosted Credly badge URL can be cited but its validity was not verified via issuer API or browser in this PR.

## Candidate-only change

- Preserve every original certificate, badge, reference link and file; add two accurate relative README links.
- Clarify that AWS SimuLearn/Skill Builder courses are **training**, not proof of an independent AWS Certified Cloud Practitioner exam pass.
- Add four dependency-free Python tests for 4 linked local paths, file size/presence, exact media inventory, expected external URL domains and read-only CI permission boundaries.
- CI only on PR, uses SHA-pinned official checkout with `contents:read`, no preserved Git credentials and **no uploads, publications, package installation or direct PDF parsing**.

## Remaining uncertainty

- A local file and an external issuer URL alone do **not** independently prove a certificate's authenticity, issue date or ownership. The original documents were not opened or verified against the issuers.
- This repository is public; PDFs may include personally identifying information already disclosed. A future privacy review requires explicit owner approval and should not rewrite Git history automatically.
- No browser, LinkedIn/Credly/MCSI profile integration, or mobile check has been claimed.

**DRAFT for review only. No merge, public release, repo visibility change or certificate rehosting without authorization.**
