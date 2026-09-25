#!/usr/bin/env python3
"""Test Odoo connection to verify authentication works correctly."""

import sys
import os

# Add src to Python path so we can import odoo_mcp
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from odoo_mcp.odoo_client import get_odoo_client

def test_connection():
    """Test basic connectivity to Odoo instance."""
    print("🔄 Testing Odoo connection...")
    print("=" * 50)
    
    try:
        # Get Odoo client instance
        print("1. Loading client configuration...")
        client = get_odoo_client()
        print(f"   ✓ Client initialized")
        
        # Test connection by getting server version
        print("\n2. Getting server version...")
        version = client.get_server_version()
        print(f"   ✓ Server Version: {version}")
        
        # Get user context
        print("\n3. Getting user context...")
        context = client.get_user_context()
        print(f"   ✓ User Context: {context}")
        
        # Test basic read operation
        print("\n4. Testing read operation (search_read on ir.model)...")
        models = client.search_read("ir.model", [], limit=5)
        print(f"   ✓ Found {len(models)} models")
        if models:
            print(f"   ✓ First model: {models[0]}")
        
        # Get installed modules
        print("\n5. Getting installed modules...")
        modules = client.get_installed_modules(limit=10)
        print(f"   ✓ Found {len(modules)} installed modules")
        if modules:
            print(f"   ✓ Sample module: {modules[0]}")
        
        print("\n" + "=" * 50)
        print("✅ All tests passed! Connection is working correctly.")
        return True
        
    except Exception as e:
        print(f"\n❌ Connection test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
