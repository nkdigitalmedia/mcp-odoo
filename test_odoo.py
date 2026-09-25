#!/usr/bin/env python
"""Simple test to check Odoo connection."""

import sys
import os
import json

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_connection():
    """Test basic connectivity to Odoo."""
    print("Testing Odoo connection...")
    print("-" * 50)
    
    # Load config
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'odoo_config.json')
        
        # Check if config exists
        if not os.path.exists(config_path):
            print(f"❌ Config file not found: {config_path}")
            return False
            
        with open(config_path, 'r') as f:
            config = json.load(f)
            
        print(f"✓ Config loaded from: {config_path}")
        print(f"  URL: {config['url']}")
        print(f"  Database: {config['db']}")
        print(f"  Username: {config['username']}")
        print(f"  API Key: {'Present' if 'api_key' in config or 'password' in config else 'Missing'}")
        
    except Exception as e:
        print(f"❌ Failed to load config: {e}")
        return False
    
    # Try to connect
    print("\nAttempting to connect to Odoo...")
    try:
        from odoo_mcp.odoo_client import OdooClient
        
        client = OdooClient(config)
        
        print("✓ Connected successfully!")
        
        # Get server info
        print("\nFetching server information...")
        version = client.get_server_version()
        print(f"✓ Odoo Version: {version}")
        
        user_context = client.get_user_context()
        print(f"✓ User Context: {user_context}")
        
        # Test basic search
        print("\nTesting search functionality...")
        # Search for some models
        models_count = client.search_count("res.partner", [])
        print(f"✓ Found {models_count} contacts (res.partner)")
        
        # Get a few records
        records = client.search_read("res.partner", [], limit=3, fields=['name', 'email'])
        if records:
            print(f"✓ Sample contact: {records[0]}")
        
        print("\n" + "-" * 50)
        print("🎉 SUCCESS! Odoo connection is working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
