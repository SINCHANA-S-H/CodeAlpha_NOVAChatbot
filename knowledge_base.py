KNOWLEDGE_BASE = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": (
            "Hello! 👋 I'm NOVA, your Intelligent Knowledge Assistant. "
            "How can I help you today?"
        ),
    },

    "about": {
        "keywords": ["who are you", "what are you", "about you", "introduce yourself"],
        "response": (
            "I'm NOVA, an Intelligent Knowledge Assistant designed to "
            "provide quick answers using a curated knowledge base."
        ),
    },

    "python": {
        "keywords": ["python", "python language"],
        "response": (
            "Python is a high-level, general-purpose programming language "
            "known for its simple syntax and wide use in web development, "
            "automation, data science, and artificial intelligence."
        ),
    },

    "flask": {
        "keywords": ["flask", "flask framework"],
        "response": (
            "Flask is a lightweight Python web framework used to build "
            "web applications and APIs. It provides routing, request "
            "handling, and other essential web-development features."
        ),
    },

    "cloud": {
        "keywords": [
            "cloud computing",
            "cloud",
            "cloud technology",
            "cloud deployment",
        ],
        "response": (
            "Cloud computing provides computing resources such as servers, "
            "storage, databases, and applications over the internet. "
            "It enables applications to scale without managing physical infrastructure."
        ),
    },

    "github": {
        "keywords": ["github", "git hub", "repository", "repo"],
        "response": (
            "GitHub is a platform for hosting Git repositories and "
            "collaborating on software projects. It helps developers "
            "manage source code, version history, and collaboration."
        ),
    },

    "help": {
        "keywords": ["help", "what can you do", "commands", "options"],
        "response": (
            "I can answer questions about Python, Flask, cloud computing, "
            "GitHub, and general topics available in my knowledge base. "
            "Try asking: 'What is Flask?'"
        ),
    },
}
def get_response(message):
    """
    Find the best response from NOVA's knowledge base.
    """
    message = message.lower().strip()

    for category in KNOWLEDGE_BASE.values():
        for keyword in category["keywords"]:
            if keyword in message:
                return category["response"]

    return (
        "I'm still learning. 🤖 I don't have an answer for that yet. "
        "Try asking me about Python, Flask, cloud computing, or GitHub."
    )