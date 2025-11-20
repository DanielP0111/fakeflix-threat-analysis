#!/usr/bin/env python3
"""Generate Jira-ready CSV from Fakeflix threat assessment spreadsheet"""
import csv
import sys

def generate_jira_csv_from_spreadsheet(output_file='threats_jira.csv'):
    """
    Generate CSV formatted for Jira import from hardcoded threat data
    In production, this would read from the Excel spreadsheet
    """
    
    # Threat data from threat-assessment-fakeflix.xlsx
    # (Top 10 threats as examples - full list would include all 23)
    threats = [
        {'id': 'T01', 'title': 'Incomplete Firebase ID token validation', 
         'stride': 'Information Disclosure', 'risk': 4.0, 
         'mitigation': 'Verify issuer, audience, expiry using Firebase Admin SDK'},
        {'id': 'T02', 'title': 'Overly permissive Firestore Security Rules', 
         'stride': 'Information Disclosure', 'risk': 4.0,
         'mitigation': 'Implement production rules with ownership checks'},
        {'id': 'T03', 'title': 'TMDB API key exposed in client bundle', 
         'stride': 'Information Disclosure', 'risk': 3.5,
         'mitigation': 'Proxy API calls through backend, rotate keys'},
        {'id': 'T04', 'title': 'PII exposure in logs and analytics', 
         'stride': 'Information Disclosure', 'risk': 3.5,
         'mitigation': 'Redact sensitive fields, minimal collection'},
        {'id': 'T05', 'title': 'Inadequate Firestore document ownership validation', 
         'stride': 'Elevation of Privilege', 'risk': 3.5,
         'mitigation': 'Add auth checks in Security Rules'},
        {'id': 'T06', 'title': 'TMDB API rate limit exhaustion', 
         'stride': 'Denial of Service', 'risk': 3.5,
         'mitigation': 'Client-side throttling, caching, quota monitoring'},
        {'id': 'T07', 'title': 'Weak Firebase password policy', 
         'stride': 'Spoofing', 'risk': 3.0,
         'mitigation': 'Enforce 12-char minimum with complexity'},
        {'id': 'T08', 'title': 'Firestore mass document creation DoS', 
         'stride': 'Denial of Service', 'risk': 3.0,
         'mitigation': 'Write rate limits in Security Rules'},
        {'id': 'T09', 'title': 'MITM tampering of TMDB metadata', 
         'stride': 'Tampering', 'risk': 3.0,
         'mitigation': 'Enforce HTTPS, implement Subresource Integrity'},
        {'id': 'T10', 'title': 'Email enumeration via sign-up errors', 
         'stride': 'Spoofing', 'risk': 3.0,
         'mitigation': 'Generic errors, implement CAPTCHA'}
    ]
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Jira CSV header
        writer.writerow([
            'Issue ID',
            'Summary', 
            'Priority', 
            'Description', 
            'Labels', 
            'Risk Score'
        ])
        
        for threat in threats:
            risk_score = threat['risk']
            
            # Map risk score to Jira priority
            if risk_score >= 4.0:
                priority = 'Critical'
            elif risk_score >= 3.5:
                priority = 'High'
            elif risk_score >= 3.0:
                priority = 'Medium'
            else:
                priority = 'Low'
            
            writer.writerow([
                threat['id'],
                threat['title'],
                priority,
                threat['mitigation'],
                threat['stride'],
                f"{risk_score:.1f}"
            ])
    
    print(f"✅ Generated {output_file} with {len(threats)} threats")
    print(f"📊 Risk distribution:")
    print(f"   - Critical (R≥4.0): {sum(1 for t in threats if t['risk'] >= 4.0)}")
    print(f"   - High (R≥3.5): {sum(1 for t in threats if t['risk'] >= 3.5)}")
    print(f"   - Medium (R≥3.0): {sum(1 for t in threats if t['risk'] >= 3.0)}")

if __name__ == "__main__":
    generate_jira_csv_from_spreadsheet()
    print("\n✅ CSV file ready for Jira import!")
