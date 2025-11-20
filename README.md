# Fakeflix Threat Analysis

**CAP 5150 Final Project**  
**Author:** Daniel Perera (da874557@ucf.edu)  
**Institution:** University of Central Florida

## Overview

Systematic threat modeling of Fakeflix—a React SPA integrating TMDB API, Firebase Authentication, and Cloud Firestore—using DFD and STRIDE methodology.

## Repository Contents

- **`/dfd/`** - OWASP Threat Dragon DFD files (JSON + PNG)
- **`/risk-assessment/`** - Threat spreadsheet with 23 threats and risk scores
- **`/scripts/`** - Python scripts for parsing and CSV generation
- **`/figures/`** - Methodology pipeline and DFD diagrams

## Methodology

Three-phase workflow:
1. Phase 1: System modeling with DFD (5 elements, 3 trust boundaries)
2. Phase 2: STRIDE threat enumeration (23 threats identified)
3. Phase 3: Risk scoring using R = 0.5L + 0.5I

## Key Results

- 156% more threats found vs. ad hoc baseline (23 vs. 9)
- 40% faster per-element analysis
- 100% actionability for high-risk threats (R ≥ 3.5)
- Strong validation: Cohen's κ = 1.0, Spearman ρ = 0.85

## Usage

View DFD: Open `dfd/fig_dfd.json` in OWASP Threat Dragon  
Review threats: Open `risk-assessment/threat-assessment-fakeflix.xlsx`  
Run scripts: `python scripts/parse_threats.py dfd/fig_dfd.json`
