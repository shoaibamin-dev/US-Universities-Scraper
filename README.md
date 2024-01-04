# US Universities Scraping Project

This Selenium Python project is designed to scrape details of all US universities from the [4icu.org](https://www.4icu.org/us/universities/) website. The goal is to extract comprehensive information about each university and generate a file containing the aggregated details.

## Project Overview

The project primarily involves web scraping using Selenium, a powerful tool for automating browser interactions. The target website, [4icu.org](https://www.4icu.org/us/universities/), lists various universities, and the scraper collects details such as:

- University name
- Website
- Address
- Phone number
- Description

## Dependencies

Ensure you have the following dependencies installed to run the project:

- Python
- Selenium
- Webdriver (compatible with your browser)

Install Python dependencies using the following command:

```bash
pip install selenium
```

Additionally, download the appropriate webdriver for your browser and set the path in the script.

## Running the Project

Follow these steps to run the project:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd us-universities-scraping
   ```

3. Set up your virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Download the appropriate webdriver for your browser (Chrome, Firefox, etc.) and set the path in the `scraper.py` script.

6. Run the scraper:

   ```bash
   python scraper.py
   ```

   The script will start scraping the university details from the website.

## Generated File

Once the scraping process is complete, the script will generate a file containing the details of all US universities. The filename and format can be configured in the script.

## Additional Notes

- This project relies on web scraping, and it's essential to be mindful of the website's terms of service.
- It's recommended to run the scraper responsibly to avoid any potential impact on the target website.

Feel free to explore and adapt the project for your specific needs. If you encounter any issues or have suggestions for improvement, please don't hesitate to reach out.

Happy scraping! 🌐🚀