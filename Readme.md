# Lazio Disco Bot

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![MIT License](https://img.shields.io/badge/license-MIT-green)


Telegram bot to monitor DiSCo Lazio scholarship and accommodation status and send notifications when your acceptance status changes.

> This bot has two versions: monolithic architecture using EC2 & Serverless using AWS Lambda.


Lazio Disco Bot periodically scrapes the DiSCo portal and notifies you via Telegram when your accommodation acceptance status is updated. It supports two deployment options:

* **Monolithic**: A standalone Python script suitable for running on a server (e.g., EC2).
* **Serverless**: AWS Lambda functions (in the `lazio-serverless` directory) for a fully managed solution.

---

## Features

* 🔐 Secure login to the DiSCo portal with your credentials
* 📄 Scrape the `AccettazionePostoAlloggio` page for status updates
* 🔄 Compare current status against the “no update” baseline
* 📲 Send Telegram messages when new updates are detected
* 🌐 Translate Italian messages to English for easy reading
* ⏱️ Configurable polling interval (default: 30 minutes)

---

## Repository Structure

```
├── example.env            # Example environment variables configuration
├── requirements.txt       # Python dependencies
├── script.py              # Monolithic bot script for EC2 or any VM
├── .gitignore             # Files and folders to ignore in Git
└── Lazio-serverless/      # Serverless (AWS Lambda) deployment
```

---

## Getting Started

### Prerequisites

* Python 3.8 or higher
* AWS account (for serverless deployment)
* Telegram Bot token and chat ID

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/gambhirsharma/lazio-disco-bot.git
   cd lazio-disco-bot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   ```bash
   cp example.env .env
   ```

   Edit `.env` with your credentials:

   ```ini
   TOKEN=<your Telegram Bot API token>
   CHAT_ID=<your Telegram chat ID>
   USER_ID=<your DiSCo portal username>
   PASS=<your DiSCo portal password>
   ```

4. **Run the bot**

   ```bash
   python script.py
   ```

The bot will check for updates every 30 minutes by default.

---

## Serverless Deployment

The `Lazio-serverless` directory contains an AWS SAM (or Serverless Framework) template for deploying the bot as a Lambda function.

1. **Install AWS SAM CLI** (or Serverless Framework)
2. **Deploy**:

   ```bash
   cd Lazio-serverless
   sam deploy --guided
   # or, for Serverless Framework:
   serverless deploy
   ```
# Architecture

Below is the serverless deployment architecture for Lazio Disco Bot:


- **Scheduler**: A CloudWatch Events rule triggers the Lambda function every 30 minutes.

- **LazioBotFunction**: The AWS Lambda function retrieves encrypted credentials from KMS, scrapes the DiSCo portal, and processes the response.

- **Logging**: Execution logs are sent to CloudWatch Logs (or a DynamoDB table) for auditing and debugging.

- **Notifications**: On detecting any status change, the function sends a Telegram message to your chat.

---

## Configuration

* **Polling Interval**: Adjust the `time.sleep(1800)` value in `script.py` as needed.
* **Translation**: Remove or customize the `deep-translator` calls if translation is not required.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

