
# Automated Test Lab 🧪 | AI Test Case Generator with Gemini

This repository aims to automate the generation of test cases for APIs and web interfaces (UI) using artificial intelligence. By providing a documentation or system URL, the project automatically creates `.feature` (Gherkin) files and Playwright `.spec.ts` test files, streamlining the process of writing and maintaining software tests.

### ☑️ You must have:

To execute the project you must have:

- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Google Gemini API Key](https://aistudio.google.com/apikey)

### How to get API Key from Google Gemini

1. Access the official website: [Google AI](https://ai.google.dev/)
2. In the menu, go to **Solutions** and select **Gemini API**.
3. Follow the instructions to generate and copy your Gemini API key.
4. Store the key in a safe place and add it to the `.env` file in the `GEMINI_API_KEY` variable.


### 🚀 Running the project:

- Clone the repository:

```bash
  $ git clone git@github.com:Automated-Test-Lab/ai-test-case-generator.git
```

- Install project dependencies:

```bash
  $ pip install -r requirements.txt
```

- Create a `.env` file in the project's root directory with the following variables:

   ```
   GEMINI_API_KEY=your_gemini_api_key
   URL_API=https://petstore.swagger.io/#/
   URL_UI=https://demos.bellatrix.solutions/
   ```

- Run scripts:

```bash
  $ python scripts/api_test_cases.py
  $ python scripts/ui_test_cases.py
```

### 📫 Contributing

To contribute to the project, follow these steps:

    1. Clone this repositoy
    2. Create a branch: git checkout -b <nome_branch>.
    3. Make your changes and commit them: git commit -m '<mensagem_commit>'
    4. Push to branch: git push origin <nome_branch>
    5. Create the merge request.