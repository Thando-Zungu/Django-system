# Kimberley Service Reporter

A mobile‑friendly, community‑powered reporting system for municipal service issues in Kimberley, South Africa.  
Citizens can report potholes, broken streetlights, illegal dumping, and more – with offline support, colour‑coded status tracking, and a fixed bottom navigation for easy mobile use.

---

## Features

- **Report issues** – Category, description, photo upload, address (with geolocation autofill).
- **Mobile dashboard** – Card‑based layout with colour‑coded status badges and photo previews.
- **Status tracking** – Pending → Logged → In Progress → Resolved (visible to all users).
- **Location assistance** – “Use my location” button + Plus Codes support (optional).
- **Offline‑first** – Reports are saved locally when offline and synced automatically.
- **Fixed bottom navigation** – Dashboard, New Report, Logout – works on all mobile screens.
- **Accessibility** – Large touch targets, dark mode ready, i18n support for Afrikaans/Setswana.
- **Django admin** – Full CRUD, filtering, and worker assignment.

---

## Tech Stack

- **Backend**: Django 4.2+, PostgreSQL / SQLite
- **Frontend**: Bootstrap 5, Bootstrap Icons, HTMX (optional for dynamic updates)
- **Offline sync**: IndexedDB + Service Worker (via Django‑PWA or custom)
- **Maps & location**: OpenStreetMap Nominatim (reverse geocoding) + browser Geolocation API


---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Thando-Zungu/Django-system.git
cd Django-system
