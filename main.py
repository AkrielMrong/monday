import os
import asyncio
import logging
from datetime import datetime, timedelta

import pymongo
import telegram
import aiohttp
from flask import Flask, request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app for keeping the server alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Website Monitoring Bot is running!", 200

class WebsiteMonitorBot:
    # [Previous implementation remains the same]
    # Modify start_bot method to use threading instead of asyncio
    def start_bot(self):
        import threading
        monitoring_thread = threading.Thread(target=self.async_monitor_hosts)
        monitoring_thread.start()

    def async_monitor_hosts(self):
        # Async version of monitor_hosts using asyncio.run()
        asyncio.run(self.monitor_hosts())

def main():
    bot = WebsiteMonitorBot()
    
    # Example usage
    bot.add_host('https://www.example.com', interval=60)
    bot.add_host('https://www.google.com', interval=120)
    
    # Start monitoring
    bot.start_bot()

if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))