#!/bin/bash

echo "=========================================="
echo "🚀 Starting E2E Automation Test Pipeline"
echo "=========================================="

# 1. డిపెండెన్సీస్ అప్‌గ్రేడ్ మరియు ఇన్స్టాలేషన్
echo "📦 Installing project dependencies..."
python -m pip install --upgrade pip
pip install pytest requests selenium

# 2. డేటాబేస్ మరియు ఏపీఐ టెస్ట్‌లు రన్ చేయడం
echo "🧪 Running Database and API tests..."
pytest db_test.py test_api.py -v

# 3. సెలీనియం యూఐ (UI) టెస్ట్ రన్ చేయడం
echo "🌐 Running Selenium UI Test..."
pytest test_ui_form.py -v


# 4. కొత్త అలెర్ట్ టెస్ట్ రన్ చేయడం
echo "🚨 Running Alert Popup Test..."
pytest test_alerts.py -v

echo "=========================================="
echo "✨ All Tests Completed Successfully!"
echo "=========================================="