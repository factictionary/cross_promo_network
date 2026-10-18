#!/usr/bin/env python3
"""
Manifest Validator for Cross-Promo Network.
Ensures campaigns.json schema is valid, required fields exist, and weights are positive integers.
"""

import json
import os
import sys

def validate_manifest(file_path):
    print(f"Validating {file_path}...")
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON syntax error: {e}")
        return False

    campaigns = data.get("campaigns", [])
    if not isinstance(campaigns, list):
        print("Error: 'campaigns' must be an array.")
        return False

    if len(campaigns) == 0:
        print("Warning: No campaigns found in manifest.")

    required_keys = ["id", "package_name", "app_name", "tagline", "target_url"]
    valid = True

    for i, camp in enumerate(campaigns):
        camp_id = camp.get("id", f"index_{i}")
        for key in required_keys:
            if not camp.get(key):
                print(f"Campaign '{camp_id}' is missing required field: '{key}'")
                valid = False

        weight = camp.get("weight", 10)
        if not isinstance(weight, (int, float)) or weight <= 0:
            print(f"Campaign '{camp_id}' has invalid weight: {weight} (must be > 0)")
            valid = False

    if valid:
        print(f"SUCCESS: {len(campaigns)} campaigns validated successfully!")
    return valid

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "campaigns.json"
    success = validate_manifest(path)
    sys.exit(0 if success else 1)
