#!/usr/bin/env python3
"""
Example script showing how to fix the intentional error in the Python Sample Server.

This script demonstrates the fix for the NameError in the trigger_error() function.
"""

def show_original_error():
    """Show the original code with the intentional error."""
    print("🔴 ORIGINAL CODE (with intentional error):")
    print("=" * 60)
    print("""
@app.route('/trigger-error')
def trigger_error():
    \"\"\"Endpoint that generates an error when enabled.\"\"\"
    global error_enabled
    
    if error_enabled:
        # INTENTIONAL ERROR: This will cause a NameError because 'undefined_variable' is not defined
        # This is the error that can be fixed in a PR
        result = undefined_variable + "This should cause an error"
        return jsonify({'result': result})
    else:
        return jsonify({
            'message': 'Error generation is disabled. Enable it first with POST /error/enable',
            'status': 'disabled'
        })
""")
    print("\n❌ This code will cause a NameError because 'undefined_variable' is not defined.")

def show_fixed_code():
    """Show the fixed code without the error."""
    print("\n🟢 FIXED CODE (error resolved):")
    print("=" * 60)
    print("""
@app.route('/trigger-error')
def trigger_error():
    \"\"\"Endpoint that generates an error when enabled.\"\"\"
    global error_enabled
    
    if error_enabled:
        # FIXED: Define the variable or use a string literal
        error_message = "Error triggered successfully"
        result = error_message + " - This was the intentional error"
        return jsonify({'result': result})
    else:
        return jsonify({
            'message': 'Error generation is disabled. Enable it first with POST /error/enable',
            'status': 'disabled'
        })
""")
    print("\n✅ This code will work correctly without any NameError.")

def show_alternative_fixes():
    """Show alternative ways to fix the error."""
    print("\n🔄 ALTERNATIVE FIXES:")
    print("=" * 60)
    
    print("\nOption 1: Use a string literal directly")
    print("result = \"Error triggered successfully\" + \" - This was the intentional error\"")
    
    print("\nOption 2: Define the variable first")
    print("undefined_variable = \"Error triggered successfully\"")
    print("result = undefined_variable + \" - This was the intentional error\"")
    
    print("\nOption 3: Use a different approach")
    print("result = f\"Error triggered successfully - This was the intentional error\"")
    
    print("\nOption 4: Return a simple message")
    print("return jsonify({'result': 'Error triggered successfully'})")

def show_pull_request_steps():
    """Show the steps to create a pull request to fix the error."""
    print("\n📋 PULL REQUEST STEPS:")
    print("=" * 60)
    
    steps = [
        "1. Fork the repository",
        "2. Create a new branch: git checkout -b fix/trigger-error",
        "3. Edit app.py and fix the undefined_variable error",
        "4. Test your fix: python test_server.py",
        "5. Commit your changes: git commit -m 'Fix NameError in trigger_error function'",
        "6. Push to your fork: git push origin fix/trigger-error",
        "7. Create a pull request on GitHub",
        "8. Add description explaining the fix",
        "9. Request review from maintainers"
    ]
    
    for step in steps:
        print(f"   {step}")

def show_testing_steps():
    """Show how to test the fix."""
    print("\n🧪 TESTING THE FIX:")
    print("=" * 60)
    
    testing_steps = [
        "1. Start the server: python app.py",
        "2. Enable error generation: curl -X POST http://localhost:5000/error/enable",
        "3. Trigger the error: curl http://localhost:5000/trigger-error",
        "4. Before fix: Should return 500 error with NameError",
        "5. After fix: Should return 200 with success message",
        "6. Run the test script: python test_server.py"
    ]
    
    for step in testing_steps:
        print(f"   {step}")

def main():
    """Main function to demonstrate the error and fix."""
    print("🐛 PYTHON SAMPLE SERVER - ERROR FIX EXAMPLE")
    print("=" * 80)
    
    show_original_error()
    show_fixed_code()
    show_alternative_fixes()
    show_pull_request_steps()
    show_testing_steps()
    
    print("\n" + "=" * 80)
    print("🎯 SUMMARY:")
    print("   - The intentional error is a NameError in the trigger_error() function")
    print("   - The fix involves defining the undefined variable or using a string literal")
    print("   - This creates a perfect scenario for testing PR workflows")
    print("   - The error is easily reproducible and fixable")

if __name__ == "__main__":
    main() 