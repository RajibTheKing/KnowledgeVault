id:: 67ee443e-b7fd-444f-96c1-14b1d999a8c5
```bash
#!/bin/bash

# Replace this with your actual Bitly Access Token
ACCESS_TOKEN="<Access Token From Bitly API Setting>"

# URL to shorten (first argument passed to the script)
LONG_URL="$1"

if [ -z "$LONG_URL" ]; then
    echo "Usage: shorten_url <long_url>"
    exit 1
fi

# Make API request to Bitly
RESPONSE=$(curl -s -X POST "https://api-ssl.bitly.com/v4/shorten" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d "{\"long_url\":\"$LONG_URL\"}")

# Extract short URL from response
SHORT_URL=$(echo "$RESPONSE" | jq -r '.link')

if [ "$SHORT_URL" = "null" ]; then
    echo "Failed to shorten URL. Check your access token and input URL."
    exit 1
fi

# Copy to clipboard (using xclip or xsel)
if command -v xclip &> /dev/null; then
    echo -n "$SHORT_URL" | xclip -selection clipboard
elif command -v xsel &> /dev/null; then
    echo -n "$SHORT_URL" | xsel --clipboard --input
else
    echo "Warning: xclip or xsel not found. Install one to enable clipboard functionality."
fi

echo "Short URL: $SHORT_URL (Copied to clipboard!)"

```
