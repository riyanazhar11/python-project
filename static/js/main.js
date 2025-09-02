// Main JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Auto-focus search input on page load
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.focus();
    }
    
    // Handle search form submission
    const searchForm = document.querySelector('.search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const query = searchInput.value.trim();
            console.log('Form submitted with query:', query);
            
            if (!query) {
                e.preventDefault();
                searchInput.focus();
                return false;
            }
            
            console.log('Form submitting...');
            
            // Add loading state to button
            const searchButton = document.querySelector('.search-button');
            if (searchButton) {
                searchButton.innerHTML = '<span>Searching...</span>';
                searchButton.disabled = true;
            }
            
            // Allow form to submit normally
            return true;
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add hover effects to company cards
    const companyCards = document.querySelectorAll('.company-card');
    companyCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Pagination buttons will submit their forms naturally without JavaScript interference
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + K to focus search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }
        
        // Escape to clear search
        if (e.key === 'Escape' && searchInput) {
            searchInput.value = '';
            searchInput.focus();
        }
    });
    
    // Add search suggestions (basic implementation)
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            const query = this.value.trim();
            
            if (query.length > 2) {
                searchTimeout = setTimeout(() => {
                    // Here you could implement search suggestions
                    // For now, we'll just add a subtle visual feedback
                    this.style.borderColor = '#3b82f6';
                }, 300);
            } else {
                this.style.borderColor = '';
            }
        });
    }
    
    // Add loading animation for page transitions
    window.addEventListener('beforeunload', function() {
        document.body.style.opacity = '0.7';
    });
    
    // Add fade-in animation for content
    const mainContent = document.querySelector('.main');
    if (mainContent) {
        mainContent.style.opacity = '0';
        mainContent.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            mainContent.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            mainContent.style.opacity = '1';
            mainContent.style.transform = 'translateY(0)';
        }, 100);
    }
});
