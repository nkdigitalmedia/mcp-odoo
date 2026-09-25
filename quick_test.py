import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Test the configuration file exists
config_path = os.path.join(os.path.dirname(__file__), 'odoo_config.json')
print(f"Looking for config at: {config_path}")

if not os.path.exists(config_path):
    print("❌ Config file not found! Creating default...")
    with open(config_path, 'w') as f:
        f.write('{"url": "https://nkdigital.odoo.com", "db": "nkdigital", "username": "nkdigitalmedia@gmail.com", "api_key": "82bac903ed705844b366132f05cb1aee01a8c331"}')

print("✅ Config file exists")

# Now test connection
print("\n🔌 Testing Odoo connection...")
try:
    from odoo_mcp.odoo_client import get_odoo_client
    
    client = get_odoo_client()
    version = client.get_server_version()
    print(f"✅ Connected! Odoo version: {version}")
    
    # Get a list of installed modules
    modules = client.get_installed_modules(limit=3)
    print(f"✅ Installed modules: {[m.get('name') for m in modules]}")
    
    print("\n🎉 Connection successful!")
    
except Exception as e:
    print(f"\n❌ Connection failed: {e}")
    import traceback
    traceback.print_exc()
