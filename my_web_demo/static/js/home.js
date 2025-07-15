document.addEventListener('DOMContentLoaded', () => {
    const modalOverlay = document.getElementById('modalOverlay');
    const okBtn = document.getElementById('okBtn');
    const preferenceButtons = document.querySelectorAll('.preference-btn');

    // Check if a preference is already set
    const userPreference = localStorage.getItem('shopPreference');
    if (!userPreference) {
        showModal();
    }

    function showModal() {
        if (modalOverlay) {
            modalOverlay.classList.remove('hidden');
        }
    }

    function hideModal() {
        if (modalOverlay) {
            modalOverlay.classList.add('hidden');
        }
    }

    okBtn?.addEventListener('click', () => {
        hideModal();
    });

    for (const btn of preferenceButtons) {
        btn.addEventListener('click', () => {
            const preference = btn.dataset.preference;
            if (preference) {
                localStorage.setItem('shopPreference', preference);
                console.log(`Preference set to: ${preference}`);
                hideModal();
            }
        });
    }

    // Close modal if clicked outside
    modalOverlay?.addEventListener('click', (e) => {
        if (e.target === modalOverlay) {
            hideModal();
        }
    });

    // Keyboard navigation for modal
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modalOverlay && !modalOverlay.classList.contains('hidden')) {
            hideModal();
        }
    });

    // Initialize the page
    initPage();
});

function initPage() {
    // Add event listeners for dynamic content
    addEventListeners();
    // Add animations
    addAnimations();
}

function addEventListeners() {
    // Add to cart buttons
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    for (const btn of addToCartButtons) {
        btn.addEventListener('click', () => {
            console.log('Added to cart');
            // Add your logic here
        });
    }

    // Like buttons
    const likeButtons = document.querySelectorAll('.like-btn');
    for (const btn of likeButtons) {
        btn.addEventListener('click', () => {
            btn.classList.toggle('active');
        });
    }

    // Quick view buttons
    const quickViewButtons = document.querySelectorAll('.quick-view-btn');
    for (const btn of quickViewButtons) {
        btn.addEventListener('click', () => {
            console.log('Quick view clicked');
            // Add your logic here
        });
    }

    // Search functionality
    const searchInput = document.querySelector('.search-input');
    const searchButton = document.querySelector('.search-button');

    searchButton?.addEventListener('click', () => {
        const query = searchInput?.value;
        if (query) {
            console.log(`Searching for: ${query}`);
            // Add your search logic here
        }
    });

    searchInput?.addEventListener('keyup', (e) => {
        if (e.key === 'Enter') {
            searchButton?.click();
        }
    });

    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    menuToggle?.addEventListener('click', () => {
        navLinks?.classList.toggle('active');
    });

    // Dropdown menus
    const dropdowns = document.querySelectorAll('.dropdown');
    for (const dropdown of dropdowns) {
        dropdown.addEventListener('click', (e) => {
            const target = e.target;
            if (target.classList.contains('dropdown-toggle')) {
                const content = dropdown.querySelector('.dropdown-content');
                content?.classList.toggle('show');
            }
        });
    }

    // Close dropdowns when clicking outside
    window.addEventListener('click', (e) => {
        const target = e.target;
        if (!target.closest('.dropdown')) {
            const openDropdowns = document.querySelectorAll('.dropdown-content.show');
            for (const dropdown of openDropdowns) {
                dropdown.classList.remove('show');
            }
        }
    });
}

// Wishlist button functionality
const wishlistBtn = document.querySelector('.wishlist-btn');
wishlistBtn?.addEventListener('click', () => {
    console.log('Wishlist clicked');
    // Add wishlist functionality here
});

// Cart button functionality
const cartBtn = document.querySelector('.cart-btn');
cartBtn?.addEventListener('click', () => {
    console.log('Cart clicked');
    // Add cart functionality here
});

// Shop More buttons
const shopMoreBtns = document.querySelectorAll('.shop-more-btn');
for (const btn of shopMoreBtns) {
    btn.addEventListener('click', () => {
        console.log('Shop More clicked');
        // Add shop more functionality here
    });
}

// Login/Register buttons
const loginBtn = document.querySelector('.login-btn');
const registerBtn = document.querySelector('.register-btn');

loginBtn?.addEventListener('click', () => {
    console.log('Login clicked');
    // Add login functionality here
});

registerBtn?.addEventListener('click', () => {
    console.log('Register clicked');
    // Add register functionality here
});

// Add scroll animations
function addAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        for (const entry of entries) {
            if (entry.isIntersecting) {
                entry.target.classList.add('slide-up');
            }
        }
    }, observerOptions);

    // Observe product sections and categories
    const animationTargets = document.querySelectorAll('.product-section, .product-categories, .brands');
    for (const target of animationTargets) {
        observer.observe(target);
    }
}

// Smooth scrolling for anchor links
const anchorLinks = document.querySelectorAll('a[href^="#"]');
for (const anchor of anchorLinks) {
    anchor.addEventListener('click', (e) => {
        e.preventDefault();
        const href = e.target.getAttribute('href');
        if (href) {
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        }
    });
}

// Add loading states for images
const images = document.querySelectorAll('img');
for (const img of images) {
    img.addEventListener('load', () => {
        img.classList.add('fade-in');
    });

    img.addEventListener('error', () => {
        console.log(`Failed to load image: ${img.src}`);
    });
}

// Simple cart functionality (placeholder)
const cartItems = [];

function addToCart(item) {
    cartItems.push(item);
    updateCartCount();
}

function updateCartCount() {
    const cartCount = document.querySelector('.cart-count');
    if (cartCount) {
        cartCount.textContent = cartItems.length.toString();
    }
}
