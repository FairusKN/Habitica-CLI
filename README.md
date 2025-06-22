# Habitica-CLI

⚔️ A terminal-based Habitica companion written in Python.  
Gamify your life, manage your tasks, and track your streaks — all from your command line.

Built using the [Habitica API](https://habitica.com/apidoc).

---

## 🚀 Features

- View user stats and streaks
- Check and interact with tasks (habits, dailies, todos)
- Configurable via `.env`
- Caches API responses to reduce requests
- Optional `--refresh` flag to force fresh data
- CLI-first design using `argparse`

---

## 🔧 Installation

Clone the repo:

```bash
git clone https://github.com/FairusKN/Habitica-CLI.git
cd Habitica-CLI
```

Set up your environment:

```
cp .env.example .env
# Then edit the .env file with your Habitica API key and user ID
```

Install Dependencies:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the CLI-first:

```
python -m habitica_cli --help
```

⚙️ Commands

```
python -m habitica_cli <command> [options]
```

| Command  | Description          |
| -------- | -------------------- |
| `status` | Show user stats      |
| `task`   | Show/check tasks     |
| `streak` | Show task streaks    |
| `config` | Reconfigure API keys |

Common Flags
--refresh: Refetch API data
--api: Check if Habitica API is reachable
--version: Show CLI version

📁 .env Configuration

Copy .env.example and fill in your values:

```
HABITICA_API_KEY=your-api-token-here
HABITICA_USER_ID=your-user-id-here
```

🛠️ Known Issues

- Some subcommands may still have edge-case bugs
- TUI (Terminal UI) interface is under consideration

📌 Roadmap
✅ CLI MVP
🟡 Error handling improvements
🟡 Add unit tests
🟡 Build textual or rich-based TUI
🟡 Package as pip install habitica-cli

💡 Author

Made by [FairusKN](github.copm/FairusKN) — student.
Built to stay consistent with Habitica and make life a bit more fun.

📜 License
[MIT License](LICCENSE.md)
