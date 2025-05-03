import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.shl.com/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send request
response = requests.get(URL, headers=headers)

# Parse content
soup = BeautifulSoup(response.content, "html.parser")

# Find table rows 
rows = soup.select("table tr")[1:]  # Skips header row

data = []

for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 4:
        name = cols[0].get_text(strip=True)
        remote = 'Yes' if '✔' in cols[1].get_text() or '•' in cols[1].get_text() else 'No'
        adaptive = 'Yes' if '✔' in cols[2].get_text() or '•' in cols[2].get_text() else 'No'
        test_types = ', '.join([tt.get_text(strip=True) for tt in cols[3].find_all("span")])
        data.append([name, remote, adaptive, test_types])

# Save to CSV
with open("shl_job_solutions.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Job Solution", "Remote Testing", "Adaptive/IRT", "Test Type"])
    writer.writerows(data)

print("✅ Scraping complete. Data saved to 'shl_job_solutions.csv'.")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC

# # Launch browser
# driver = webdriver.Chrome()
# driver.get("https://www.shl.com/en/products/")  # update this to the actual catalog URL

# # Example: Select Job Family
# job_family_dropdown = Select(driver.find_element(By.ID, "JobFamily"))  # Update with actual ID
# job_family_dropdown.select_by_visible_text("IT")

# # Click Search
# search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
# search_button.click()

# # Wait for results to load
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "result-class-name"))  # Use correct class
# )

# # Extract results (modify based on HTML structure)
# products = driver.find_elements(By.CLASS_NAME, "result-class-name")
# for product in products:
#     print(product.text)

# driver.quit()
