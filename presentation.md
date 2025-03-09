---
title: "POS Inventory System"
author: "Bill Omole"
date: "March 2025"
revealOptions:
    transition: "slide"
---

# POS Inventory System

**A Django-Based API for Inventory, Sales & Administration**

- Modular design separating Administration, Products, and Sales
- RESTful endpoints built with Django REST Framework
- Asynchronous tasks with Celery & Redis
- Comprehensive logging, caching, and API documentation
- Authenitcation using django Oauth

---

## Architecture Overview

**Administration Module**
- **Business:** Manages business details (name, address, tax, owner)
- **Employee:** Employee records linked to the user model
- **Supplier:** Supplier information for products

**Products Module**
- **Category:** Categorizes products; includes images & thumbnails
- **Product:** Product details including tax, packaging, and sale status
- **Stock:** One-to-one with Product for inventory tracking
- **SupplierProduct:** Through model linking Suppliers and Products

**Sales Module**
- **Customer:** Buyer details
- **PaymentMode:** Allowed payment methods with dynamic properties
- **Sale:** Complete sale transaction (with receipt, status, etc.)
- **ProductSale:** Through model linking Products and Sales
- **Purchase:** Purchase transactions from suppliers

---

## Technical Stack

- **Backend:** Django 4.2.3, Django REST Framework, django-allauth
- **Asynchronous Tasks:** Celery 5.3.1, django-celery-beat, Flower
- **Caching & Broker:** Redis 4.6.0, hiredis 2.2.3
- **Database:** PostgreSQL (configured with dj_database_url)
- **Static Files:** Whitenoise with CompressedManifestStaticFilesStorage
- **Environment Management:** django-environ
- **API Documentation:** DRF Spectacular (Swagger UI)
- **Frontend Integration:** django-webpack-loader, crispy-forms with Bootstrap 5

---

## Key Features

- **Inventory Management:**
  - Create and manage products, categories, and stock levels
  - Automatic thumbnail generation for category images

- **Sales Management:**
  - Create sales with multi-product transactions
  - Detailed tax and pricing calculations
  - Generate reports and manage receipts

- **Administration:**
  - Manage business information, employees, and suppliers
  - Seamless nested user creation & updates for employees and business owners

- **Asynchronous Processing:**
  - Background tasks using Celery (e.g., email notifications)

---

## Deployment & Configuration

- **Settings:**
  - Managed via django-environ with a robust `.env` file
- **Database:**
  - PostgreSQL configured through dj_database_url
- **Static & Media:**
  - Static files served via Whitenoise; media stored in dedicated directories
- **Security & Logging:**
  - Secure headers, logging configuration, and error reporting
- **Cloud Ready:**
  - Deployable on platforms such as AWS, Heroku, or PythonAnywhere

---

## Challenges Faced

- **Limited Time:**
  - Tight deadlines required rapid development and deployment

- **Deployment Server Issues:**
  - Encountered difficulties getting the deployment server to work reliably

- **Limited AWS Expertise:**
  - Steep learning curve with AWS services impacted deployment choices

- **Ambitious Workload:**
  - Complex business logic and high system demands challenged scalability and performance

---

## Future Enhancements

- **Real-Time Dashboards:**
  - Live inventory and sales reporting

- **Enhanced UI/UX:**
  - Improved admin panel and customer-facing interfaces

- **External Integrations:**
  - Payment gateways, shipping APIs, and advanced analytics

- **Cloud Scalability:**
  - Further optimizations using AWS or similar cloud platforms

---

# Thank You!
