# Blog Writer Agent 🤖✍️

An AI-powered blog content generation system that uses multiple specialized agents to research, outline, write, and humanize blog posts.

## Features 🌟

- Web research using Tavily API
- Automated content outline generation
- AI-powered blog post writing
- Content humanization
- Markdown file output
- Multi-agent collaboration system

## Prerequisites 📋

- Python 3.8+
- OpenAI API key
- Tavily API key

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Blog-writer-agent.git
cd Blog-writer-agent
```

2. Create and activate virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # For Unix/MacOS
myenv\Scripts\activate     # For Windows
```

3. Install dependencies:
```bash
pip install python-dotenv openai tavily-python swarm-agent
```

4. Create a `.env` file with your API keys:
```properties
OPENAI_API_KEY=your-openai-api-key-here
TAVILY_API_KEY=your-tavily-api-key-here
```

## Usage 💻

Run the script:
```bash
python app.py
```

The script will:
1. Research your topic using Tavily
2. Generate a content outline
3. Write a blog post
4. Humanize the content
5. Save the result to `output.md`

## Project Structure 📁

```
Blog-writer-agent/
├── app.py              # Main application file
├── .env                # API keys and configuration
├── .gitignore         # Git ignore rules
├── output.md          # Generated blog post
└── README.md          # Project documentation
```

## Agent System 🤖

- **Web Researcher**: Searches and summarizes web content
- **Content Outliner**: Creates structured content outlines
- **Blog Writer**: Transforms outlines into blog posts
- **Humanizer**: Makes content more engaging and conversational

## Environment Variables 🔑

Required environment variables in `.env`:
- `OPENAI_API_KEY`: Your OpenAI API key
- `TAVILY_API_KEY`: Your Tavily API key

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- OpenAI for the GPT API
- Tavily for the search API
- Swarm for the agent framework