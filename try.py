from tavily import TavilyClient

# Step 1. Instantiating your TavilyClient
tavily_client = TavilyClient(api_key="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")

# Step 2. Executing a simple search query
response = tavily_client.search("What is the weather at kolkata")

# Step 3. That's it! You've done a Tavily Search!
print(response)