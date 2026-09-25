#!/usr/bin/env python
"""Test Odoo connection using interactive approach."""

import sys
import os
import json

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from odoo_mcp.odoo_client import OdooClient
    
    # Load configuration
    config_path = "C:/Users/pcyco/Desktop/GITDEV/mcp-odoo/odoo_config.json"
    print(f"Loading config from: {config_path}")
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    print(f"Config loaded. URL: {config['url']}")
    print(f"Database: {config['db']}")
    print(f"Username: {config['username']}")
    
    # Try to connect
    print("\n🔌 Connecting to Odoo...")
    client = OdooClient(config)
    
    print("✅ Connected successfully!")
    
    # Get server version
    print("\n📋 Getting server information...")
    version = client.get_server_version()
    print(f"Odoo Version: {version}")
    
    # Get installed modules
    print("\n🔍 Getting installed modules...")
    modules = client.get_installed_modules(limit=5)
    print(f"Found {len(modules)} modules")
    
    print("\n✅ All tests passed - Odoo connection is working!")
    
except Exception as e:
    print(f"\n❌ Connection failed: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
