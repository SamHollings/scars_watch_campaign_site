# Fluff Generator Module - Flask Version

The `src/fluff_generator.py` module provides a clean, reusable interface for generating Warhammer 40k campaign narrative using the Google Gemini API.

## Overview

### What It Does
- Generates post-battle fluff narratives
- Maintains conversation history
- Integrates story context from `data/ongoing_story.txt`
- Uses LangChain with Google Gemini API

### What Changed
- ❌ No longer uses Streamlit
- ✅ Pure Python module
- ✅ Works with Flask
- ✅ Can run standalone or be imported

## Usage

### 1. In Flask (Used by app.py)

```python
from src.fluff_generator import FluffGenerator

# Initialize
fluff_gen = FluffGenerator(debug_mode=False)

# Generate response
result = fluff_gen.generate_response(
    user_message="Generate a battle report for Scars Watch",
    message_history=[...]  # optional
)

# Access results
response_text = result['response']
updated_history = result['messages']
```

### 2. As a Utility Module

```python
from src import fluff_generator

# Quick generation
result = fluff_generator.generate_fluff(
    user_input="Tell me about Phlegmus",
    history=None
)

# Get initial state
initial_messages = fluff_generator.get_initial_state()

# Reset conversation
initial_messages = fluff_generator.reset_generator_state()
```

### 3. Command Line (Demo/Testing)

```bash
python -m src.fluff_generator
```

This launches an interactive command-line interface for testing the fluff generator:
```
You: What is the current state of the Red Scar?
Assistant: [Generated narrative response...]
```

Commands:
- `quit` or `exit` - Exit the program
- `reset` - Reset conversation history
- Regular text - Send a message

## Class Reference

### FluffGenerator

Main class for managing fluff generation.

#### Methods

**`__init__(debug_mode: bool = False)`**
- Initialize the generator
- Sets up the Gemini model

**`generate_response(user_message: str, message_history: List[Dict] = None) -> Dict`**
- Generate a response to a user message
- Returns: `{'response': str, 'messages': List[Dict]}` or `{'error': str, 'messages': List}`

**`get_initial_messages() -> List[Dict]`**
- Get system and initial AI messages
- Use this to start a new conversation

**`reset_conversation() -> List[Dict]`**
- Reset to initial state
- Returns fresh initial message list

**`format_message_for_display(message: Dict) -> str`**
- Format a message for pretty printing
- Returns formatted string with role emoji

## Data Flow

```
User Input
    ↓
FluffGenerator.generate_response()
    ↓
[Load story context from retrieval.py]
    ↓
[Call Gemini API with LangChain]
    ↓
[Generate narrative response]
    ↓
[Update message history]
    ↓
Return result {'response': ..., 'messages': ...}
```

## Response Structure

### Success Response
```json
{
    "response": "Generated narrative text...",
    "messages": [
        {"role": "system", "content": "..."},
        {"role": "assistant", "content": "..."},
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
    ]
}
```

### Error Response
```json
{
    "error": "Error message describing what went wrong",
    "messages": [...]
}
```

## Integration with Flask

In `app.py`:

```python
from src.fluff_generator import FluffGenerator

# Create global instance
fluff_gen = FluffGenerator(debug_mode=False)

# In API endpoint
@app.route('/api/fluff/message', methods=['POST'])
def fluff_message():
    data = request.get_json()
    result = fluff_gen.generate_response(
        data.get('message'),
        data.get('messages')
    )
    return jsonify(result)
```

## Configuration

### Environment Variables

**`DEBUG_MODE`**
- Controls debug logging
- Default: False
- Set to `true` for verbose output

**`GEMINI_API_KEY`**
- Required for API calls
- Set in `.env` file

### Story Context

The module automatically loads context from:
- File: `data/ongoing_story.txt`
- Module: `src/retrieval.py`

## Dependencies

From `requirements.txt`:
- `langchain` - LLM framework
- `langchain-google-genai` - Gemini integration
- `google-genai` - Gemini API
- `python-dotenv` - Environment config

## Example: Custom Implementation

```python
from src.fluff_generator import FluffGenerator

# Create generator
gen = FluffGenerator(debug_mode=True)

# Start conversation
messages = gen.get_initial_messages()

# User turns
user_input = "Generate a narrative about the siege of Scars Watch"
result = gen.generate_response(user_input, messages)

if 'error' in result:
    print(f"Error: {result['error']}")
else:
    print(result['response'])
    messages = result['messages']

# Follow-up
follow_up = "What happened after the siege?"
result = gen.generate_response(follow_up, messages)
print(result['response'])
```

## Performance Notes

- **First response**: 2-5 seconds (API initialization)
- **Subsequent responses**: 1-3 seconds (depends on Gemini API)
- **Message history size**: No limit, but larger histories slow generation
- **Concurrency**: Thread-safe for multiple users

## Logging

Debug output includes:
- Model initialization status
- Number of messages in context
- Truncated response preview
- Error details

Enable with:
```python
gen = FluffGenerator(debug_mode=True)
```

Or via environment:
```bash
DEBUG_MODE=true python app.py
```

## Testing

### Unit Test Example
```python
def test_fluff_generation():
    gen = FluffGenerator()
    result = gen.generate_response("Test input")

    assert 'response' in result
    assert 'messages' in result
    assert len(result['messages']) > 0
```

### Integration Test Example
```python
def test_api_endpoint(client):
    response = client.post('/api/fluff/message', json={
        'message': 'Test',
        'messages': []
    })

    assert response.status_code == 200
    data = response.get_json()
    assert 'response' in data
    assert 'messages' in data
```

## Migration from Streamlit

### What Changed
| Streamlit | Flask Module |
|-----------|--------------|
| `st.chat_input()` | `generate_response()` method |
| `st.session_state` | Function parameter `message_history` |
| `st.write()` | Return value string |
| `st.error()` | Exception/error dict |
| `st.rerun()` | Manual history management |

### Migration Path
1. Old: `python -m streamlit run fluff_generator.py`
2. New: `python app.py` (Flask with integrated API)

## Troubleshooting

### "Error generating response"
- Check `GEMINI_API_KEY` in `.env`
- Verify API credentials are valid
- Check rate limits with Gemini API

### Empty responses
- Verify `data/ongoing_story.txt` exists
- Check `GEMINI_API_KEY` is set
- Try with simpler input

### Slow responses
- May be Gemini API slowness
- Check network connection
- Monitor API quotas

## Future Enhancements

Planned improvements:
- [ ] Streaming responses
- [ ] Response caching
- [ ] Vector DB for story retrieval
- [ ] Multiple model support
- [ ] Response filtering/validation
- [ ] Persistent conversation storage
