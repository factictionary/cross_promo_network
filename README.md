# Factictionary Cross-Promotion Ad Network

Centralized repository for serving house ads and cross-promotions across all Factictionary Android apps when third-party ad networks (Google AdMob / AppLovin) return sub-100% fill rates.

## CDN URL Format
Files are served globally via jsDelivr CDN without hitting GitHub rate limits:
```
https://cdn.jsdelivr.net/gh/<YOUR_GITHUB_USERNAME>/<REPO_NAME>@main/campaigns.json
```

## Structure
- `campaigns.json`: The live manifest consumed by all apps.
- `assets/banners/`: Standard 320x50 banners and 300x250 Medium Rectangles.
- `assets/icons/`: Official 512x512 app icons.
- `assets/interstitials/`: Full-screen 1080x1920 creatives.
- `assets/videos/`: 15-second MP4 promo clips for rewarded ads.
- `validate_manifest.py`: Script to validate JSON structure and weights.
