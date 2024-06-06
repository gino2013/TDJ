# Character Upgrade Simulation

This project is a character upgrade simulation using the Clean Architecture approach, built with Streamlit for the UI.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Run Simulation](#run-simulation)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project simulates the process of upgrading characters in a game. Each character has a star level, shards, and daily shards. The goal is to upgrade characters to 6 stars by collecting shards daily. The simulation runs until all characters reach 6 stars.

## Project Structure
```
project_root/
│
├── domain/
│   └── character.py
│
├── use_cases/
│   └── use_cases.py
│
├── interface_adapters/
│   └── streamlit_interface.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `domain/character.py`: Defines the `Character` class and its methods.
- `use_cases/use_cases.py`: Contains use case functions like `redistribute_shards`, `add_new_character`, and `run_simulation`.
- `interface_adapters/streamlit_interface.py`: Manages the Streamlit UI and interacts with the use case functions.
- `main.py`: Entry point for running the Streamlit app using a subprocess.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: Project documentation.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/character-upgrade-simulation.git
    cd character-upgrade-simulation
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Adding Initial Characters
1. Open `streamlit_interface.py` and run the Streamlit app using `main.py`:
    ```sh
    python main.py
    ```

2. In the Streamlit UI, add the initial characters by filling in their names, star levels, and current shards. Click 'Add Initial Characters' to submit.

### Adding New Characters to Queue
1. In the Streamlit UI, use the form under 'Add New Characters to Queue' to add new characters.
2. Fill in the new character's name, star level, and current shards. Click 'Add New Character to Queue' to submit.

## Run Simulation
1. Click 'Run Simulation' in the Streamlit UI to start the simulation.
2. The results will display the character upgrades over time.
3. The simulation continues until all characters have reached 6 stars.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.

---

If you have any questions or need further assistance, feel free to contact the project maintainers.