#!/usr/bin/env python3
"""
Simple test script for the Python Sample Server.
This script demonstrates how to test the server endpoints and trigger the intentional error.
"""

import requests
import json
import time

# Server configuration
BASE_URL = "http://localhost:5000"

def test_server():
    """Test the server endpoints and demonstrate error triggering."""
    
    print("🚀 Testing Python Sample Server")
    print("=" * 50)
    
    try:
        # Test 1: Check if server is running
        print("\n1. Testing server health...")
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Server is healthy!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Server health check failed: {response.status_code}")
            return
        
        # Test 2: Get server info
        print("\n2. Getting server information...")
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Server info retrieved!")
            print(f"   Response: {response.json()}")
        
        # Test 3: Check error status (should be disabled by default)
        print("\n3. Checking error generation status...")
        response = requests.get(f"{BASE_URL}/error/status")
        if response.status_code == 200:
            status = response.json()
            print(f"✅ Error status: {status['error_enabled']}")
        
        # Test 4: Try to trigger error while disabled
        print("\n4. Testing error trigger while disabled...")
        response = requests.get(f"{BASE_URL}/trigger-error")
        if response.status_code == 200:
            print("✅ Error trigger correctly disabled!")
            print(f"   Response: {response.json()}")
        
        # Test 5: Enable error generation
        print("\n5. Enabling error generation...")
        response = requests.post(f"{BASE_URL}/error/enable")
        if response.status_code == 200:
            print("✅ Error generation enabled!")
            print(f"   Response: {response.json()}")
        
        # Test 6: Trigger the intentional error
        print("\n6. Triggering the intentional error...")
        try:
            response = requests.get(f"{BASE_URL}/trigger-error")
            print(f"❌ Unexpected: Error was not triggered. Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("✅ Intentional error triggered successfully!")
            print(f"   Error: {e}")
        
        # Test 7: Disable error generation
        print("\n7. Disabling error generation...")
        response = requests.post(f"{BASE_URL}/error/disable")
        if response.status_code == 200:
            print("✅ Error generation disabled!")
            print(f"   Response: {response.json()}")
        
        # Test 8: Test data endpoints
        print("\n8. Testing data endpoints...")
        response = requests.get(f"{BASE_URL}/api/data")
        if response.status_code == 200:
            print("✅ Data endpoint working!")
            data = response.json()
            print(f"   Found {len(data['data'])} items")
        
        # Test 9: Test specific data item
        print("\n9. Testing specific data item...")
        response = requests.get(f"{BASE_URL}/api/data/1")
        if response.status_code == 200:
            print("✅ Specific data item retrieved!")
            print(f"   Item: {response.json()}")
        
        print("\n" + "=" * 50)
        print("🎉 All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure it's running on http://localhost:5000")
        print("   Run: python app.py")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")

def interactive_test():
    """Interactive test mode for manual testing."""
    print("\n🔄 Interactive Test Mode")
    print("=" * 50)
    print("Available commands:")
    print("  health     - Check server health")
    print("  status     - Check error status")
    print("  enable     - Enable error generation")
    print("  disable    - Disable error generation")
    print("  trigger    - Trigger the error")
    print("  data       - Get all data")
    print("  item <id>  - Get specific data item")
    print("  quit       - Exit")
    
    while True:
        try:
            command = input("\nEnter command: ").strip().lower()
            
            if command == "quit":
                break
            elif command == "health":
                response = requests.get(f"{BASE_URL}/health")
                print(f"Status: {response.status_code}")
                print(f"Response: {response.json()}")
            elif command == "status":
                response = requests.get(f"{BASE_URL}/error/status")
                print(f"Status: {response.status_code}")
                print(f"Response: {response.json()}")
            elif command == "enable":
                response = requests.post(f"{BASE_URL}/error/enable")
                print(f"Status: {response.status_code}")
                print(f"Response: {response.json()}")
            elif command == "disable":
                response = requests.post(f"{BASE_URL}/error/disable")
                print(f"Status: {response.status_code}")
                print(f"Response: {response.json()}")
            elif command == "trigger":
                try:
                    response = requests.get(f"{BASE_URL}/trigger-error")
                    print(f"Status: {response.status_code}")
                    print(f"Response: {response.json()}")
                except requests.exceptions.RequestException as e:
                    print(f"Error triggered: {e}")
            elif command == "data":
                response = requests.get(f"{BASE_URL}/api/data")
                print(f"Status: {response.status_code}")
                print(f"Response: {response.json()}")
            elif command.startswith("item "):
                item_id = command.split()[1]
                response = requests.get(f"{BASE_URL}/api/data/{item_id}")
                print(f"Status: {response.status_code}")
                print(f"Response: {response.json()}")
            else:
                print("Unknown command. Type 'quit' to exit.")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_test()
    else:
        test_server() 