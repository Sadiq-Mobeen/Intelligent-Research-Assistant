# Intelligent-Research-Assistant
Intelligent Research Assistant is a software where user can use his locally installed ollama models to read the PDFs for him and give the ollama model instructions to get desired output as per instruction. Like "Read the given PDF and give a summary".
### Project Structure:
    Intelligent-Research-Assistant/
    │
    ├── .gitignore                # Specifies files/dirs to exclude from version control
    ├── setup.py                  # Package installation script (uses setuptools)
    ├── pyproject.toml            # Modern build system configuration (optional but recommended)
    ├── requirements.txt          # Production dependencies
    ├── requirements_dev.txt      # Development dependencies (testing, linting, etc.)
    ├── README.md                 # Project overview, setup guide, screenshots
    ├── LICENSE                   # Software license (MIT/Apache/GPL)
    ├── .env.example              # Template for environment variables
    │
    ├── src/
    │   ├── __init__.py           # Marks directory as Python package
    │   │
    │   ├── gui/                  # All GUI-related components
    │   │   ├── __init__.py
    │   │   ├── main_window.py    # Main application window layout
    │   │   │
    │   │   └── components/       # Reusable UI widgets
    │   │       ├── __init__.py
    │   │       ├── chat_box.py   # Handles user input/display (Text widgets, Send button)
    │   │       ├── pdf_browser.py # PDF selection dialog with file list display
    │   │       ├── output_panel.py # Tabs for Answer/Reasoning displays
    │   │       ├── model_selector.py # Dropdown + refresh for Ollama models
    │   │       └── status_bar.py # Bottom bar for progress/notifications
    │   │
    │   ├── handlers/             # Business logic components
    │   │   ├── __init__.py
    │   │   ├── pdf_handler.py    # PDF processing (text extraction, chunking)
    │   │   ├── ollama_handler.py # Ollama API communication (prompt construction, response parsing)
    │   │   ├── save_handler.py   # File export logic (.txt, .pdf, .csv)
    │   │   └── error_handler.py  # Centralized error handling/reporting
    │   │
    │   ├── data_models/          # Data structures and schemas
    │   │   ├── __init__.py
    │   │   ├── chat_history.py   # Conversation history storage/management
    │   │   └── application_state.py # Persists UI state between sessions
    │   │
    │   ├── utils/                # Helper functions and utilities
    │   │   ├── __init__.py
    │   │   ├── async_utils.py    # Threading/async operations management
    │   │   ├── validators.py     # Input validation (PDFs, user commands)
    │   │   ├── security.py       # File sanitization/security checks
    │   │   ├── logger.py         # Logging configuration
    │   │   └── cache_manager.py  # Caching system for processed PDFs
    │   │
    │   ├── config/               # Application configuration
    │   │   ├── __init__.py
    │   │   ├── settings.py       # User-configurable parameters
    │   │   └── logging.conf      # Logging format/configurations
    │   │
    │   └── assets/               # Static resources
    |       ├── CHANGELOG.md       # Tracks changes to assets (e.g., new icons, updated styles)
    |       ├── icons/             # Stores icons for buttons (e.g., save_icon.png, browse_icon.png)
    |       │   ├── save_icon.png
    |       │   └── browse_icon.png
    |       ├── styles/            # Stores GUI styles (e.g., for tkinter's ttk widgets)
    |       │   └── default.ttkstyle
    |       ├── themes/            # Stores theme configurations (e.g., dark/light mode)
    |       │   ├── dark.json
    |       │   └── light.json
    |       └── locales/           # Stores language files for internationalization (optional)
    |       │   ├── en.json        # English translations
    |       │   └── es.json        # Spanish translations
    |       └── samples/          # Example PDFs for testing
    │
    ├── tests/                    # Test suite
    │   ├── __init__.py
    │   ├── conftest.py           # Pytest fixtures and plugins
    │   ├── unit/                 # Unit tests
    │   │   ├── test_pdf_handler.py
    │   │   └── test_ollama_mocks.py
    │   └── integration/          # Integration tests
    │       ├── test_gui_workflow.py
    │       └── test_file_export.py
    │
    ├── docs/                     # Documentation
    │   ├── user_guide.md         # End-user instructions
    │   ├── developer_guide.md    # Architecture/contributing info
    │   └── api_reference.md      # Module-level documentation
    │
    ├── scripts/                  # Helper scripts (optional)
    │   ├── install_ollama.sh     # Dependency setup script for linux OS
    │   └── build_release.py      # Packaging automation
    │
    └── docker/                   # Containerization support (optional)
        ├── Dockerfile
        └── compose.yaml