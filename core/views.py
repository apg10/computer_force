from django.shortcuts import render

CATEGORIES = [
    {"id": "audio", "title": "Audio", "img": "https://picsum.photos/seed/audio/640/420"},
    {"id": "computers", "title": "Computers", "img": "https://picsum.photos/seed/computers/640/420"},
    {"id": "graphics-cards", "title": "Graphics cards", "img": "https://picsum.photos/seed/graphics/640/420"},
    {"id": "keyboard-mice", "title": "Keyboard and mice", "img": "https://picsum.photos/seed/keyboard/640/420"},
    {"id": "laptops", "title": "Laptops", "img": "https://picsum.photos/seed/laptops/640/420"},
    {"id": "monitors", "title": "Monitors", "img": "https://picsum.photos/seed/monitors/640/420"},
    {"id": "networking", "title": "Networking", "img": "https://picsum.photos/seed/networking/640/420"},
    {"id": "peripherals", "title": "Peripherals", "img": "https://picsum.photos/seed/peripherals/640/420"},
    {"id": "printing", "title": "Printing & scanning", "img": "https://picsum.photos/seed/printing/640/420"},
    {"id": "software", "title": "Software", "img": "https://picsum.photos/seed/software/640/420"},
    {"id": "storage", "title": "Storage", "img": "https://picsum.photos/seed/storage/640/420"},
    {"id": "tablets", "title": "Tablets", "img": "https://picsum.photos/seed/tablets/640/420"},
]

HOME_CATEGORIES = [
    {"id": "computers", "title": "Computers", "img": "https://picsum.photos/seed/computers/640/420"},
    {"id": "laptops", "title": "Laptops", "img": "https://picsum.photos/seed/laptops/640/420"},
    {"id": "monitors", "title": "Monitors", "img": "https://picsum.photos/seed/monitors/640/420"},
    {"id": "printing", "title": "Printing & scanning", "img": "https://picsum.photos/seed/printing/640/420"},
    {"id": "software", "title": "Software", "img": "https://picsum.photos/seed/software/640/420"},
    {"id": "tablets", "title": "Tablets", "img": "https://picsum.photos/seed/tablets/640/420"},
]


def home(request):
    return render(request, "core/home.html", {"home_categories": HOME_CATEGORIES})


def products(request):
    q = (request.GET.get("q") or "").strip().lower()
    categories = CATEGORIES
    if q:
        categories = [c for c in CATEGORIES if q in c["title"].lower()]
    return render(request, "core/products.html", {"categories": categories, "q": request.GET.get("q", "")})


def about(request):
    return render(request, "core/about.html")

def developer_profile(request):
    return render(request, "core/developer.html")