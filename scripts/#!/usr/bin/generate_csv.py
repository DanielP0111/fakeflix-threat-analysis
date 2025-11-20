#!/usr/bin/env python3
"""Generate Jira-ready CSV from threat data"""
import csv

def generate_jira_csv(threats, output_file='threats_jira.csv'):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Summary', 'Priority', 'Description', 'Labels', 'Risk Score'])
        for threat in threats:
            risk_score = threat.get('risk_score', 0)
            if risk_score >= 4.0:
                priority = 'Critical'
            elif risk_score >= 3.5:
                priority = 'High'
            elif risk_score >= 3.0:
                priority = 'Medium'
            else:
                priority = 'Low'
            writer.writerow([
                threat.get('title', 'Unknown Threat'),
                priority,
                threat.get('description', ''),
                threat.get('stride_category', 'Unknown'),
                f"{risk_score:.1f}"
            ])
    print(f"Generated {output_file} with {len(threats)} threats")

def main():
    example_threats = [
        {'title': 'API Key Exposure', 'stride_category': 'Information Disclosure',
         'description': 'TMDB API key exposed', 'risk_score': 3.5},
        {'title': 'Incomplete Token Validation', 'stride_category': 'Information Disclosure',
         'description': 'ID tokens not verified', 'risk_score': 4.0}
    ]
    generate_jira_csv(example_threats)

if __name__ == "__main__":
    main()
