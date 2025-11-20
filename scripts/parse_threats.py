#!/usr/bin/env python3
"""Parse OWASP Threat Dragon JSON and extract threat data"""
import json
import sys

def parse_threat_dragon_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    threats = []
    diagrams = data.get('detail', {}).get('diagrams', [])
    for diagram in diagrams:
        cells = diagram.get('cells', [])
        for cell in cells:
            if cell.get('shape') == 'flow':
                flow_data = cell.get('data', {})
                if flow_data.get('threats'):
                    threats.extend(flow_data['threats'])
    return threats

def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_threats.py <threat-dragon.json>")
        sys.exit(1)
    threats = parse_threat_dragon_json(sys.argv[1])
    print(f"Found {len(threats)} threats in DFD")
    for i, threat in enumerate(threats, 1):
        print(f"\nThreat {i}:")
        print(f"  Title: {threat.get('title', 'N/A')}")
        print(f"  Type: {threat.get('type', 'N/A')}")

if __name__ == "__main__":
    main()
