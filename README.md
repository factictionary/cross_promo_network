# Factictionary Cross-Promotion Ad Network

Centralized repository for serving house ads and cross-promotions across all Factictionary Android apps when third-party ad networks (Google AdMob / AppLovin) return sub-100% fill rates.

## Git Repository
```bash
git remote add origin https://github.com/factictionary/cross_promo_network.git
git push -u origin main
```

## CDN URL
All assets and the manifest are served globally via jsDelivr CDN:
```text
https://cdn.jsdelivr.net/gh/factictionary/cross_promo_network@main/campaigns.json
```

## Structure
- `campaigns.json`: The live manifest consumed by all apps.
- `assets/banners/`: Standard 320x50 banners and 300x250 Medium Rectangles.
- `assets/icons/`: Official 512x512 app icons.
- `assets/interstitials/`: Full-screen 1080x1920 creatives.
- `assets/videos/`: 15-second MP4 promo clips for rewarded ads.
- `validate_manifest.py`: Script to validate JSON structure and weights.
