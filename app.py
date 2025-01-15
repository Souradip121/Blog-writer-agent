from dotenv import load_dotenv
import os
import json
from tavily import TavilyClient
from swarm import Swarm, Agent

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
client = Swarm()

def search_web(query):
    try:
        response = tavily_client.search(query)
        # Extract relevant information from search results
        articles = [
            {
                "title": result["title"],
                "content": result["content"]
            }
            for result in response["results"][:3]  # Take top 3 results
        ]
        return json.dumps(articles, indent=2)
    except Exception as e:
        return f"Error during web search: {str(e)}"

def save_to_markdown(content, filename="output.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Content saved to {filename}"

def process_chain():
    try:
        # Initial search
        print("\n🔎 Starting web research...")
        search_response = client.run(
            agent=agent_searcher,
            messages=[{"role": "user", "content": "Atul case study"}]
        )
        print("\n📊 Search Results:")
        print(search_response.messages[-1]['content'])
        
        # Create outline
        print("\n📝 Creating outline...")
        outline_response = client.run(
            agent=agent_outliner,
            messages=[{"role": "user", "content": f"Create an outline from this research: {search_response.messages[-1]['content']}"}]
        )
        print("\n📑 Outline Created:")
        print(outline_response.messages[-1]['content'])

        # Write content
        print("\n✍️ Writing blog post...")
        writing_response = client.run(
            agent=agent_writer,
            messages=[{"role": "user", "content": f"Write a blog post following this outline: {outline_response.messages[-1]['content']}"}]
        )
        print("\n📄 First Draft:")
        print(writing_response.messages[-1]['content'])

        # Humanize content
        print("\n🎨 Humanizing content...")
        final_response = client.run(
            agent=agent_humanizer,
            messages=[{"role": "user", "content": f"Make this more engaging: {writing_response.messages[-1]['content']}"}]
        )
        print("\n✨ Final Content:")
        print(final_response.messages[-1]["content"])

        # Save the final content
        final_content = final_response.messages[-1]["content"]
        result = save_to_markdown(final_content)
        print(f"\n💾 {result}")
        return "✅ Blog post generation completed successfully!"

    except Exception as e:
        print(f"\n❌ Error occurred:")
        return f"Error in processing chain: {str(e)}"

# Web Search Agent
agent_searcher = Agent(
    name="Web Researcher",
    instructions="""
    1. Search the web for relevant content
    2. Focus on recent and reliable sources
    3. Summarize key findings in bullet points
    4. Include specific examples and data points
    """,
    functions=[search_web]
)

# Outliner Agent
agent_outliner = Agent(
    name="Content Outliner",
    instructions="""
    1. Create a hierarchical outline
    2. Include main topics and subtopics
    3. Ensure logical flow of ideas
    4. Add brief notes for each section
    """
)

# Blog Writer Agent
agent_writer = Agent(
    name="Blog Writer",
    instructions="""
    1. Follow the outline structure
    2. Write clear, engaging paragraphs
    3. Include introduction and conclusion
    4. Add transitions between sections
    """
)

# Humanizer Agent
agent_humanizer = Agent(
    name="Content Humanizer",
    instructions="""
    1. Make the tone conversational
    2. Add engaging examples
    3. Include reader engagement elements
    4. Maintain professional quality
    """,
    functions=[save_to_markdown]
)

if __name__ == "__main__":
    try:
        result = process_chain()
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")