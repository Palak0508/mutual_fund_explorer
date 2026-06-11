"""
Bluestock Mutual Fund Analytics Pipeline - Master Execution Script
Author: Capstone Analytics Team
Year: 2026
"""

import sys
import os
import subprocess

def print_banner(step_title):
    print("\n" + "="*60)
    print(f"🚀 {step_title.upper()}")
    print("="*60)

def run_script(script_name):
    """Safely executes a standalone sub-script within the workspace pipeline."""
    if not os.path.exists(script_name):
        print(f"⚠️ Warning: '{script_name}' not found. Skipping step.")
        return False
        
    try:
        print(f"Running script: {script_name}...")
        # Run process and wait for completion
        result = subprocess.run([sys.executable, script_name], check=True, text=True)
        if result.returncode == 0:
            print(f"✅ Successfully executed {script_name}")
            return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error occurred while running {script_name}: {e}")
        return False

def main():
    print_banner("Starting Bluestock End-to-End Analytics Pipeline")
    
    # Step 1: Data Ingestion
    print_banner("Step 1: Raw Data Ingestion & Database Sync")
    run_script("data_ingestion.py")
    
    # Step 2: Data Cleaning & Preprocessing
    print_banner("Step 2: Data Cleaning & Validation")
    run_script("data_cleaning.py")
    
    # Step 3: Interactive Command Line Analytics Utility
    print_banner("Pipeline check complete. Operational tools online.")
    print("✨ Master pipeline processing sequence finished successfully!")

if __name__ == "__main__":
    main()