# 🚗 HourSpot - Smart AI-Powered Parking Platform

[![Vercel Deployment Ready](https://img.shields.io/badge/Deployment-Vercel%20Ready-black?logo=vercel)](https://vercel.com)
[![Status](https://img.shields.io/badge/Status-Active-emerald)](#)
[![Domain](https://img.shields.io/badge/Domain-CSE%20AIML-blue)](#)

> **HourSpot** is a smart parking platform that bridges the gap between unused private parking spaces (house driveways, empty plots, storefronts) and vehicle drivers searching for guaranteed, safe temporary parking near famous temples, hill stations, and congested city centers.

---

## 🌟 Live 3-Page Architecture

1. **Page 1: Login & Authentication Page**
   - 📱 **Mobile Phone & 6-Digit OTP** authentication simulator with instant verification.
   - 📧 **Email ID & Password / 1-Click Fast Passes** for testing as a Vehicle Driver or Space Owner.
   - 🛡️ Role-based access control.

2. **Page 2: Vehicle User (Search, AI Ranking & Instant Booking)**
   - 🔍 **Destination Search** (e.g. Famous Hilltop Temple, Hill Station Mall Road, Central Market).
   - ⚖️ **Multi-attribute Comparison**: Distance, Price/hr, Host Rating, Vehicle Type (🚗 Car, 🏍️ Bike, ⚡ EV), Availability, Security (CCTV, Guard, Covered roof).
   - 🗺️ **Interactive Spatial Map (Leaflet)** with live custom pin badges and GPS radar sync.
   - 🎟️ **Instant Booking & Payment**: Duration calculator, fee breakdown, and **Digital QR Parking Pass** generation with live check-in directions.

3. **Page 3: Space Renter / Host Portal (List & Earn)**
   - 📝 **Space Listing Wizard**: Add house driveways, storefronts, or empty plots; specify vehicle clearances, pricing, operating timings, and security amenities.
   - 📊 **Host Analytics Dashboard**: Real-time revenue tracking, platform fees breakdown, and live slot occupancy monitor.
   - 📈 **AIML Parking Demand & Dynamic Pricing Engine**: 24-hour surge predictor that forecasts peak influx times (e.g. temple aarti hours) and auto-optimizes pricing.

---

## 🎬 Live Canvas Cinematic Background Simulation
Running continuously in the background across all 3 pages:
- **Highway Scenic Vista**: Mountains, pine trees, clouds, and a distant illuminated hilltop temple shrine.
- **Roadside House**: Features a modern villa with an illuminated **"HourSpot Verified Parking"** bay.
- **Smart Car Navigation Loop**:
  1. *Cruising Highway*: Car drives along the highway with radar scan waves active.
  2. *Spot Detected*: Detects available space at the roadside house.
  3. *Driveway Turn*: Blinker activates and car turns smoothly off the highway into the private driveway.
  4. *Parked & Verified*: Comes to a safe stop inside the house garage bay with a green **"✓ Parked & Secured via HourSpot"** confirmation.

---

## 🤖 CSE (AIML) Component

### 1. Smart Parking Recommendation Algorithm
Calculates a multi-criteria utility score \(S_i \in [0, 100]\) for every candidate spot \(i\):
$$S_i = w_d \cdot (1 - \hat{d}_i) + w_p \cdot (1 - \hat{p}_i) + w_r \cdot \hat{r}_i + w_s \cdot s_i + w_a \cdot a_i$$

Where:
- \(\hat{d}_i\): Normalized walking distance to destination.
- \(\hat{p}_i\): Normalized price relative to local market average.
- \(\hat{r}_i\): Host trust score & historical review rating.
- \(s_i\): Security weight (CCTV surveillance, guard presence, gated perimeter).
- \(a_i\): Real-time availability confidence factor.

### 2. Time-Series Parking Demand & Dynamic Pricing Model
Forecasts hourly occupancy probability:
$$D(t, z) = f(\text{Hour}, \text{DayOfWeek}, \text{FestivalFlag}, \text{HistoricalOccupancy}_z)$$
- Suggests dynamic pricing multipliers ($1.15\times - 1.30\times$) during peak religious/tourist rush to maximize host earnings while maintaining high occupancy.

---

## 🚀 How to Run Locally

### Option 1: Direct Browser
Simply open `index.html` in any modern web browser (Google Chrome, Microsoft Edge, Safari, Firefox).

### Option 2: Using the Python Server
```bash
python3 server.py
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🌐 How to Deploy on Vercel

HourSpot is 100% static-ready and optimized for Vercel deployment with zero build configuration!

### Method A: Deploy via GitHub (Recommended)
1. Push this project to your GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: HourSpot smart parking platform"
   git branch -M main
   git remote add origin https://github.com/sujeeth-gounder/HP.git
   git push -u origin main
   ```
2. Go to [https://vercel.com](https://vercel.com) and log in.
3. Click **"Add New Project"** -> **"Import Git Repository"**.
4. Select `sujeeth-gounder/HP`.
5. Keep default settings (Framework Preset: *Other*) and click **"Deploy"**.
6. Vercel will instantly build and provide a live URL (e.g. `https://hp-taupe.vercel.app` or similar).

### Method B: Deploy via Vercel CLI
```bash
npm i -g vercel
vercel
```

---

## 📂 Project Structure
```
├── index.html        # Main single-page application (All 3 pages + Canvas Animation)
├── server.py         # Standalone Python backend server & mock APIs
├── package.json      # Project metadata & npm scripts
├── vercel.json       # Vercel deployment & routing configuration
└── README.md         # Documentation & setup guide
```

---

## 👥 Contributors & License
- **Project**: HourSpot Smart Parking Platform
- **Repository**: [https://github.com/sujeeth-gounder/HP](https://github.com/sujeeth-gounder/HP)
- **License**: MIT
