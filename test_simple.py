import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from odoo_mcp.odoo_client import get_odoo_client
    
    print("🔄 Testing Odoo connection...")
    print("=" * 50)
    
    # Create client
    client = get_odoo_client()
    
    # Get server version
    print("Getting server version...")
    version = client.get_server_version()
    print("✓ Server Version:", version)
    
    # Get user context  
    print("\nGetting user context...")
    context = client.get_user_context()
    print("✓ User Context:", context)
    
    print("\n" + "=" * 50)
    print("✅ Connection successful!")
    
except Exception as e:
    print("❌ Connection failed:", str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)
