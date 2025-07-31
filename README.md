# python-server-error

A simple Flask-based Python server that can generate errors on demand for testing and debugging purposes.

## Features

- **Health Check Endpoint**: Monitor server status
- **Error Generation**: Enable/disable error generation on demand
- **Sample API**: Basic CRUD-like endpoints
- **CORS Support**: Cross-origin request support
- **Logging**: Comprehensive logging for debugging

## Quick Start

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd python-sample-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### Basic Endpoints

- `GET /` - Home page with server information
- `GET /health` - Health check endpoint
- `GET /api/data` - Get all data items
- `GET /api/data/<id>` - Get specific data item by ID

### Error Management Endpoints

- `POST /error/enable` - Enable error generation
- `POST /error/disable` - Disable error generation  
- `GET /error/status` - Check error generation status
- `GET /trigger-error` - Trigger the intentional error (when enabled)

## Error Testing Workflow

### 1. Check Current Status
```bash
curl http://localhost:5000/error/status
```

### 2. Enable Error Generation
```bash
curl -X POST http://localhost:5000/error/enable
```

### 3. Trigger the Error
```bash
curl http://localhost:5000/trigger-error
```

This will return a 500 error with a `NameError` because `undefined_variable` is not defined.

### 4. Disable Error Generation
```bash
curl -X POST http://localhost:5000/error/disable
```

## The Intentional Error

The error is located in the `trigger_error()` function in `app.py`:

```python
@app.route('/trigger-error')
def trigger_error():
    """Endpoint that generates an error when enabled."""
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
```

## Fixing the Error

To fix this error, you would need to:

1. Define the `undefined_variable` or replace it with a valid variable
2. Create a pull request with the fix

Example fix:
```python
# Instead of:
result = undefined_variable + "This should cause an error"

# Use:
result = "Error triggered successfully" + " - This was the intentional error"
```

## Development

### Project Structure
```
python-sample-server/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore file
```

### Running in Development Mode

The server runs in debug mode by default, which provides:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

### Environment Variables

- `PORT` - Server port (default: 5000)

## Testing

You can test the endpoints using curl, Postman, or any HTTP client:

```bash
# Test health endpoint
curl http://localhost:5000/health

# Test data endpoint
curl http://localhost:5000/api/data

# Test error workflow
curl -X POST http://localhost:5000/error/enable
curl http://localhost:5000/trigger-error
curl -X POST http://localhost:5000/error/disable
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is open source and available under the MIT License. 
