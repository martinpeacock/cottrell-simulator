# Changelog
All notable changes to this project will be documented in this file.

The format follows [Semantic Versioning](https://semver.org/):
`MAJOR.MINOR.PATCH`

---

## [1.3.0] – 2025-01-XX
### Added
- Sidebar layout for all simulation controls  
- Tabbed interface for multi‑simulation expansion  
- Downloadable PNG plot export  
- ZP branding (logo + footer)  
- README.md, requirements.txt, .gitignore  
- Repository structure for long‑term scalability  

### Changed
- Updated UI layout to a more professional, modular design  
- Improved parameter handling (mm² electrode area, mM concentration)  

### Fixed
- Cleaned and validated triple‑quoted strings for Spyder compatibility  
- Removed hidden characters that caused syntax errors  

---

## [1.2.2] – 2024-12-XX
### Added
- Electrode area input converted to mm² (user‑facing)  
- Concentration input converted to mM (user‑facing)  
- Internal unit conversions for accuracy  
- Improved UI polish and layout consistency  

### Fixed
- Minor formatting issues in the sidebar  
- Improved error handling for invalid inputs  

---

## [1.2.0] – 2024-12-XX
### Added
- ZP logo and footer branding  
- Contact link to Zimmer & Peacock  
- Semantic versioning introduced  

### Changed
- Improved layout and spacing for clarity  

---

## [1.1.0] – 2024-11-XX
### Added
- Pause/skip functionality for early‑time Cottrell artefacts  
- Updated versioning to reflect new features  

---

## [1.0.0] – 2024-11-XX
### Added
- Initial Cottrell chronoamperometry simulator  
- Dual‑axis plot (current + charge)  
- Basic parameter inputs  
- Streamlit deployment  