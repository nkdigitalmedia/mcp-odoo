#!/usr/bin/env python
"""Check and list all installed Odoo apps (modules)."""

import sys
import os
import json

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def check_odoo_apps():
    """List all installed Odoo apps/modules."""
    print("📦 Checking Odoo Apps/Modules")
    print("=" * 60)
    
    # Load config
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'odoo_config.json')
        with open(config_path, 'r') as f:
            config = json.load(f)
        print(f"✓ Connected to: {config['url']}")
        print(f"✓ Database: {config['db']}")
        print()
        
    except Exception as e:
        print(f"❌ Failed to load config: {e}")
        return False
    
    # Connect and get apps
    try:
        from odoo_mcp.odoo_client import OdooClient
        
        client = OdooClient(
            url=config['url'],
            db=config['db'],
            username=config['username'],
            api_key=config.get('api_key'),
            password=config.get('password') or config.get('api_key')
        )
        
        # Get server version
        version = client.get_server_version()
        print(f"Odoo Server Version: {version}")
        print("-" * 60)
        
        # Get all installed modules/apps
        print("\n🔍 Fetching installed applications...")
        
        # Search for installed modules
        domain = [
            ('state', '=', 'installed')
        ]
        
        fields = ['name', 'display_name', 'category', 'summary', 'author', 'version', 'state']
        
        modules = client.search_read(
            'ir.module.module',
            domain,
            fields=fields,
            limit=100,
            order='category ASC, display_name ASC'
        )
        
        print(f"\n✅ Found {len(modules)} installed modules/apps:")
        print()
        
        # Group by category
        categories = {}
        for module in modules:
            category = module.get('category', 'Uncategorized') or 'Uncategorized'
            if category not in categories:
                categories[category] = []
            categories[category].append(module)
        
        # Display modules by category
        for category, mods in sorted(categories.items()):
            print(f"\n📁 {category} ({len(mods)} modules)")
            print("-" * 60)
            
            for mod in sorted(mods, key=lambda x: x.get('display_name', x['name'])):
                display_name = mod.get('display_name', mod['name'])
                summary = mod.get('summary', '')
                version = mod.get('version', '')
                
                print(f"  • {display_name}")
                if summary:
                    print(f"    {summary}")
                if version:
                    print(f"    Version: {version}")
                print()
        
        # Show summary
        print("=" * 60)
        print(f"📊 SUMMARY: {len(modules)} modules installed across {len(categories)} categories")
        
        # List main Odoo apps
        print("\n🏢 Main Odoo Applications:")
        main_apps = [
            'sale', 'purchase', 'account', 'stock', 'mrp', 'project', 
            'hr', 'crm', 'website', 'point_of_sale', 'ecommerce'
        ]
        
        app_modules = [m for m in modules if m['name'] in main_apps]
        if app_modules:
            for app in sorted(app_modules, key=lambda x: x.get('display_name', x['name'])):
                print(f"  ✓ {app.get('display_name', app['name'])}")
        else:
            print("  (No main Odoo apps detected)")
        
        print("\n✅ App check completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Failed to check apps: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = check_odoo_apps()
    sys.exit(0 if success else 1)
