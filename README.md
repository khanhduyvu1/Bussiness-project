
# Introduction
This project is a business application designed to help users manage their product inventory efficiently. The application allows users to control various product details such as names, quantities, and manufacturers. It leverages the power of FastAPI for the backend to handle API requests and React JSX for a responsive and user-friendly frontend. This solution aims to simplify inventory management processes and improve operational efficiency for businesses of all sizes.

Python version: 3.12.2

# Getting Started
This section provides instructions on how to get a copy of the project up and running on your local machine for development and testing purposes.

## Installation process
1. Clone the repository:
   ```bash
   git clone https://yourrepositorylink.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-project-name
   ```

## Software dependencies
- Python 3.12.2
- Node.js and npm (Node package manager)
  
  Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

  Install the required Node modules:
  ```bash
  cd frontend
  npm install
  ```

## Latest releases
You can view the latest release of the project [here](https://yourrepositorylink/releases).

## API references
Refer to the FastAPI documentation available at `http://localhost:8000/docs` after your server is running to see all available endpoints and their specifications.

# Build and Test
To build and run the application:

1. Activate the Python virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

2. Start the FastAPI backend:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Navigate to the frontend directory and start the React application:
   ```bash
   npm start
   ```

4. Run tests (make sure to write tests in the `tests` directory):
   ```bash
   pytest
   ```

# Contribute
We welcome contributions from the community! If you'd like to contribute to this project, please fork the repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For more detailed information on contributing, please refer to the [project documentation](https://yourrepositorylink/contributing).

# More Resources
If you want to learn more about creating good README files, refer to the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops).

Inspiring README examples:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)
