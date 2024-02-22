# Line Bot with OpenAI Integration

This project demonstrates how to integrate a Line bot with the OpenAI API to generate responses to user messages using natural language processing. (Test)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Andres-Montoya-SV/line-bot.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file from .env.example in the project root directory and add the following variables:

    ```
    LINE_CHANNEL_ACCESS_TOKEN="YOUR_LINE_CHANNEL_ACCESS_TOKEN"
    LINE_USER_ID="YOUR_LINE_USER_ID"
    OPENAI_API_KEY="YOUR_OPEN_AI_API_KEY"
    ```

4. Running the application:

    Execute the following command to start the application:

    ```bash
    python app.py
    ```

## Usage

Once the application is running, it will listen for incoming messages from the Line messaging platform. When a message is received, the bot will use the OpenAI API to generate a response and send it back to the user.

## Dependencies

- `linebot`: Python SDK for the Line Messaging API.
- `openai`: Python SDK for the OpenAI API.
- `python-dotenv`: For loading environment variables from a `.env` file.

## File Structure

- `app.py`: Main application file containing webhook handling and message generation logic.
- `requirements.txt`: List of Python dependencies.
- `.env`: Environment variables file (ignored by Git).
- `README.md`: This documentation file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
