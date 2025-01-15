# Project Title

## Environment Installation

To set up the environment, you can use `venv`. Follow these steps:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

## Module Installation

Install the required modules using the `requirements.txt` file. Run the following command:

```bash
pip install -r requirements.txt
```

## Agent Cases

This project includes three agent cases:

1. **main.py** - Description of what this agent does.
2. **main-olama-localai.py** - Description of what this agent does.
3. **pdf-analysis/main.py** - Description of what this agent does.

## Testing the Main Agent

To test the main agent, follow these steps:

1. Ensure that your virtual environment is activated.
2. Create a `.env` file from the `.env.example` file and add your OpenAI API key into it.
3. Run the main agent script:
   ```bash
   python main.py
   ```
4. Follow any prompts or instructions provided by the script to complete the testing process.

## Testing the PDF-Analysis Agent

To test the main agent, follow these steps:

1. Ensure that your virtual environment is activated.
2. Create a `.env` file from the `.env.example` file and add your OpenAI API key into it.
3. Create an example PDF file for testing the agent in pdf-analysis directory.
4. Run the main agent script:
   ```bash
   python main.py
   ```
5. Follow any prompts or instructions provided by the script to complete the testing process.

Make sure to check the output for any errors or confirmations that the agent is functioning as expected.