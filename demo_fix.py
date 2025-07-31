#!/usr/bin/env python3
"""
Demonstration script showing the fix for the intentional error.
This script shows how to apply the fix to the app.py file.
"""

import os
import shutil
from datetime import datetime

def backup_original():
    """Create a backup of the original app.py file."""
    if os.path.exists('app.py'):
        backup_name = f"app_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        shutil.copy('app.py', backup_name)
        print(f"✅ Created backup: {backup_name}")
        return backup_name
    return None

def apply_fix():
    """Apply the fix to the app.py file."""
    print("🔧 Applying fix to app.py...")
    
    # Read the current app.py file
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Apply the fix by replacing the problematic line
    old_line = '        result = undefined_variable + "This should cause an error"'
    new_line = '        error_message = "Error triggered successfully"\n        result = error_message + " - This was the intentional error"'
    
    if old_line in content:
        fixed_content = content.replace(old_line, new_line)
        
        # Write the fixed content back
        with open('app.py', 'w') as f:
            f.write(fixed_content)
        
        print("✅ Fix applied successfully!")
        print("   - Replaced undefined_variable with a proper string variable")
        print("   - The error should now be resolved")
        return True
    else:
        print("❌ Could not find the problematic line in app.py")
        return False

def test_fix():
    """Test the fix by running a simple test."""
    print("\n🧪 Testing the fix...")
    
    # Import the fixed app module
    try:
        import app
        print("✅ app.py imports successfully")
        
        # Test the trigger_error function logic
        app.error_enabled = True
        try:
            # This should not raise an error now
            result = app.trigger_error()
            print("✅ trigger_error function works without error!")
            print(f"   Result: {result}")
        except Exception as e:
            print(f"❌ Error still exists: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error importing app.py: {e}")
        return False

def restore_backup(backup_name):
    """Restore the original app.py from backup."""
    if backup_name and os.path.exists(backup_name):
        shutil.copy(backup_name, 'app.py')
        print(f"✅ Restored original app.py from {backup_name}")

def main():
    """Main demonstration function."""
    print("🐛 PYTHON SAMPLE SERVER - ERROR FIX DEMONSTRATION")
    print("=" * 60)
    
    # Step 1: Create backup
    backup_name = backup_original()
    
    # Step 2: Apply the fix
    if apply_fix():
        # Step 3: Test the fix
        if test_fix():
            print("\n🎉 SUCCESS: The error has been fixed!")
            print("   - The NameError is now resolved")
            print("   - The trigger_error function works correctly")
            print("   - This demonstrates how a PR would fix the issue")
        else:
            print("\n❌ FAILED: The fix did not work as expected")
    else:
        print("\n❌ FAILED: Could not apply the fix")
    
    # Step 4: Ask if user wants to restore the original
    print("\n" + "=" * 60)
    response = input("Do you want to restore the original app.py with the error? (y/n): ").lower()
    
    if response == 'y':
        restore_backup(backup_name)
        print("✅ Original app.py restored with the intentional error")
    else:
        print("✅ Keeping the fixed version")
    
    print("\n📝 SUMMARY:")
    print("   - This demonstration shows how to fix the intentional error")
    print("   - The fix involves replacing the undefined variable with a proper string")
    print("   - This creates a perfect scenario for testing PR workflows")
    print("   - The error is easily reproducible and fixable")

if __name__ == "__main__":
    main() 