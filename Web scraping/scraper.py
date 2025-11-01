import time
import asyncio
import aiohttp
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from fake_useragent import UserAgent
from .utils import setup_logging, clean_price, deduplicate_product, validate_product, send_notification

class AdvancedScraper:
    def __init__(self, site_config, advanced_config):
        self.site = site_config
        self.adv = advanced_config
        self.ua = UserAgent() if self.adv.get('user_agents_rotate', False) else None
        self.proxies = self.adv.get('proxies', [])
        self.stats = {'success': 0, 'errors': [], 'total_products': 0}
        self.deduplicated = set()
        setup_logging()
        logging.info(f"Initialized scraper for {self.site['name']}")

    def get_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
        }
        headers['User-Agent'] = self.ua.random if self.ua else 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        return headers

    def parse_product(self, elem):
        sel = self.site['selectors']
        p = {}
        name_elem = elem.select_one(sel['name'])
        p['name'] = name_elem.text.strip() if name_elem else 'N/A'
        price_elem = elem.select_one(sel['price'])
        raw_price = price_elem.text.strip() if price_elem else 'N/A'
        p['price'] = clean_price(raw_price, self.site.get('currency_regex', r'\$?(\d+[.,]?\d*)'))
        desc = elem.select_one(sel['description'])
        p['description'] = (desc.text.strip()[:200] + '...') if desc else 'N/A'
        rating = elem.select_one(sel['rating'])
        p['rating'] = rating.text.strip() if rating else 'N/A'
        img = elem.select_one(sel['image'])
        p['image'] = urljoin(self.site['base_domain'], img['src']) if img else 'N/A'
        link = elem.select_one(sel['link'])
        p['link'] = urljoin(self.site['base_domain'], link['href']) if link else 'N/A'
        return p

    def detect_captcha(self, html):
        return any(x in html.lower() for x in ['captcha', 'verify', 'recaptcha'])

    async def scrape_page_async(self, session, url, proxy=None):
        try:
            async with session.get(url, headers=self.get_headers(), proxy=proxy) as r:
                if r.status != 200:
                    self.stats['errors'].append(f"{url}: HTTP {r.status}")
                    return []
                html = await r.text()
                if self.detect_captcha(html):
                    logging.warning(f"⚠️ CAPTCHA detected at {url}")
                    return []
                soup = BeautifulSoup(html, 'html.parser')
                products = []
                for elem in soup.select(self.site['selectors']['products_container']):
                    product = self.parse_product(elem)
                    if not validate_product(product):
                        continue
                    if not deduplicate_product(product, self.deduplicated):
                        continue
                    products.append(product)
                self.stats['success'] += 1
                return products
        except Exception as e:
            self.stats['errors'].append(f"{url}: {e}")
            return []

    async def scrape_all_async(self):
        base = self.site['base_url']
        urls = [f"{base}{i}" for i in range(1, self.site['max_pages'] + 1)]
        products = []
        async with aiohttp.ClientSession() as s:
            tasks = [self.scrape_page_async(s, u) for u in urls]
            results = await asyncio.gather(*tasks)
            for res in results:
                products.extend(res)
        self.stats['total_products'] = len(products)
        return products

    def export_data(self, data):
        import csv, json
        if not data:
            logging.warning("No data to export.")
            return
        with open('products.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        if self.adv.get('export_json'):
            with open('products.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
        logging.info(f"Exported {len(data)} items.")

    def run(self):
        start = time.time()
        logging.info("🚀 Starting scraping...")
        products = asyncio.run(self.scrape_all_async()) if self.adv.get('use_async', True) else []
        self.export_data(products)
        send_notification(self.adv, self.stats)
        logging.info(f"✅ Done in {round(time.time() - start, 2)}s | {len(products)} items scraped.")
